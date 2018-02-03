import json
from copy import deepcopy

from jsonobject import JsonObject, StringProperty, ListProperty, ObjectProperty, DictProperty, IntegerProperty

SAMPLE_LEX_EVENT = {
    "currentIntent": {
        "name": "intent-name",
        "slots": {
            "slot name1": "value",
            "slot name2": "value"
        },
        "slotDetails": {
            "slot name1": {
                "resolutions": [
                    {"value": "resolved value"},
                    {"value": "resolved value"}
                ],
                "originalValue": "original text"
            },
            "slot name2": {
                "resolutions": [
                    {"value": "resolved value"},
                    {"value": "resolved value"}
                ],
                "originalValue": "original text"
            }
        },
        "confirmationStatus": "None, Confirmed, or Denied (intent confirmation, if configured)"
    },
    "bot": {
        "name": "bot name",
        "alias": "bot alias",
        "version": "bot version"
    },
    "userId": "User ID specified in the POST request to Amazon Lex.",
    "inputTranscript": "Text used to process the request",
    "invocationSource": "FulfillmentCodeHook or DialogCodeHook",
    "outputDialogMode": "Text or Voice, based on ContentType request header in runtime API request",
    "messageVersion": "1.0",
    "sessionAttributes": {
        "key1": "value",
        "key2": "value"
    },
    "requestAttributes": {
        "key1": "value",
        "key2": "value"
    }
}


class PyLexObject(JsonObject):
    def to_dict(self):
        return self.to_json()


class ResolvedValueProperty(PyLexObject):
    """ {"value": "resolved value"} """
    value = StringProperty('')


class SlotDetailValueProperty(PyLexObject):
    """
    {
        "resolutions": [
            {"value": "resolved value"},
            {"value": "resolved value"}
        ],
        "originalValue": "original text"
    }
    """

    originalValue = StringProperty('')
    resolutions = ListProperty(ResolvedValueProperty)
    """ :type : List[ResolvedValueProperty]"""


class SlotsProperty(PyLexObject):
    pass


class SessionAttributesProperty(PyLexObject):
    pass


class RequestAttributesProperty(PyLexObject):
    pass


class CurrentIntentProperty(PyLexObject):
    name = StringProperty('')
    slots = ObjectProperty(SlotsProperty)
    slotDetails = DictProperty(SlotDetailValueProperty)
    confirmationStatus = StringProperty('')


class BotProperty(PyLexObject):
    name = StringProperty('')
    alias = StringProperty('')
    version = StringProperty('')


class LexInputEvent(PyLexObject):
    currentIntent = ObjectProperty(CurrentIntentProperty)
    """ :type : CurrentIntentProperty """
    bot = ObjectProperty(BotProperty)
    """ :type : BotProperty """
    userId = StringProperty('')
    inputTranscript = StringProperty('')
    invocationSource = StringProperty('')
    outputDialogMode = StringProperty('')
    messageVersion = StringProperty('')
    sessionAttributes = ObjectProperty(SessionAttributesProperty)
    """ :type : SessionAttributesProperty """
    requestAttributes = ObjectProperty(RequestAttributesProperty)
    """ :type : RequestAttributesProperty """

    @classmethod
    def create_class(cls, slots_property_class):
        class NewCurrentIntentProperty(CurrentIntentProperty):
            slots = ObjectProperty(slots_property_class)
            """ :type : SlotsProperty """

        class NewLexInputEvent(cls):
            currentIntent = ObjectProperty(NewCurrentIntentProperty)
            """ :type : CurrentIntentProperty """

        return NewLexInputEvent


class GenericAttachmentButtonProperty(PyLexObject):
    text = StringProperty('')
    value = StringProperty('')


class GenericAttachmentsProperty(PyLexObject):
    title = StringProperty('')
    subTitle = StringProperty('')
    imageUrl = StringProperty('')
    attachmentLinkUrl = StringProperty('')
    buttons = ListProperty(GenericAttachmentButtonProperty)
    """ :type : List[GenericAttachmentButtonProperty] """


class ResponseCardProperty(PyLexObject):
    version = IntegerProperty()
    contentType = StringProperty('application/vnd.amazonaws.card.generic')
    genericAttachments = ListProperty(GenericAttachmentsProperty)
    """ :type : List[GenericAttachmentsProperty] """


class MessageProperty(PyLexObject):
    contentType = StringProperty('PlainText')
    content = StringProperty('')


class DialogActionProperty(PyLexObject):
    type = StringProperty('')
    message = ObjectProperty(MessageProperty)
    """ :type : MessageProperty """
    responseCard = ObjectProperty(ResponseCardProperty)
    """ :type : ResponseCardProperty """


class DialogActionSlotsProperty(DialogActionProperty):
    slots = ObjectProperty(SlotsProperty)
    """ :type : dict[str, str] """


class LexOutputResponse(PyLexObject):
    dialogAction = ObjectProperty(DialogActionProperty)
    """ :type : DialogActionProperty """
    sessionAttributes = ObjectProperty(SessionAttributesProperty)
    """ :type : SessionAttributesProperty """

    def update_from_input(self, event):
        """

        :type event: LexInputEvent
        :return:
        """
        self.update_session_attributes(event)

    def update_session_attributes(self, event):
        for key, val in event.sessionAttributes.iteritems():
            self.sessionAttributes[key] = val

    def to_json(self):
        d = super(LexOutputResponse, self).to_json()
        if hasattr(self.dialogAction, 'message') and not self.dialogAction.message.content:
            del d['dialogAction']['message']
        if hasattr(self.dialogAction, 'responseCard') and self.dialogAction.responseCard.version is None:
            del d['dialogAction']['responseCard']
        return d


class CloseLexOutputResponse(LexOutputResponse):
    class CloseDialogActionProperty(DialogActionProperty):
        type = StringProperty('Close')
        fulfillmentState = StringProperty('Fulfilled')

    dialogAction = ObjectProperty(CloseDialogActionProperty)
    """ :type : CloseLexOutputResponse.CloseDialogActionProperty """


class LexOutputSlotsResponse(LexOutputResponse):
    class SubDialogActionSlotsProperty(DialogActionSlotsProperty):
        pass

    dialogAction = ObjectProperty(SubDialogActionSlotsProperty)
    """ :type : LexOutputSlotsResponse.SubDialogActionSlotsProperty """

    @classmethod
    def create_class(cls, slots_property_class):

        class NewIntentOutputResponse(LexOutputSlotsResponse):
            class SubDialogActionSlotsProperty(cls.SubDialogActionSlotsProperty):
                slots = ObjectProperty(slots_property_class)

            dialogAction = ObjectProperty(SubDialogActionSlotsProperty)
            """ :type : NewIntentOutputResponse.SubDialogActionSlotsProperty """

        return NewIntentOutputResponse

    def update_from_input(self, event):
        """

        :type event: LexInputEvent
        :return:
        """
        super(LexOutputSlotsResponse, self).update_from_input(event)
        self.update_slots(event)
        self.update_intent_name(event)

    def update_intent_name(self, event):
        if hasattr(self.dialogAction, 'intentName'):
            self.dialogAction.intentName = event.currentIntent.name

    def update_slots(self, event):
        """
        :type lex_input_event: LexInputEvent
        :return: None
        """
        if isinstance(event, LexInputEvent):
            event_slots = event.currentIntent.slots
        elif isinstance(event, basestring) or isinstance(event, unicode) or isinstance(event, str):
            event_slots = deepcopy(json.loads(event)['currentIntent']['slots'])
        else:
            event_slots = deepcopy(event['currentIntent']['slots'])

        for key, val in event_slots.iteritems():
            self.dialogAction.slots[key] = val


class ConfirmIntentOutputResponse(LexOutputSlotsResponse):
    class SubDialogActionSlotsProperty(DialogActionSlotsProperty):
        type = StringProperty('ConfirmIntent')
        intentName = StringProperty('')

    dialogAction = ObjectProperty(SubDialogActionSlotsProperty)
    """ :type : ConfirmIntentOutputResponse.SubDialogActionSlotsProperty """


class DelegateIntentOutputResponse(LexOutputSlotsResponse):
    class SubDialogActionSlotsProperty(DialogActionSlotsProperty):
        type = StringProperty('DelegateIntent')

    dialogAction = ObjectProperty(SubDialogActionSlotsProperty)
    """ :type : DelegateIntentOutputResponse.SubDialogActionSlotsProperty """


class ElicitIntentOutputResponse(LexOutputResponse):
    class ElicitIntentDialogActionProperty(DialogActionProperty):
        type = StringProperty('ElicitIntent')

    dialogAction = ObjectProperty(ElicitIntentDialogActionProperty)
    """ :type : ElicitIntentOutputResponse.ElicitIntentDialogActionProperty """


class ElicitSlotOutputResponse(LexOutputSlotsResponse):
    class SubDialogActionSlotsProperty(DialogActionSlotsProperty):
        type = StringProperty('ElicitSlot')
        intentName = StringProperty('')
        slotToElicit = StringProperty('')

    dialogAction = ObjectProperty(SubDialogActionSlotsProperty)
    """ :type : ElicitSlotOutputResponse.SubDialogActionSlotsProperty """

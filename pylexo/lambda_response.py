import json
from copy import deepcopy

from schematics import types
from schematics.schema import Field

from .base import PyLexObject, SlotsProperty, GenericAttachmentsProperty
from .input import LexInputEvent


class ResponseCardProperty(PyLexObject):
    version = types.IntType()
    contentType = types.StringType('application/vnd.amazonaws.card.generic')
    genericAttachments = types.ListType(types.ModelType(GenericAttachmentsProperty))
    """ :type : List[GenericAttachmentsProperty] """


class MessageProperty(PyLexObject):
    contentType = types.StringType(default='PlainText')
    content = types.StringType(default='')


class DialogActionProperty(PyLexObject):
    type = types.StringType(default='')
    message = types.ModelType(MessageProperty, serialize_when_none=False, default=MessageProperty())
    """ :type : MessageProperty """
    responseCard = types.ModelType(ResponseCardProperty, serialize_when_none=False, default=ResponseCardProperty())
    """ :type : ResponseCardProperty """


class DialogActionSlotsProperty(DialogActionProperty):
    slots = types.ModelType(SlotsProperty, default=SlotsProperty())
    """ :type : dict[str, str] """


class LexOutputResponse(PyLexObject):
    dialogAction = types.ModelType(DialogActionProperty, default=DialogActionProperty())
    """ :type : DialogActionProperty """
    sessionAttributes = types.DictType(types.StringType(), default={})
    """ :type : SessionAttributesProperty """

    def update_from_input(self, event):
        """

        :type event: LexInputEvent
        :return:
        """
        self.update_session_attributes(event)

    def update_session_attributes(self, event):
        for key, val in event.sessionAttributes.items():
            self.sessionAttributes[key] = val

    def to_primitive(self, role=None, app_data=None, **kwargs):
        d = deepcopy(super(LexOutputResponse, self).to_primitive(role=role, app_data=app_data, **kwargs))

        if hasattr(self.dialogAction, 'message') and not self.dialogAction.message.content:
            del d['dialogAction']['message']
        if hasattr(self.dialogAction, 'responseCard') and self.dialogAction.responseCard.version is None:
            del d['dialogAction']['responseCard']
        return d


class CloseLexOutputResponse(LexOutputResponse):
    class CloseDialogActionProperty(DialogActionProperty):
        type = types.StringType(default='Close')
        fulfillmentState = types.StringType(default='Fulfilled')

    dialogAction = types.ModelType(CloseDialogActionProperty, default=CloseDialogActionProperty())
    """ :type : CloseLexOutputResponse.CloseDialogActionProperty """


class LexOutputSlotsResponse(LexOutputResponse):
    class SubDialogActionSlotsProperty(DialogActionSlotsProperty):
        pass

    dialogAction = types.ModelType(SubDialogActionSlotsProperty, default=SubDialogActionSlotsProperty())
    """ :type : LexOutputSlotsResponse.SubDialogActionSlotsProperty """

    @classmethod
    def create_class(cls, slots_property_class):

        class NewIntentOutputResponse(LexOutputSlotsResponse):
            class SubDialogActionSlotsProperty(cls.SubDialogActionSlotsProperty):
                slots = types.ModelType(slots_property_class, default=slots_property_class())

            dialogAction = types.ModelType(SubDialogActionSlotsProperty, default=SubDialogActionSlotsProperty())
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

        for key, val in event_slots.items():
            if key not in self.dialogAction.slots._schema.fields:
                field = Field(key, types.StringType())
                self.dialogAction.slots._schema.append_field(field)
            self.dialogAction.slots[key] = val


class ConfirmIntentOutputResponse(LexOutputSlotsResponse):
    class SubDialogActionSlotsProperty(DialogActionSlotsProperty):
        type = types.StringType(default='ConfirmIntent')
        intentName = types.StringType(default='')

    dialogAction = types.ModelType(SubDialogActionSlotsProperty, default=SubDialogActionSlotsProperty())
    """ :type : ConfirmIntentOutputResponse.SubDialogActionSlotsProperty """


class DelegateIntentOutputResponse(LexOutputSlotsResponse):
    class SubDialogActionSlotsProperty(DialogActionSlotsProperty):
        type = types.StringType(default='Delegate')

    dialogAction = types.ModelType(SubDialogActionSlotsProperty, default=SubDialogActionSlotsProperty())
    """ :type : DelegateIntentOutputResponse.SubDialogActionSlotsProperty """


class ElicitIntentOutputResponse(LexOutputResponse):
    class ElicitIntentDialogActionProperty(DialogActionProperty):
        type = types.StringType(default='ElicitIntent')

    dialogAction = types.ModelType(ElicitIntentDialogActionProperty, default=ElicitIntentDialogActionProperty())
    """ :type : ElicitIntentOutputResponse.ElicitIntentDialogActionProperty """


class ElicitSlotOutputResponse(LexOutputSlotsResponse):
    class SubDialogActionSlotsProperty(DialogActionSlotsProperty):
        type = types.StringType(default='ElicitSlot')
        intentName = types.StringType(default='')
        slotToElicit = types.StringType(default='')

    dialogAction = types.ModelType(SubDialogActionSlotsProperty, default=SubDialogActionSlotsProperty())
    """ :type : ElicitSlotOutputResponse.SubDialogActionSlotsProperty """

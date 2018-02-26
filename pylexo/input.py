from schematics import types

from .base import PyLexObject

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


class ResolvedValueProperty(PyLexObject):
    """ {"value": "resolved value"} """
    value = types.StringType('')


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

    originalValue = types.StringType(default='')
    resolutions = types.ListType(types.ModelType(ResolvedValueProperty), default=[])
    """ :type : List[ResolvedValueProperty] """


class RequestAttributesProperty(PyLexObject):
    pass


class CurrentIntentProperty(PyLexObject):
    name = types.StringType()
    slots = types.DictType(types.StringType())
    slotDetails = types.DictType(types.ModelType(SlotDetailValueProperty))
    confirmationStatus = types.StringType()


class BotProperty(PyLexObject):
    name = types.StringType()
    alias = types.StringType()
    version = types.StringType()


class LexInputEvent(PyLexObject):
    currentIntent = types.ModelType(CurrentIntentProperty, default=CurrentIntentProperty())
    """ :type : CurrentIntentProperty """
    bot = types.ModelType(BotProperty, default=BotProperty())
    """ :type : BotProperty """
    userId = types.StringType()
    inputTranscript = types.StringType()
    invocationSource = types.StringType()
    outputDialogMode = types.StringType()
    messageVersion = types.StringType()
    sessionAttributes = types.DictType(types.StringType(), default={})
    requestAttributes = types.DictType(types.StringType(), default={})

    def is_all_slots_filled(self):
        return all(self.currentIntent.slots.values())

    @classmethod
    def create_class(cls, slots_property_class):
        class NewCurrentIntentProperty(CurrentIntentProperty):
            slots = types.ModelType(slots_property_class, default=slots_property_class())
            """ :type : SlotsProperty """

        class NewLexInputEvent(cls):
            currentIntent = types.ModelType(NewCurrentIntentProperty, default=NewCurrentIntentProperty())
            """ :type : CurrentIntentProperty """

        return NewLexInputEvent

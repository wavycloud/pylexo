import json

from jsonobject import JsonObject, StringProperty, ListProperty, ObjectProperty, DictProperty

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


class BotProperty(JsonObject):
    name = StringProperty()
    alias = StringProperty()
    version = StringProperty()


class SlotDetailValueProperty(JsonObject):
    """
    {
        "resolutions": [
            {"value": "resolved value"},
            {"value": "resolved value"}
        ],
        "originalValue": "original text"
    }
    """

    class ResolvedValueProperty(JsonObject):
        """ {"value": "resolved value"} """
        value = StringProperty()

    originalValue = StringProperty()
    resolutions = ListProperty(ResolvedValueProperty)

class CurrentIntentProperty(JsonObject):
    name = StringProperty()
    slots = DictProperty()
    slotDetails = DictProperty(SlotDetailValueProperty)
    confirmationStatus = StringProperty()


class LexInputEvent(JsonObject):
    currentIntent = ObjectProperty(CurrentIntentProperty)
    """ :type : CurrentIntentProperty """
    bot = ObjectProperty(BotProperty)
    """ :type : BotProperty """
    userId = StringProperty()
    inputTranscript = StringProperty()
    invocationSource = StringProperty()
    outputDialogMode = StringProperty()
    messageVersion = StringProperty()
    sessionAttributes = DictProperty()
    requestAttributes = DictProperty()


__all__ = [
    'BotProperty',
    'SlotDetailValueProperty',
    'CurrentIntentProperty',
    'LexInputEvent',
]

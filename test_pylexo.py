from pprint import pprint

from example import OrderFlowerInputEvent
from pylexo import LexInputEvent, LexOutputResponse, CloseLexOutputResponse, ElicitIntentOutputResponse
import json

orderFlowerJson = """
        {
            "messageVersion": "1.0",
            "invocationSource": "DialogCodeHook",
            "userId": "user_123",
            "sessionAttributes": {},
            "bot": {
                "name": "OrderFlowers",
                "alias": null,
                "version": "$LATEST"
            },
            "outputDialogMode": "Text",
            "currentIntent": {
                "name": "OrderFlowers",
                "slots": {
                    "PickupTime": null,
                    "FlowerType": null,
                    "PickupDate": null
                },
                "confirmationStatus": "None"
            }
        }
    """


def test_generic():
    event = LexInputEvent(json.loads(orderFlowerJson))
    d = event.to_json()
    assert event.messageVersion == '1.0'
    assert event.invocationSource == 'DialogCodeHook'
    assert event.userId == 'user_123'
    assert event.sessionAttributes == {}
    assert event.bot.name == 'OrderFlowers'
    assert event.bot.alias == None
    assert event.bot.version == '$LATEST'
    assert event.outputDialogMode == 'Text'
    assert event.currentIntent.name == 'OrderFlowers'
    assert event.currentIntent.confirmationStatus == 'None'
    assert event.currentIntent.slots['PickupTime'] == None
    assert event.currentIntent.slots['FlowerType'] == None
    assert event.currentIntent.slots['PickupDate'] == None

    event_dict = event.to_json()
    assert event_dict['messageVersion'] == '1.0'
    assert event_dict['invocationSource'] == 'DialogCodeHook'
    assert event_dict['userId'] == 'user_123'
    assert event_dict['sessionAttributes'] == {}
    assert event_dict['bot']['name'] == 'OrderFlowers'
    assert event_dict['bot']['alias'] == None
    assert event_dict['bot']['version'] == '$LATEST'
    assert event_dict['outputDialogMode'] == 'Text'
    assert event_dict['currentIntent']['name'] == 'OrderFlowers'
    assert event_dict['currentIntent']['confirmationStatus'] == 'None'
    assert event_dict['currentIntent']['slots']['PickupTime'] == None
    assert event_dict['currentIntent']['slots']['FlowerType'] == None
    assert event_dict['currentIntent']['slots']['PickupDate'] == None


def test_OrderFlower():
    event = OrderFlowerInputEvent(json.loads(orderFlowerJson))
    assert event.messageVersion == '1.0'
    assert event.invocationSource == 'DialogCodeHook'
    assert event.userId == 'user_123'
    assert event.sessionAttributes == {}
    assert event.bot.name == 'OrderFlowers'
    assert event.bot.alias == None
    assert event.bot.version == '$LATEST'
    assert event.outputDialogMode == 'Text'
    assert event.currentIntent.name == 'OrderFlowers'
    assert event.currentIntent.confirmationStatus == 'None'
    assert event.currentIntent.slots.PickupTime == None
    assert event.currentIntent.slots.FlowerType == None
    assert event.currentIntent.slots.PickupDate == None

    event_dict = event.to_json()
    assert event_dict['messageVersion'] == '1.0'
    assert event_dict['invocationSource'] == 'DialogCodeHook'
    assert event_dict['userId'] == 'user_123'
    assert event_dict['sessionAttributes'] == {}
    assert event_dict['bot']['name'] == 'OrderFlowers'
    assert event_dict['bot']['alias'] == None
    assert event_dict['bot']['version'] == '$LATEST'
    assert event_dict['outputDialogMode'] == 'Text'
    assert event_dict['currentIntent']['name'] == 'OrderFlowers'
    assert event_dict['currentIntent']['confirmationStatus'] == 'None'
    assert event_dict['currentIntent']['slots']['PickupTime'] == None
    assert event_dict['currentIntent']['slots']['FlowerType'] == None
    assert event_dict['currentIntent']['slots']['PickupDate'] == None


def test_lex_close_response():
    response = CloseLexOutputResponse()

    d = response.to_json()
    pprint(d)
    keys = d['dialogAction'].keys()
    assert 'message' not in keys
    assert 'responseCard' not in keys

def test_lex_elicit_response():
    response = ElicitIntentOutputResponse()
    d = response.to_json()
    pprint(d)
    keys = d['dialogAction'].keys()
    assert 'message' not in keys
    assert 'responseCard' not in keys
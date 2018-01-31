from pprint import pprint

import order_flower_intent
from pylexo import LexInputEvent, LexOutputResponse, CloseLexOutputResponse, ElicitIntentOutputResponse, \
    ConfirmIntentOutputResponse, ElicitSlotOutputResponse
import json

orderFlowerJson = """
        {
            "messageVersion": "1.0",
            "invocationSource": "DialogCodeHook",
            "userId": "user_123",
            "sessionAttributes": {
                "RequestorCity": "Portland"
            },
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
                    "FlowerType": "Roses",
                    "PickupDate": null
                },
                "confirmationStatus": "None"
            }
        }
    """


def test_generic():
    event = LexInputEvent(json.loads(orderFlowerJson))
    d = event.to_dict()
    assert event.messageVersion == '1.0'
    assert event.invocationSource == 'DialogCodeHook'
    assert event.userId == 'user_123'
    # assert event.sessionAttributes == {}
    assert event.bot.name == 'OrderFlowers'
    assert event.bot.alias is None
    assert event.bot.version == '$LATEST'
    assert event.outputDialogMode == 'Text'
    assert event.currentIntent.name == 'OrderFlowers'
    assert event.currentIntent.confirmationStatus == 'None'
    assert event.currentIntent.slots['PickupTime'] is None
    assert event.currentIntent.slots['FlowerType'] == 'Roses'
    assert event.currentIntent.slots['PickupDate'] is None

    event_dict = event.to_dict()
    assert event_dict['messageVersion'] == '1.0'
    assert event_dict['invocationSource'] == 'DialogCodeHook'
    assert event_dict['userId'] == 'user_123'
    assert event_dict['sessionAttributes'] == {
        "RequestorCity": "Portland"
    }
    assert event_dict['bot']['name'] == 'OrderFlowers'
    assert event_dict['bot']['alias'] is None
    assert event_dict['bot']['version'] == '$LATEST'
    assert event_dict['outputDialogMode'] == 'Text'
    assert event_dict['currentIntent']['name'] == 'OrderFlowers'
    assert event_dict['currentIntent']['confirmationStatus'] == 'None'
    assert event_dict['currentIntent']['slots']['PickupTime'] is None
    assert event_dict['currentIntent']['slots']['FlowerType'] == 'Roses'
    assert event_dict['currentIntent']['slots']['PickupDate'] is None
    confirmIntent = ConfirmIntentOutputResponse()
    confirmIntent.update_slots(event)
    assert confirmIntent.dialogAction.slots.to_dict() == event.currentIntent.slots.to_dict()


def test_OrderFlower():
    event = order_flower_intent.LexInputEvent(json.loads(orderFlowerJson))
    assert event.messageVersion == '1.0'
    assert event.invocationSource == 'DialogCodeHook'
    assert event.userId == 'user_123'
    #assert event.sessionAttributes == {}
    assert event.bot.name == 'OrderFlowers'
    assert event.bot.alias is None
    assert event.bot.version == '$LATEST'
    assert event.outputDialogMode == 'Text'
    assert event.currentIntent.name == 'OrderFlowers'
    assert event.currentIntent.confirmationStatus == 'None'
    assert event.currentIntent.slots.PickupTime is None
    assert event.currentIntent.slots.FlowerType == 'Roses'
    assert event.currentIntent.slots.PickupDate is None

    event_dict = event.to_dict()
    assert event_dict['messageVersion'] == '1.0'
    assert event_dict['invocationSource'] == 'DialogCodeHook'
    assert event_dict['userId'] == 'user_123'
    assert event_dict['sessionAttributes'] == {
        "RequestorCity": "Portland"
    }
    assert event_dict['bot']['name'] == 'OrderFlowers'
    assert event_dict['bot']['alias'] is None
    assert event_dict['bot']['version'] == '$LATEST'
    assert event_dict['outputDialogMode'] == 'Text'
    assert event_dict['currentIntent']['name'] == 'OrderFlowers'
    assert event_dict['currentIntent']['confirmationStatus'] == 'None'
    assert event_dict['currentIntent']['slots']['PickupTime'] is None
    assert event_dict['currentIntent']['slots']['FlowerType'] == 'Roses'
    assert event_dict['currentIntent']['slots']['PickupDate'] is None
    confirmIntent = order_flower_intent.ConfirmIntentOutputResponse()
    confirmIntent.update_from_input(event)
    assert confirmIntent.dialogAction.intentName == 'OrderFlowers'
    assert event.sessionAttributes.RequestorCity == confirmIntent.sessionAttributes.RequestorCity
    assert dict(confirmIntent.sessionAttributes) == dict(event.sessionAttributes)
    assert confirmIntent.dialogAction.slots.to_dict() == event.currentIntent.slots.to_dict()


def test_lex_close_response():
    response = CloseLexOutputResponse()

    d = response.to_dict()
    pprint(d)
    keys = d['dialogAction'].keys()
    assert 'message' not in keys
    assert 'responseCard' not in keys

def test_lex_elicit_response():
    response = ElicitIntentOutputResponse()
    d = response.to_dict()
    pprint(d)
    keys = d['dialogAction'].keys()
    assert 'message' not in keys
    assert 'responseCard' not in keys


def test_dynamic_output_slots_class():
    event = order_flower_intent.LexInputEvent(json.loads(orderFlowerJson))
    EllicitSlotOrderFlowerOutputResponse = ElicitSlotOutputResponse.create_class(order_flower_intent.SlotsProperty)
    response = EllicitSlotOrderFlowerOutputResponse()
    response.update_slots(event)
    assert response.dialogAction.slots.FlowerType == 'Roses'
    response.dialogAction.slots.FlowerType = 'Pink Rose'
    response_dict = response.to_dict()
    pprint(response_dict)
    assert response_dict['dialogAction']['slots']['FlowerType'] == 'Pink Rose'

def test_output_classes():
    event = order_flower_intent.LexInputEvent(json.loads(orderFlowerJson))
    response = order_flower_intent.ConfirmIntentOutputResponse()
    response.update_slots(event)
    assert response.dialogAction.slots.FlowerType == 'Roses'

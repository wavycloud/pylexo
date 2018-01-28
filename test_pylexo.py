from example import OrderFlowerInputEvent
from pylexo import LexInputEvent
import json

orderFlowerJson = """
        {
            "messageVersion": "1.0",
            "invocationSource": "DialogCodeHook",
            "userId": "ignw84y6seypre4xly5rimopuri2xwnd",
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
    assert event.messageVersion == '1.0'
    assert event.invocationSource == 'DialogCodeHook'
    assert event.userId == 'ignw84y6seypre4xly5rimopuri2xwnd'
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


def test_OrderFlower():
    event = OrderFlowerInputEvent(json.loads(orderFlowerJson))
    assert event.messageVersion == '1.0'
    assert event.invocationSource == 'DialogCodeHook'
    assert event.userId == 'ignw84y6seypre4xly5rimopuri2xwnd'
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

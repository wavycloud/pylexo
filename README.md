# pylexo
Pylexo wraps lex lambda events and converts it into an object so you don't have to remember string keys.

All you have to do is pass your event to LexInputEvent

This is what you can do with 
```python
from pylexo import LexInputEvent
event = {
    "messageVersion": "1.0",
    "invocationSource": "DialogCodeHook",
    "userId": "abcde",
    "sessionAttributes": {},
    "bot": {
        "name": "OrderFlowers",
        "alias": None,
        "version": "$LATEST"
    },
    "outputDialogMode": "Text",
    "currentIntent": {
        "name": "OrderFlowers",
        "slots": {
            "PickupTime": None,
            "FlowerType": None,
            "PickupDate": None
        },
        "confirmationStatus": "None"
    }
}

pylexo_event = LexInputEvent(event)
print("messageVersion:   {}".format(pylexo_event.messageVersion))
print("invocationSource: {}".format(pylexo_event.invocationSource))
print("userId:           {}".format(pylexo_event.userId))
print("PickupTime:       {}".format(pylexo_event.currentIntent.slots['PickupTime']))
```

# Custom Slots
if you would like to have autocomplete on slots you will have to Override LexInputEvent. Please note that we rely on jsonobject for modeling JSON schema.

```python
from jsonobject import JsonObject, StringProperty, ObjectProperty
from pylexo import CurrentIntentProperty, LexInputEvent


class OrderFlowerSlotsProperty(JsonObject):
    PickupTime = StringProperty()
    FlowerType = StringProperty()
    PickupDate = StringProperty()


class OrderFlowerCurrentIntentProperty(CurrentIntentProperty):
    slots = ObjectProperty(OrderFlowerSlotsProperty)
    """ :type : OrderFlowerSlotsProperty """


class OrderFlowerInputEvent(LexInputEvent):
    currentIntent = ObjectProperty(OrderFlowerCurrentIntentProperty)
    """ :type : OrderFlowerCurrentIntentProperty """
```

Now wrap your event using OrderFlowerInputEvent class to get autocomplete on slots
```python
pylexo_event = OrderFlowerInputEvent(event)
print("PickupTime:       {}".format(pylexo_event.currentIntent.slots.PickupTime))
print("FlowerType:       {}".format(pylexo_event.currentIntent.slots.FlowerType))
print("PickupDate:       {}".format(pylexo_event.currentIntent.slots.PickupDate))

# back to dict
event_dict = pylexo_event.to_dict()
```

# command line to generate stubs
after installing execute the following command to generate a file like order_flower_intent.py
```
pylexo -s PickupTime FlowerType PickupDate -f order_flower_intent.py
```
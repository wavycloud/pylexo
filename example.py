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

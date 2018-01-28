from pylexo import PyLexObject, CurrentIntentProperty, LexInputEvent, StringProperty, ObjectProperty


class OrderFlowerSlotsProperty(PyLexObject):
    PickupTime = StringProperty()
    FlowerType = StringProperty()
    PickupDate = StringProperty()


class OrderFlowerCurrentIntentProperty(CurrentIntentProperty):
    slots = ObjectProperty(OrderFlowerSlotsProperty)
    """ :type : OrderFlowerSlotsProperty """


class OrderFlowerInputEvent(LexInputEvent):
    currentIntent = ObjectProperty(OrderFlowerCurrentIntentProperty)
    """ :type : OrderFlowerCurrentIntentProperty """

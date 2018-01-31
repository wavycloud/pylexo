import pylexo


class Slots:
    PickupTime = "PickupTime"
    FlowerType = "FlowerType"
    PickupDate = "PickupDate"


class SessionAttributes:
    RequestorCity = "RequestorCity"

class SlotsProperty(pylexo.SlotsProperty):
    PickupTime = pylexo.StringProperty()
    FlowerType = pylexo.StringProperty()
    PickupDate = pylexo.StringProperty()


class SessionAttributesProperty(pylexo.SessionAttributesProperty):
    RequestorCity = pylexo.StringProperty()


class CurrentIntentProperty(pylexo.CurrentIntentProperty):
    slots = pylexo.ObjectProperty(SlotsProperty)
    """ :type : SlotsProperty """


class LexInputEvent(pylexo.LexInputEvent):
    currentIntent = pylexo.ObjectProperty(CurrentIntentProperty)
    """ :type : CurrentIntentProperty """
    sessionAttributes = pylexo.ObjectProperty(SessionAttributesProperty)
    """ :type : SessionAttributesProperty """


class CloseLexOutputResponse(pylexo.CloseLexOutputResponse):
    sessionAttributes = pylexo.ObjectProperty(SessionAttributesProperty)
    """ :type : SessionAttributesProperty """


class ElicitIntentOutputResponse(pylexo.ElicitIntentOutputResponse):
    sessionAttributes = pylexo.ObjectProperty(SessionAttributesProperty)
    """ :type : SessionAttributesProperty """


class ElicitSlotOutputResponse(pylexo.ElicitSlotOutputResponse):
    class SubDialogActionSlotsProperty(pylexo.ElicitSlotOutputResponse.SubDialogActionSlotsProperty):
        slots = pylexo.ObjectProperty(SlotsProperty)
        """ :type : SlotsProperty """

    dialogAction = pylexo.ObjectProperty(SubDialogActionSlotsProperty)
    """ :type : ElicitSlotOutputResponse.SubDialogActionSlotsProperty """
    sessionAttributes = pylexo.ObjectProperty(SessionAttributesProperty)
    """ :type : SessionAttributesProperty """


class ConfirmIntentOutputResponse(pylexo.ConfirmIntentOutputResponse):
    class SubDialogActionSlotsProperty(pylexo.ConfirmIntentOutputResponse.SubDialogActionSlotsProperty):
        slots = pylexo.ObjectProperty(SlotsProperty)
        """ :type : SlotsProperty """

    dialogAction = pylexo.ObjectProperty(SubDialogActionSlotsProperty)
    """ :type : ConfirmIntentOutputResponse.SubDialogActionSlotsProperty """
    sessionAttributes = pylexo.ObjectProperty(SessionAttributesProperty)
    """ :type : SessionAttributesProperty """


class DelegateIntentOutputResponse(pylexo.DelegateIntentOutputResponse):
    class SubDialogActionSlotsProperty(pylexo.DelegateIntentOutputResponse.SubDialogActionSlotsProperty):
        slots = pylexo.ObjectProperty(SlotsProperty)
        """ :type : SlotsProperty """

    dialogAction = pylexo.ObjectProperty(SubDialogActionSlotsProperty)
    """ :type : DelegateIntentOutputResponse.SubDialogActionSlotsProperty """
    sessionAttributes = pylexo.ObjectProperty(SessionAttributesProperty)
    """ :type : SessionAttributesProperty """

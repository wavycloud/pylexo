import pylexo


class SlotsProperty(pylexo.SlotsProperty):
    PickupTime = pylexo.StringProperty()
    FlowerType = pylexo.StringProperty()
    PickupDate = pylexo.StringProperty()


class CurrentIntentProperty(pylexo.CurrentIntentProperty):
    slots = pylexo.ObjectProperty(SlotsProperty)
    """ :type : SlotsProperty """


class InputEvent(pylexo.LexInputEvent):
    currentIntent = pylexo.ObjectProperty(CurrentIntentProperty)
    """ :type : CurrentIntentProperty """


class CloseLexOutputResponse(pylexo.CloseLexOutputResponse):
    pass


class ElicitIntentOutputResponse(pylexo.ElicitIntentOutputResponse):
    pass


class ElicitSlotOutputResponse(pylexo.ElicitSlotOutputResponse):
    class SubDialogActionSlotsProperty(pylexo.ElicitSlotOutputResponse.SubDialogActionSlotsProperty):
        slots = pylexo.ObjectProperty(SlotsProperty)
        """ :type : SlotsProperty """

    dialogAction = pylexo.ObjectProperty(SubDialogActionSlotsProperty)
    """ :type : ElicitSlotOutputResponse.SubDialogActionSlotsProperty """


class ConfirmIntentOutputResponse(pylexo.ConfirmIntentOutputResponse):
    class SubDialogActionSlotsProperty(pylexo.ConfirmIntentOutputResponse.SubDialogActionSlotsProperty):
        slots = pylexo.ObjectProperty(SlotsProperty)
        """ :type : SlotsProperty """

    dialogAction = pylexo.ObjectProperty(SubDialogActionSlotsProperty)
    """ :type : ConfirmIntentOutputResponse.SubDialogActionSlotsProperty """


class DelegateIntentOutputResponse(pylexo.DelegateIntentOutputResponse):
    class SubDialogActionSlotsProperty(pylexo.DelegateIntentOutputResponse.SubDialogActionSlotsProperty):
        slots = pylexo.ObjectProperty(SlotsProperty)
        """ :type : SlotsProperty """

    dialogAction = pylexo.ObjectProperty(SubDialogActionSlotsProperty)
    """ :type : DelegateIntentOutputResponse.SubDialogActionSlotsProperty """

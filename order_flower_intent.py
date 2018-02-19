import pylexo
from schematics import types

class Slots:
    PickupTime = "PickupTime"
    FlowerType = "FlowerType"
    PickupDate = "PickupDate"


class SessionAttributes:
    RequestorCity = "RequestorCity"

class SlotsProperty(pylexo.SlotsProperty):
    PickupTime = types.StringType()
    FlowerType = types.StringType()
    PickupDate = types.StringType()


class SessionAttributesProperty(pylexo.SessionAttributesProperty):
    RequestorCity = types.StringType()


class CurrentIntentProperty(pylexo.CurrentIntentProperty):
    slots = types.ModelType(SlotsProperty, default=SlotsProperty())
    """ :type : SlotsProperty """


class LexInputEvent(pylexo.LexInputEvent):
    currentIntent = types.ModelType(CurrentIntentProperty, default=CurrentIntentProperty())
    """ :type : CurrentIntentProperty """
    sessionAttributes = types.ModelType(SessionAttributesProperty, default=SessionAttributesProperty())
    """ :type : SessionAttributesProperty """


class CloseLexOutputResponse(pylexo.CloseLexOutputResponse):
    sessionAttributes = types.ModelType(SessionAttributesProperty, default=SessionAttributesProperty())
    """ :type : SessionAttributesProperty """


class ElicitIntentOutputResponse(pylexo.ElicitIntentOutputResponse):
    sessionAttributes = types.ModelType(SessionAttributesProperty, default=SessionAttributesProperty())
    """ :type : SessionAttributesProperty """


class ElicitSlotOutputResponse(pylexo.ElicitSlotOutputResponse):
    class SubDialogActionSlotsProperty(pylexo.ElicitSlotOutputResponse.SubDialogActionSlotsProperty):
        slots = types.ModelType(SlotsProperty, default=SlotsProperty())
        """ :type : SlotsProperty """

    dialogAction = types.ModelType(SubDialogActionSlotsProperty, default=SubDialogActionSlotsProperty())
    """ :type : ElicitSlotOutputResponse.SubDialogActionSlotsProperty """
    sessionAttributes = types.ModelType(SessionAttributesProperty, default=SessionAttributesProperty())
    """ :type : SessionAttributesProperty """


class ConfirmIntentOutputResponse(pylexo.ConfirmIntentOutputResponse):
    class SubDialogActionSlotsProperty(pylexo.ConfirmIntentOutputResponse.SubDialogActionSlotsProperty):
        slots = types.ModelType(SlotsProperty, default=SlotsProperty())
        """ :type : SlotsProperty """

    dialogAction = types.ModelType(SubDialogActionSlotsProperty, default=SubDialogActionSlotsProperty())
    """ :type : ConfirmIntentOutputResponse.SubDialogActionSlotsProperty """
    sessionAttributes = types.ModelType(SessionAttributesProperty, default=SessionAttributesProperty())
    """ :type : SessionAttributesProperty """


class DelegateIntentOutputResponse(pylexo.DelegateIntentOutputResponse):
    class SubDialogActionSlotsProperty(pylexo.DelegateIntentOutputResponse.SubDialogActionSlotsProperty):
        slots = types.ModelType(SlotsProperty, default=SlotsProperty())
        """ :type : SlotsProperty """

    dialogAction = types.ModelType(SubDialogActionSlotsProperty, default=SubDialogActionSlotsProperty())
    """ :type : DelegateIntentOutputResponse.SubDialogActionSlotsProperty """
    sessionAttributes = types.ModelType(SessionAttributesProperty, default=SessionAttributesProperty())
    """ :type : SessionAttributesProperty """

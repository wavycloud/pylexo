import os

template = '''import pylexo


class Slots:
{slot_strings}


class SessionAttributes:
{session_strings}

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
'''


def generate_file_string(slots, sessions=None):
    sessions = sessions or []
    session_lines = '\n'.join(
        ['    {} = pylexo.StringType()'.format(session_name) for session_name in sessions]) or '    pass'
    session_strings = '\n'.join(
        ['    {} = "{}"'.format(session_name, session_name) for session_name in sessions]) or '    pass'
    slot_lines = '\n'.join(['    {} = pylexo.StringType()'.format(slot_name) for slot_name in slots])
    slot_strings = '\n'.join(['    {} = "{}"'.format(slot_name, slot_name) for slot_name in slots])
    file_string = template.format(slot_lines=slot_lines, slot_strings=slot_strings, session_lines=session_lines,
                                  session_strings=session_strings)
    return file_string


def generate_file(filepath, slots, sessions=None):
    file_string = generate_file_string(slots, sessions)
    with open(filepath, 'w+') as fp:
        fp.write(file_string)


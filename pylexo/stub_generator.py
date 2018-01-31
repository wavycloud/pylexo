import os

template = '''import pylexo


class Slots:
{slot_strings}


class SessionAttributes:
{session_strings}

class SlotsProperty(pylexo.SlotsProperty):
{slot_lines}


class SessionAttributesProperty(pylexo.SessionAttributesProperty):
{session_lines}


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
'''


def generate_file_string(slots, sessions=None):
    sessions = sessions or []
    session_lines = '\n'.join(
        ['    {} = pylexo.StringProperty()'.format(session_name) for session_name in sessions]) or '    pass'
    session_strings = '\n'.join(
        ['    {} = "{}"'.format(session_name, session_name) for session_name in sessions]) or '    pass'
    slot_lines = '\n'.join(['    {} = pylexo.StringProperty()'.format(slot_name) for slot_name in slots])
    slot_strings = '\n'.join(['    {} = "{}"'.format(slot_name, slot_name) for slot_name in slots])
    file_string = template.format(slot_lines=slot_lines, slot_strings=slot_strings, session_lines=session_lines,
                                  session_strings=session_strings)
    return file_string


def generate_file(filepath, slots, sessions=None):
    file_string = generate_file_string(slots, sessions)
    with open(filepath, 'w+') as fp:
        fp.write(file_string)


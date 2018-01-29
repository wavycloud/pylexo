import os

template = '''import pylexo

class Slots:
{slot_strings}

class SlotsProperty(pylexo.SlotsProperty):
{slot_lines}


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
'''


def generate_file_string(slots):
    slot_lines = '\n'.join(['    {} = pylexo.StringProperty()'.format(slot_name) for slot_name in slots])
    slot_strings = '\n'.join(['    {} = "{}"'.format(slot_name, slot_name) for slot_name in slots])
    file_string = template.format(slot_lines=slot_lines, slot_strings=slot_strings)
    return file_string


def generate_file(slots, filepath):
    file_string = generate_file_string(slots)
    with open(filepath, 'w+') as fp:
        fp.write(file_string)


def generate_intent_file_strings(intent_to_slots):
    """
    :param intent_to_slots: intent name to slot {'OrderFlower': ['PickupDate', 'PickupTime', 'FlowerType']}
    :param dirpath: path to write files to
    :return: dict of intent to file_string
    """
    return {intent: generate_file_string(slots) for intent, slots in intent_to_slots.iteritems()}


def generate_intent_files(intent_to_slots, dirpath, prefix='', suffix='', lowercase=True):
    """
    :param intent_to_slots: intent name to slot {'OrderFlower': ['PickupDate', 'PickupTime', 'FlowerType']}
    :param dirpath: path to write files to
    :param prefix: filename prefix
    :param suffix: filename suffix
    :param lowercase: Whether to lowercase generated filename or not
    :return: dict of intent to file_string
    """
    """

    """
    intent_to_string = generate_intent_file_strings(intent_to_slots)

    for intent, file_string in intent_to_string.iteritems():
        filename = '{}{}{}'.format(prefix, intent, suffix)
        if lowercase:
            filename = filename.lower()
        filepath = os.path.join(dirpath, filename)
        with open(filepath, 'w+') as fp:
            fp.write(file_string)

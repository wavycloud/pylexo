import os
from argparse import ArgumentParser

import stub_generator

template = '''
import pylexo


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

def main():
    parser = ArgumentParser()
    parser.add_argument('-s','--slots', nargs='+', help='<Required> Slots names', required=True)
    parser.add_argument('-f','--filepath', help='filepath', required=False)
    args = parser.parse_args()
    slots = args.slots
    filepath = args.filepath

    if filepath:
        stub_generator.generate_file(slots, filepath)
    else:
        print(stub_generator.generate_file_string(slots))

if __name__ == '__main__':
    main()
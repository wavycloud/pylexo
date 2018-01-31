import os
from argparse import ArgumentParser

import stub_generator

def main():
    parser = ArgumentParser()
    parser.add_argument('-s','--slots', nargs='+', help='<Required> Slots names', required=True)
    parser.add_argument('-n', '--sessions', nargs='+', help='Session names', required=False)
    parser.add_argument('-f','--filepath', help='filepath', required=False)
    args = parser.parse_args()
    slots = args.slots
    sessions = args.sessions
    filepath = args.filepath

    if filepath:
        stub_generator.generate_file(filepath, slots, sessions)
    else:
        print(stub_generator.generate_file_string(slots, sessions))

if __name__ == '__main__':
    main()
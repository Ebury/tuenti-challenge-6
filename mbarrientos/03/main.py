import argparse

import sys

import yaml


class Main(object):
    """
    Challenge 03 - YATM Microservice
    """
    tape = []

    def process_tape(self, state, pos) -> str:
        if pos >= len(self.tape):
            char = ' '
        elif pos < 0:
            char = ' '
        else:
            char = self.tape[pos]

        move_char = 0
        next_state = state

        action = self.code[state][char]
        if 'write' in action.keys():
            if pos >= len(self.tape):
                self.tape.append(action['write'])
            elif pos < 0:
                self.tape.insert(0, action['write'])
            else:
                self.tape[pos] = action['write']

        if 'move' in action.keys():
            if action['move'] == 'left':
                move_char = -1
            else:
                move_char = 1

        if 'state' in action.keys():
            next_state = action['state']

        return next_state, pos + move_char

    def run(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('input', type=str)
        args = parser.parse_args()

        with open(args.input) as f:
            input = yaml.load(f.read())

        self.code = input['code']

        tapes = input['tapes']

        with open('output.txt', 'w') as f:
            for idx, t in enumerate(tapes):
                self.tape = list(tapes[t])
                next_state, next_pos = self.process_tape('start', 0)
                while next_state != 'end':
                    next_state, next_pos = self.process_tape(next_state, next_pos)
                f.write('Tape #{}: {}\n'.format(idx + 1, ''.join(self.tape)))

if __name__ == '__main__':
    main = Main()
    sys.exit(main.run())


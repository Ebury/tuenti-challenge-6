# -*- coding: utf-8 -*-
import sys
import argparse

import yaml


class State:
    def __init__(self, state, actions, tape, index):
        self.next_action = state
        self.tape = tape
        self.actions = actions
        self.index = index

    def move(self, value):
        self.index += 1 if value == 'right' else -1

    def write(self, value):
        try:
            self.tape[self.index] = value
        except IndexError:
            self.tape.append(value)

    def state(self, value):
        self.next_action = value

    def run(self):
        for k, v in self.actions.items():
            getattr(self, k)(v)

        return self.tape, self.index, self.next_action


class Main:
    def __init__(self):
        self.args = self.parse_args()
        with open(self.args.input, 'r') as f:
            parsed_input = yaml.load(f)
            self.tapes = parsed_input['tapes']
            self.states = parsed_input['code']

    def parse_args(self):
        parser = argparse.ArgumentParser()
        # Add arguments if needed
        parser.add_argument('input')
        parser.add_argument('output')
        return parser.parse_args()

    def output(self, tape):
        state_name = 'start'
        index = 0
        while state_name != 'end':
            try:
                state = State(state_name, self.states[state_name][tape[index]], tape, index)
            except IndexError:
                state = State(state_name, self.states[state_name][' '], tape, index)

            tape, index, state_name = state.run()

        return "".join(tape)

    def run(self):
        with open(self.args.output, 'w') as foutput:
            for i, tape in self.tapes.items():
                output = self.output(list(tape))
                foutput.write("Tape #%d: %s\n" % (i, output))


if __name__ == '__main__':
    main = Main()
    sys.exit(main.run())

#! /urs/bin/python2.7
import yaml


class Tape():
    def __init__(self, tape_text, code):
        self.text = [s for s in tape_text]
        self.index = 0
        self.state = 'start'
        self.code = code

    def move(self, direction):
        if direction == 'left':
            self.index -= 1
        if direction == 'right':
            self.index += 1

    def write(self, new_value):
        if self.index < len(self.text):
            self.text[self.index] = new_value
        else:
            self.text.append(new_value)

    def change_state(self, new_state):
        self.state = new_state

    def get_next_step(self, next_state):
        if self.index < len(self.text):
            return next_state[self.text[self.index]]
        else:
            return next_state[' ']

    def next_state(self):
        next_state = self.code[self.state]

        steps = self.get_next_step(next_state)
        dict_steps = {'move': self.move,
                      'state': self.change_state,
                      'write': self.write}
        for step, data in steps.iteritems():
            dict_steps[step](data)

    def start(self):
        while self.state != 'end':
            self.next_state()

if __name__ == '__main__':
    with open('submitInput') as f:
        data = yaml.load(f.read())
        code = data['code']

        for num, tape in data['tapes'].iteritems():
            tape = Tape(tape, code)
            tape.start()

            print "Tape #{}: {}".format(num, ''.join(tape.text))

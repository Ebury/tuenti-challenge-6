# -*- coding: utf-8 -*-
import sys
import argparse


class Main:
    def __init__(self):
        self.args = self.parse_args()

    def parse_args(self):
        parser = argparse.ArgumentParser()
        # Add arguments if needed
        parser.add_argument('input')
        parser.add_argument('output')
        return parser.parse_args()

    def run(self):
        with open(self.args.input, 'r') as finput:
            with open(self.args.output, 'w') as foutput:
                input_lines = int(finput.readline())
                for i, x in zip(range(1, input_lines+1), (int(x) for x in finput)):
                    if x == 0:
                        y = 0
                    elif x <= 4:
                        y = 1
                    else:
                        y = (x - 1) >> 1
                    foutput.write("Case #%d: %d\n" % (i, y))


if __name__ == '__main__':
    main = Main()
    sys.exit(main.run())


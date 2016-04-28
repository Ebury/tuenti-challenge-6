import sys
import argparse


class Main:
    def __init__(self):
        self.args = self.parse_args()

    def parse_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('input')
        parser.add_argument('output')
        return parser.parse_args()

    def run(self):
        with open(self.args.input, 'r') as finput:
            with open(self.args.output, 'w') as foutput:
                input_lines = finput.readlines()
                for i, x in enumerate(input_lines[1:]):
                    x = int(x)
                    if x == 0:
                        y = 0
                    elif x <= 4:
                        y = 1
                    elif bool(x % 2):
                        y = x / 2
                    else:
                        y = x / 2 - 1
                    foutput.write("Case #%d: %d\n" % (i + 1, y))


if __name__ == '__main__':
    main = Main()
    sys.exit(main.run())

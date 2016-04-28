# -*- coding: utf-8 -*-
import sys
import argparse
from collections import Counter


class Main:
    def __init__(self):
        self.args = self.parse_args()
        with open(self.args.corpus, 'r') as fcorpus:
            self.corpus = fcorpus.readline().strip().split()

    def parse_args(self):
        parser = argparse.ArgumentParser()
        # Add arguments if needed
        parser.add_argument('corpus')
        parser.add_argument('input')
        parser.add_argument('output')
        return parser.parse_args()

    def output(self, i, j):
        counter = Counter(self.corpus[i:j])
        return ",".join(["%s %d" % (i, j) for i, j in counter.most_common(3)])


    def run(self):
        with open(self.args.input, 'r') as finput:
            with open(self.args.output, 'w') as foutput:
                input_lines = int(finput.readline())
                for i, x in zip(range(1, input_lines+1), ([int(y) for y in x.split()] for x in finput)):
                    y = self.output(*x)
                    foutput.write("Case #%d: %s\n" % (i, y))


if __name__ == '__main__':
    main = Main()
    sys.exit(main.run())

import argparse

import sys

COMBOS = (
    ['L', 'LD', 'D', 'RD', 'R', 'P'],
    ['D', 'RD', 'R', 'P'],
    ['R', 'D', 'RD', 'P'],
    ['D', 'LD', 'L', 'K'],
    ['R', 'RD', 'D', 'LD', 'L', 'K'],
)

SUBCOMBOS = [c[:-1] for c in COMBOS]


class Main(object):
    """
    Challenge 04 - Hadouken!
    """

    def find_combos(self, seq: list) -> int:
        combos = len(set([idx+len(c) for c in COMBOS for idx, _ in enumerate(seq) if seq[idx:idx + len(c)] == c]))
        subcombos = len(set([idx+len(sc) for sc in SUBCOMBOS for idx, _ in enumerate(seq) if seq[idx:idx + len(sc)] == sc]))

        return subcombos - combos

    def run(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('input', type=str)
        args = parser.parse_args()

        with open(args.input) as f:
            input = f.readlines()

        N_CASES = int(input[0])
        cases = input[1:N_CASES+1]

        with open('output.txt', 'w') as out:
            for idx, c in enumerate(cases):
                out.write('Case #{}: {}\n'.format(idx+1, str(self.find_combos(c.rstrip().split('-')))))


if __name__ == '__main__':
    main = Main()
    sys.exit(main.run())


import argparse

import sys
from collections import Counter


class Main(object):
    """
    Challenge 02 - The Voynich Manuscript
    """
    CORPUS_FILE = 'corpus.txt'

    def run(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('input', type=str)
        args = parser.parse_args()

        with open(self.CORPUS_FILE) as f:
            corpus_words = f.readlines()[0].split()

        with open(args.input) as f:
            lines = f.readlines()

        n_fragments = lines[0]
        fragments = lines[1:]

        with open('output.txt', 'w') as output:
            for idx, f in enumerate(fragments):
                freq = Counter()
                start, end = f.split()
                fragment_words = corpus_words[int(start):int(end)]

                for w in fragment_words:
                    freq[w] += 1

                winners = freq.most_common(3)

                output.write('Case #{}: {}\n'.format(idx+1, ','.join(['{} {}'.format(w[0], w[1]) for w in winners])))


if __name__ == '__main__':
    main = Main()
    sys.exit(main.run())


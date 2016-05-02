import re
import sys
import telnetlib
from collections import defaultdict, Counter

MAX_TRIES = 10


class Main(object):
    """
    Challenge 05 - Hangman!
    """

    def __init__(self):
        self.telnet = telnetlib.Telnet('52.49.91.111', 9988)

        with open('words.txt') as f:
            words_raw = f.read().split('\n')

        self.words = defaultdict(list)
        for w in words_raw:
            self.words[len(w)].append(w)
        self.words_count = {length: Counter(''.join(self.words[length])) for length in self.words.keys()}

    def most_frequent(self, word_length: int, filter: list, exclude: list = None):
        filter_re_string = ''.join(filter).replace('_', '.')
        print("Filtering with regex '{}'".format(filter_re_string))
        regex = re.compile(filter_re_string, re.IGNORECASE)
        _words = [w for w in self.words[word_length] if regex.match(w)]
        words_count = Counter(''.join(_words))

        if exclude:
            for c in exclude:
                try:
                    words_count.pop(c)
                except KeyError:
                    pass

        return words_count.most_common(1)[0][0]

    def guess(self):
        fails = 0
        found = False
        tried_letters = []
        self.telnet.write(b'\n')
        pre_guess = []
        game_over = False
        while not game_over and not found:
            screen = self.telnet.read_until(b'>', 2)
            print(screen.split(b'\n'))

            if b'GAME OVER' in b''.join(screen.split(b'\n')):
                print("GAME OVER!")
                game_over = True
                continue

            # Reading actual status of word guessed against previous try
            actual_guess = [c.decode('utf-8') for c in screen.split(b'\n')[-3].split()]
            if not pre_guess:
                pre_guess = actual_guess
            elif actual_guess == pre_guess:
                fails += 1
            elif '_' not in actual_guess:
                found = True
                print('FOUND! Correct guess was: {}'.format(actual_guess))

            else:
                pre_guess = actual_guess

            if not found:
                print("Actual guess: {}".format(actual_guess))
                try_letter = self.most_frequent(len(pre_guess), filter=actual_guess, exclude=tried_letters)
                print("Trying with letter: {}".format(try_letter))
                self.telnet.write(str(try_letter).encode() + b"\n")
                tried_letters.append(try_letter)

        return found

    def run(self):

        for i in range(MAX_TRIES):
            found = self.guess()
            print(found)
            while found:
                self.guess()
                print(found)


if __name__ == '__main__':
    main = Main()
    sys.exit(main.run())

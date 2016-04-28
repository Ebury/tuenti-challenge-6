import sys
from collections import Counter


def main():
    with open(sys.argv[1]) as corpus_file:
        corpus = corpus_file.read().split(' ')

    with open(sys.argv[2]) as input_file:
        content = input_file.readlines()[1:]

    output_file = open('output.txt', 'w')
    max = len(content) if len(content) < 5000 else 5000

    for position in range(0, max):
        limits = content[position].split(' ')

        sliced_corpus = corpus[int(limits[0])-1:int(limits[1])]

        repetitions = Counter(sliced_corpus).most_common(3)

        output_file.write('Case #{0}: {1},{2},{3}\n'.format(position + 1,
                                                            '{} {}'.format(repetitions[0][0], repetitions[0][1]),
                                                            '{} {}'.format(repetitions[1][0], repetitions[1][1],),
                                                            '{} {}'.format(repetitions[2][0], repetitions[2][1],)))

    output_file.close()

if __name__ == "__main__":
    main()

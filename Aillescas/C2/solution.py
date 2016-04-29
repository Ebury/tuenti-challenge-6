#! /urs/bin/python2.7


def solve(r1, r2, corpus):
    sub_corpus = corpus[r1 - 1: r2]
    res, dictionary = get_frecuency(sub_corpus)

    return "{} {},{} {},{} {}".format(res[0][0], res[0][1], res[1][0], res[1][1], res[2][0], res[2][1])


def get_frecuency(corpus):
    dict_frecuency = {}
    first_three = [['', 0], ['', 0], ['', 0]]
    for w in corpus:
        f = dict_frecuency.get(w, 0)
        f += 1
        first, second, third = first_three
        if first[1] <= f:
            if first[0] != w:
                third[0] = second[0]
                third[1] = second[1]
                second[0] = first[0]
                second[1] = first[1]
            first[0] = w
            first[1] = f

        elif second[1] <= f:
            if second[0] != w:
                third[0] = second[0]
                third[1] = second[1]
            second[0] = w
            second[1] = f

        elif third[1] <= f:
            third[0] = w
            third[1] = f

        dict_frecuency[w] = f

    return first_three, dict_frecuency

if __name__ == '__main__':
    corpus = ''
    with open('corpus.txt') as f:
        corpus = f.read().split(' ')
    with open('submitInput') as f:
        cases = int(f.readline())
        for i in xrange(cases):
            range1, range2 = [int(val) for val in f.readline().split(' ')]
            print "Case #{}: {}".format(i + 1, solve(range1, range2, corpus))

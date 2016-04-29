import re

combos = [['L', 'LD', 'D', 'RD', 'R', 'P'],
          ['D', 'RD', 'R', 'P'],
          ['R', 'D', 'RD', 'P'],
          ['D', 'LD', 'L', 'K'],
          ['R', 'RD', 'D', 'LD', 'L', 'K']]


def invalid_combos(movements):
    #import ipdb; ipdb.set_trace()

    failed_pos = []
    for combo in combos:
        failed_combo = '-'.join(combo[:-1])
        positions = [(m.start(), m.end()) for m in re.finditer('(?={})'.format(failed_combo), movements)]
        for position in positions:
            if movements.find('-'.join(combo), position[0]) == -1:
                failed_pos.append(position[1])
    return failed_pos

if __name__ == '__main__':
    with open('testInput') as f:
        num = int(f.readline())

        for c in xrange(num):
            movements = f.readline().strip()
            print "Case #{}: {}".format(c + 1, len(invalid_combos(movements)))

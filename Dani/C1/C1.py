import sys, math

def main():
    with open(sys.argv[1]) as f:
        content = f.readlines()[1:]

    f = open('output.txt', 'w')
    max = len(content) if len(content) < 50 else 50
    for position in range(0, max):

        diners = int(content[position])

        if diners == 0:
            tables = 0
        else:
            tables = int(math.ceil((diners-2) / 2.0)) if diners > 4 else 1

        f.write('Case #{0}: {1}\n'.format(position+1, tables))

    f.close()

if __name__ == "__main__":
    main()
#! /urs/bin/python


def solve(team_members_num):
    # Easiest case tem_members_num == 0
    if team_members_num == 0:
        return 0
    # Easy case team_members less or equal than 4
    if team_members_num <= 4:
        return 1
    else:
        # The initial and final table can accomodate 3 people, the rest 2
        tables = 2
        team_members_in_the_middle = team_members_num - 6
        if team_members_in_the_middle > 0:
            tables_in_the_middle = round((float(team_members_in_the_middle) / 2.0))
            tables += tables_in_the_middle

        return int(tables)

if __name__ == '__main__':
    with open('submitInput.txt') as f:
        cases = int(f.readline())
        for i in xrange(cases):
            print "Case #{}: {}".format(i + 1, solve(int(f.readline().strip())))

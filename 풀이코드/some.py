'''def longest_streak(s):
    if s != '':
        contender = leader = s[0]
        streak_length = streak_record = 1
        for n in s[1:]:
            if n == contender:
                streak_length = streak_length + 1
            else:
                contender = n
                streak_length = 1
            if streak_length > streak_record:
                leader = contender
                streak_record = streak_length
        return leader, streak_record
    else:
        return None

for s in longest_streak(input()):
    print(s)'''


def sublists(ns):
    def loop(turn,ns):
        sub =[]
        for i in range(len(ns)-turn+1):
            sub.append(ns[i:i+turn])
        return sub
    sub = [[]]
    for turn in range(1,len(ns)):
        sub += loop(turn,ns)
    if sub !=[]:
        sub.append(ns)
    return sub
sublists([1,2,3,4,5,8,4,7])
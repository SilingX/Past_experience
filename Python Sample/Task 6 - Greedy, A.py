#!/usr/bin/env python
# coding: utf-8

# # Task 6 - Greedy, A*
# 
# In this final task, you should modify your solution to Task 4 to include the greedy and A* algorithms. The input and output should be in exactly the same format. The only difference is that the first input can now be d, b, i, u, g or a, where g indicates greedy search and a indicates A* search. Use the heuristic we developed in Task 5 for these informed search strategies.

# In[ ]:


import sys
from io import StringIO

sys.setrecursionlimit(2000)


def heuristic(text, is_goal):
    if is_goal:
        return 0
    keys = "ETAONS"
    count = [ch.upper() for word in text for ch in word if ch.upper() in keys]
    counter = {key: count.count(key) for key in keys}
    num = 0
    freq = ''.join(sorted(counter, key=(lambda k: (-counter[k], k))))
    for i, j in zip(freq, keys):
        num += i != j
    return (num+1) // 2


def successors(text):
    ans = []
    for a, b in GROUPS:
        def change(word): return ''.join([a if ch == b
                                          else a.lower() if ch == b.lower()
                                          else b if ch == a
                                          else b.lower() if ch == a.lower()
                                          else ch for ch in word])

        ans.append((change(text), f'{a}{b}'))
    return ans


def match(message):
    '''
    calculate the match rate of message and d
    message: the message to be split
    '''

    def simplify(string): return ''.join(ch for ch in string if ch.isalpha())
    message = [simplify(word) for word in message.split()]

    num = 0
    for word in message:
        num += 1 if word.lower() in DICTIONARY else 0
    percent = num / len(message) * 100

    return percent


def task6(al, secret, d, t, swap, p):
    global DICTIONARY, GROUPS, THRESHOLD, NODES, FRINGES, DEPTH
    DICTIONARY = set(''.join(list(open(d))).split())
    swap = sorted(swap)
    GROUPS = [(i, j) for idx, i in enumerate(swap[:-1])
              for j in swap[idx+1:]]
    THRESHOLD = t
    NODES = DEPTH = FRINGES = 0

    secret = open(secret).read()
    func = {
        'g': GREEDY,
        'a': A_STAR,
    }
    output = StringIO()

    result = func[al](secret)
    if not result:
        print('No solution found.', file=output)
    else:
        print("Solution:", result[0], end='\n\n', file=output)
        print("Key:", result[1], file=output)
        print("Path Cost:", len(result[1])//2, file=output)

    print("\nNum nodes expanded:", NODES, file=output)
    print("Max fringe size:", FRINGES, file=output)
    print("Max depth:", DEPTH, end='', file=output)
    if p == 'y':
        print("\n\nFirst few expanded states:", file=output)
        print('\n\n'.join(m for m in memory), end='', file=output)
    return output.getvalue()


memory = []


def GREEDY(root):
    fringe = [(root, 0, heuristic(root, match(root) >= THRESHOLD), '')]
    global NODES, FRINGES, DEPTH
    while fringe:
        if NODES >= 1000:
            return
        cur, g, h, path = fringe.pop(0)
        DEPTH = max(DEPTH, len(path) // 2)
        if len(memory) < 10:
            memory.append(cur)
        NODES += 1
        if match(cur) >= THRESHOLD:
            return cur, path
        fringe = fringe + [(child, g+1, heuristic(child, match(child) >= THRESHOLD), path+group)
                           for child, group in successors(cur)]
        fringe.sort(key=(lambda x: (x[2])))
        FRINGES = max(FRINGES, len(fringe))


def A_STAR(root):
    fringe = [(root, 0, heuristic(root, match(root) >= THRESHOLD), '')]
    global NODES, FRINGES, DEPTH
    while fringe:
        if NODES >= 1000:
            return
        cur, g, h, path = fringe.pop(0)
        DEPTH = max(DEPTH, len(path) // 2)
        if len(memory) < 10:
            memory.append(cur)
        NODES += 1
        if match(cur) >= THRESHOLD:
            return cur, path
        fringe = fringe + [(child, g+1, heuristic(child, match(child) >= THRESHOLD), path+group)
                           for child, group in successors(cur)]
        fringe.sort(key=(lambda x: (x[1]+x[2])))
        FRINGES = max(FRINGES, len(fringe))


if __name__ == '__main__':
    ...
    # Example function calls below, you can add your own to test the task4 function
    # print(task6('a', 'scrambled_quokka3.txt',
    #      'common_words.txt', 90, 'AENOST', 'y'))


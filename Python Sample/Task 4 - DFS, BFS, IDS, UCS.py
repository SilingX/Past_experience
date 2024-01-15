#!/usr/bin/env python
# coding: utf-8

# # Task 4 - DFS, BFS, IDS, UCS
# 
# In this task, you will now combine all your work so far to write a function to perform uninformed searches. It should take six inputs:
# 
# 1. A character (d, b, i or u) specifying the algorithm (DFS, BFS, IDS and UCS, respectively)
# 2. The name of a text file containing a secret message
# 3. The name of a text file containing a list of words, in alphabetical order and each on a separate line, which will act as a dictionary of correct words
# 4. A threshold, t, specifying what percentage of words must be correct for this to count as a goal (given as an integer between 0 and 100).
# 5. A string containing the letters that are allowed to be swapped
# 6. A character (y or n) indicating whether to print the messages corresponding to the first 10 expanded nodes.
# 
# It should then perform DFS, BFS, IDS or UCS to search for a decryption to the given message, reusing your code from previous tasks if you would like to. Note that children should be generated in the same order as in Task 2, and you do not need to handle cycles. In the case of UCS, if two nodes have the same priority for expansion, you should expand the node that was added to the fringe first, first. Additionally, you should stop the search if 1000 nodes have been expanded without finding a solution.
# 
# The function should return a string. This string must contain the following information, in order:
# 
# 1. The decrypted message, key for generating that message and the path cost, if a solution was found. If no solution was found, the program should print, "No solution found."
# 2. The number of nodes expanded during the search. Note that the start node counts as an expanded node and, in the case of IDS, the final expanded node count should be the sum of the expanded node counts on each iteration.
# 3. The maximum number of nodes in the fringe at the same time during the search
# 4. The maximum search depth reached. That is, the depth of the deepest expanded node. Note that the start node has a depth of 0, and its children have depths of 1.
# 5. (If indicated with y) the messages corresponding to the first 10 expanded nodes in the search. If less than 10 nodes were expanded, it should print all expanded nodes.
# 

# In[ ]:


import sys
from io import StringIO

sys.setrecursionlimit(2000)


def successors(text):
    ans = []
    text = ' '.join(text)
    for a, b in GROUPS:
        if a not in text.upper() and b not in text.upper():
            continue
        new_chs = [a if ch == b
                   else a.lower() if ch == b.lower()
                   else b if ch == a
                   else b.lower() if ch == a.lower()
                   else ch for ch in text]
        ans.append((''.join(new_chs).split(), f'{a}{b}'))
    return ans


def match(message):
    '''
    calculate the match rate of message and d
    message: the message to be split
    '''

    def simplify(string): return ''.join(ch for ch in string if ch.isalpha())
    message = [simplify(word) for word in message]

    num = 0
    for word in message:
        num += 1 if word.lower() in DICTIONARY else 0
    percent = num / len(message) * 100

    return percent


def task4(al, secret, d, t, swap, p):
    global DICTIONARY, GROUPS, THRESHOLD, NODES, FRINGES, DEPTH
    DICTIONARY = set(''.join(list(open(d))).split())
    swap = sorted(swap)
    GROUPS = [(i, j) for idx, i in enumerate(swap[:-1])
              for j in swap[idx+1:]]
    THRESHOLD = t
    NODES = DEPTH = FRINGES = 0

    def simplify(string): return ''.join(ch for ch in string)
    secret = [simplify(word) for word in ''.join(list(open(secret))).split()]

    func = {
        'b': BFS,
        'd': DFS,
        'i': IDS,
        'u': UCS
    }
    output = StringIO()

    result = func[al](secret)
    if not result:
        print('No solution found.', file=output)
    else:
        print("Solution:", *result[0], end='\n\n', file=output)
        print("Key:", result[1], file=output)
        print("Path Cost:", len(result[1])//2, file=output)

    print("\nNum nodes expanded:", NODES, file=output)
    print("Max fringe size:", FRINGES, file=output)
    print("Max depth:", DEPTH, end='', file=output)
    if p == 'y':
        print("\n\nFirst few expanded states:", file=output)
        print('\n\n'.join([' '.join(m) for m in memory]), end='', file=output)
    return output.getvalue()


memory = []


def DFS(root, maxdepth=1000):
    fringe = [(root, 0, '')]
    global NODES, FRINGES, DEPTH
    while fringe:
        if NODES >= 1000:
            return
        cur, depth, path = fringe.pop(0)
        DEPTH = max(DEPTH, depth)
        if len(memory) < 10:
            memory.append(cur)
        if depth >= 1000:
            return
        NODES += 1
        if match(cur) >= THRESHOLD:
            return cur, path
        if depth >= maxdepth:
            continue

        fringe = [(child, depth+1, path+group)
                  for child, group in successors(cur)] + fringe
        FRINGES = max(FRINGES, len(fringe))


def BFS(root):
    fringe = [(root, '')]
    waiting_list = []
    global NODES, FRINGES, DEPTH
    while True:
        while fringe:
            if NODES >= 1000:
                return
            cur, path = fringe.pop(0)
            if len(memory) < 10:
                memory.append(cur)
            if DEPTH > 999:
                return
            NODES += 1
            if match(cur) >= THRESHOLD:
                return cur, path
            waiting_list.extend([(child, path+group)
                                for child, group in successors(cur)])
            FRINGES = max(FRINGES, len(fringe) + len(waiting_list))
        if waiting_list:
            fringe = waiting_list
            waiting_list = []
        else:
            return
        DEPTH += 1


def IDS(root):
    max_depth = 0
    global DEPTH
    while True:
        result = DFS(root, max_depth)
        if NODES >= 1000:
            return
        if result:
            DEPTH = max_depth
            return result
        max_depth += 1


def UCS(root):
    return BFS(root)


if __name__ == '__main__':
    # Example function calls below, you can add your own to test the task4 function
    #print(task4('d', 'cabs.txt', 'common_words.txt', 100, 'ABC', 'y'))
    # print(task4('d', 'abc.txt', 'common_words.txt', 100, 'ABC', 'y'))
    print(task4('d', 'cabs.txt', 'common_words.txt', 100, 'ABC', 'y'))
    # print(task4('i', 'spain.txt', 'common_english_words_online.txt', 80, 'ADE', 'n'))


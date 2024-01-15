#!/usr/bin/env python
# coding: utf-8

# # Task 5 - Heuristics
# 
# Your task is to write a function that compares this theoretical ordering to the letter ordering in a given message, then estimates how many letter swaps would be needed to make them the same. The function should take two inputs:
# 
# 1. The name of a text file containing the message
# 2. A boolean (either True or False) indicating whether this message corresponds to a goal node. (We need this because, to be valid, a heuristic must always estimate the cost at a goal node to be 0)
# 
# The program should output 0 if this is a goal node. Otherwise, it should count how many times the letters A, E, N, O, S, and T occur in the message and sort them from most common to least common. For example, if T was the most common letter in the message, followed by E, then O, then A, then S, then N, then the sorted string would be TEOASN. Note that, if two letters have the same frequency, you should use alphabetical order to break ties (e.g. A comes before E).
# 
# The program should then compare this sorted string to the theoretical goal (ETAONS) and count how many letters are in the wrong place. For example, all 6 letters are in the wrong place in TEOASN, but only three are wrong for TAEONS. Finally, the output heuristic value should be ceiling(n/2), where n is the number of letters out of place, and the ceiling function rounds up to the nearest integer. Thus we roughly estimate how many swaps we need to make the ordering the same. 

# In[ ]:


from collections import Counter

def task5(file, is_goal):
    if is_goal: return 0
    keys = "ETAONS"
    count = [ch.upper() for line in open(file)
             for ch in line if ch.upper() in keys]
    counter = {key: count.count(key) for key in keys}
    num = 0
    freq = ''.join(sorted(counter, key=(lambda k: (-counter[k], k))))
    for i, j in zip(freq, "ETAONS"):
        num += i != j
    return (num+1)//2

if __name__ == '__main__':
    # Example function calls below, you can add your own to test the task5 function
    print(task5('freq_eg1.txt', False))


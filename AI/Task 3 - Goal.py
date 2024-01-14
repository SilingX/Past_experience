#!/usr/bin/env python
# coding: utf-8

# # Task 3 - Goal
# 
# In this task, you will write a function to check if a given message is valid English, by comparing it to a common English word list. The function should take three inputs:
# 
# 1. The name of a text file containing the message
# 2. The name of a text file containing a list of words, in alphabetical order and each on a separate line, which will act as a dictionary of correct words
# 3. A threshold, t, specifying what percentage of words must be correct for this to count as a goal (given as an integer between 0 and 100). The threshold is important, because we may need a buffer if our dictionary is missing words, or there are some misspelt words in the message.
# 
# The function should return a string containing two lines of text. 
# The first line should be "True" if at least t% of the words in the message are correct according to the dictionary and "False" otherwise. 
# The second line should be the percentage of words that were correct, to 2 decimal places (round off any further decimal places; 0.005 rounds up to 0.01). 

# In[ ]:


def task3(message, dictionary, threshold):
    simplify = lambda string: ''.join(ch for ch in string if ch.isalnum())
    message = [simplify(word) for word in ''.join(list(open(message))).split()]
    dictionary = set(''.join(list(open(dictionary))).split())
    
    num = 0
    for word in message:
        #print(word, dictionary)
        num += 1 if word.lower() in dictionary else 0
    percent = num / len(message) * 100
    return f'{percent >= threshold}\n{percent:.2f}'
        

def btask3(message_filename, dictionary_filename, threshold):
    #TODO
    ans = [True,0.00]
    mraw = list(open(message_filename))
    dicraw = list(open(dictionary_filename))
    dicrem = []
    mrem = []
    for line in mraw:
      mram = line.split()
      for word in mram:
        mrem.append(word.strip("%~?*;:,!.\"").replace("'","").replace("(","").replace(")",""))
    for key in dicraw:
      dicrem.append(key.strip())
    m = len(mrem)
    n = 0
    for word in mrem:
      for key in dicrem:
        if word.lower() == key.lower():
            n = n + 1
            break
    cal = float('%.4f'%(n/m))*100
    ans[1] = ('%.2f'%cal)
    if float(ans[1]) < float(threshold):
      ans[0] = False
    formas = str(ans[0])+'\n'+str(ans[1])
    return formas

if __name__ == '__main__':
    # Example function calls below, you can add your own to test the task3 function
    #print(task3('jingle_bells.txt', 'dict_xmas.txt', 90))
    #print(better_task3('jingle_bells.txt', 'dict_xmas.txt', 90))
    print(task3('fruit_ode.txt', 'dict_fruit.txt', 80))
    #print(task3('amazing_poetry.txt', 'common_words.txt', 95))


#!/usr/bin/env python
# coding: utf-8

# # Task 1 - Secret Messages
# 
# For this task, you will write a function to encode and decode messages using the above letter swapping method (which is the how the secret message in the introduction was encoded). The function should have three parameters:
# 
# 1. A string specifying the key (i.e. the sequence of letter swaps).
#    For example, "AEGHAG", would mean we should apply the swaps A ↔ E, G ↔ H, then A ↔ G if we’re encoding, or the reverse (A ↔ G, G ↔ H, then A ↔ E) if we’re decoding.
#    Note that "AEGHAG" is the same as "EAGHAG", since A ↔ E is the same as E ↔ A.
# 2. The name of a text file containing the message to be encoded or decoded.
# 3. Either 'e' or 'd' indicating whether to encode or decode, respectively.
#
# The function will return the resulting encoded or decoded message as a string, with capitalisation, punctuation and spacing preserved.

# In[ ]:


def task1(key, filename, indicator):
    #TODO
    #print(open(filename))
    orilist = list(open(filename))
    ans = ''
    for x in range(len(orilist)):
      oristr = orilist[x]
      codestr = ''
      if indicator == 'd':
         for n in range(len(oristr)):
            i = len(key)-1
            tempstr = oristr[n]
            upflag = tempstr.isupper()
            while(i>-1):
              if(upflag):
                if tempstr == key[i].upper():
                  if i%2 == 0:
                    tempstr = key[i+1].upper()
                    i = i-1
                  else:
                    tempstr = key[i-1].upper()
                    i = i-2
                  continue
              else:
                if tempstr == key[i].lower():
                  if i%2 == 0:
                    tempstr = key[i+1].lower()
                    i = i-1
                  else:
                    tempstr = key[i-1].lower()
                    i = i-2
                  continue
              i = i-1
            codestr = codestr+tempstr
      if indicator == 'e':
         for n in range(len(oristr)):
            i = 0
            tempstr = oristr[n]
            upflag = tempstr.isupper()
            while(i<len(key)):
              if(upflag):
                if tempstr == key[i].upper():
                  if i%2 == 0:
                    tempstr = key[i+1].upper()
                    i = i+2
                  else:
                    tempstr = key[i-1].upper()
                    i = i+1
                  continue
              else:
                if tempstr == key[i].lower():
                  if i%2 == 0:
                    tempstr = key[i+1].lower()
                    i = i+2
                  else:
                    tempstr = key[i-1].lower()
                    i = i+1
                  continue
              i = i+1
            codestr = codestr+tempstr
      ans = ans + codestr
    return ans

if __name__ == '__main__':
    # Example function calls below, you can add your own to test the task1 function
    print(task1('AE', 'spain.txt', 'd'))
    print(task1('VFSC', 'ai.txt', 'd'))
    print(task1('ABBC', 'cabs.txt', 'd'))
    print(task1('VJ', 'strange_words_plain.txt', 'e')    )


# Letter Count

# Your task is read an input string and count every letter, then output the letter counts in ascending order sorted by the lexical value of the letter, one record per line.

# For example, the string "you are hearing me talk" when passed into the solution method would yield:

# a appears 3 times
# e appears 3 times
# g appears 1 time
# h appears 1 time
# i appears 1 time
# k appears 1 time
# l appears 1 time
# m appears 1 time
# n appears 1 time
# o appears 1 time
# r appears 2 times
# t appears 1 time
# u appears 1 time
# y appears 1 time

# Be sure to correctly account for plurals in the word "time" and both upper case and lower case letters should be counted, however, output should be all lower case.

# Solution should be clean, well structured, and performant code counts!
import re
regex = re.compile(r'\w')
freq = {}

def solution(s):
  for i in s.lower():
    for match in regex.findall(i):
      if match in freq:
        freq[match] += 1
      else:
        freq[match] = 1

  for i in sorted(freq.keys()):
    if freq[i] > 1:
      print(i + ' appears ' + str(freq[i]) + ' times')
    else:
      print(i + ' appears ' + str(freq[i]) + ' time')
  pass

print(solution("I just found this Al Gore doll!"))
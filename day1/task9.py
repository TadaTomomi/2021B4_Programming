import sys
import random
str = ""
for i in range(1, len(sys.argv)):
  word = sys.argv[i]
  if (len(word) > 3):
    str += word[0] + "".join(random.sample(word[1:-1], len(word)-2)) + word[-1] + " "
  else:
    str += word + " "

print(str)
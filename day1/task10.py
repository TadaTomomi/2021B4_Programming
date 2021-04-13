import sys

def n_gram(seq, n):
  gram = []
  for i in range(len(seq)-n+1):
    gram.append(seq[i:i+n])
  return gram

list = sys.argv[1:]
print("単語bi-gram: " + str(n_gram(list, 2)))
print("文字bi-gram: " + str(n_gram("".join(list), 2)))
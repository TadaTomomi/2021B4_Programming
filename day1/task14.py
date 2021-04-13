import numpy as np

docs = [["リンゴ", "リンゴ"], ["リンゴ", "レモン"], ["レモン", "ミカン"]]
terms = ["リンゴ", "レモン", "ミカン"]

def idf(term, docs):
  count =0
  for doc in docs:
    if term in doc:
      count += 1
  return np.log10(len(docs)/count) + 1

#他のファイル実行時に出力されてしまうのでコメントアウト
# for term in terms:
#   print("idf(" + str(term) + ") = " + str(idf(term, docs)))
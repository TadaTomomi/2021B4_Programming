docs = [["リンゴ", "リンゴ"], ["リンゴ", "レモン"], ["レモン", "ミカン"]]
terms = ["リンゴ", "レモン", "ミカン"]

def tf(term, doc):
  count = 0
  for word in doc:
    if word == term:
      count += 1
  return count/len(doc)

#他のファイル実行時に出力されてしまうのでコメントアウト
# for doc in docs:
#   for term in terms:
#     print("tf(" + str(term) + ", " + str(doc) + ") = " + str(tf(term, doc)) + " ", end = "")
#   print("")

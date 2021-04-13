file = open('dataset/data.txt', 'r')
docs = []
words = []
while True:
  data = file.readline().replace("\n", "")
  if data:
    word_list = data.split("と")
    docs.append(word_list)
    for word in word_list:
      words.append(word)
  else:
    break

terms = list(set(words))

#他のファイル実行時に出力されてしまうのでコメントアウト
# print("docs : " + str(docs))
# print("terms: " + str(terms))
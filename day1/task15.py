import numpy as np
import task13
import task14

docs = [["リンゴ", "リンゴ"], ["リンゴ", "レモン"], ["レモン", "ミカン"]]
terms = ["リンゴ", "レモン", "ミカン"]

def tf_idf(terms, docs):
  matrix = np.zeros((len(docs), len(terms)))
  for j in range(len(terms)):
    idf = task14.idf(terms[j], docs)
    for i in range(len(docs)):
      tf = task13.tf(terms[j], docs[i])
      matrix[i][j] = tf * idf
  return matrix

print(tf_idf(terms, docs))

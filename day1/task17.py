import numpy as np
from nlp import task15
from nlp import task16
import task12

docs = task12.docs
terms = task12.terms
matrix = np.zeros((len(docs), len(docs)))

tfidf = task15.tf_idf(terms, docs)

for i in range(tfidf.shape[0]):
  for j in range(tfidf.shape[0]):
    matrix[i][j] = task16.cosine_sim(tfidf[i], tfidf[j])

print(matrix)


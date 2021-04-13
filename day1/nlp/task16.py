import numpy as np

def cosine_sim(x1, x2):
  return np.dot(x1, x2) / (np.linalg.norm(x1) * np.linalg.norm(x2))

x1 = np.array([1, 0, 0, 1])
x2 = np.array([0, 1, 0, 1])

# print(cosine_sim(x1, x2))
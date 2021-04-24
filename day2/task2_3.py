import numpy as np
import task2_2

class SingleLayer():
  def __init__(self, W, b):
    self.W = W
    self.b = b

  def relu(self, x):
    z = np.dot(self.W.T, x) + self.b
    return task2_2.relu(z)


def main():
  x = np.array([1.0, 0.5])
  W = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
  b = np.array([0.1, 0.2, 0.3])
  l = SingleLayer(W, b)
  print(l.relu(x))

if __name__ == "__main__":
  main()
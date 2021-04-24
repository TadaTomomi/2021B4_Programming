import numpy as np
import task2_2

class MLP_3Layer():
  def __init__(self, W1, b1, W2, b2, W3, b3):
    self.W1 = W1
    self.b1 = b1
    self.W2 = W2
    self.b2 = b2
    self.W3 = W3
    self.b3 = b3

  def forward(self, x):
    z1 = np.dot(x, self.W1) + self.b1
    a1 = task2_2.relu(z1)
    z2 = np.dot(a1, self.W2) + self.b2
    a2 = task2_2.relu(z2)
    z3 = np.dot(a2, self.W3) + self.b3
    a3 = task2_2.relu(z3)
    return a3

def main():
  x = np.array([[1.0, 0.5], [-0.3, -0.2], [0.0, 0.8], [0.3, -0.4]])
  W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
  b1 = np.array([0.1, 0.2, 0.3])
  W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
  b2 = np.array([0.1, 0.2])
  W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
  b3 = np.array([0.1, 0.2])
  m = MLP_3Layer(W1, b1, W2, b2, W3, b3)
  print(m.forward(x))

if __name__ == "__main__":
  main()
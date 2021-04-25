import numpy as np
import task2_5

class SoftamaxCrossEntropy():
  def __init__(self):
    self.y = None
    self.t = None
  def forward(self, x, t):
    self.y = task2_5.softmax(x)
    self.t = t
    return -1 * np.sum(self.t * np.log(self.y)) / len(x)
  def backprop(self):
    dx = self.y - self.t
    return dx

def main():
  x = np.array([[1.0, 0.5], [-0.4, 0.1]])
  t = np.array([[1.0, 0.0], [0.0, 1.0]])
  s = SoftamaxCrossEntropy()
  loss = s.forward(x, t)
  print("順伝播出力:")
  print(loss)
  dx = s.backprop()
  print("逆伝播出力:")
  print (dx)

main()
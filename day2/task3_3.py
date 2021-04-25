import numpy as np

class Softmax():
  def __init__(self):
    self.out = None
  def forward(self, x):
    self.out = 1 / (1 + np.exp(-x))
    return self.out
  def backprop(self, dout):
    dx = dout * self.out * (1 - self.out)
    return dx

def main():
  x = np.array([-0.5, 0.0, 1.0, 2.0])
  softmax = Softmax()
  y = softmax.forward(x)
  print("順伝播出力: ", y)
  dy = np.array([1.0, 1.0, 1.0, 1.0])
  dx = softmax.backprop(dy)
  print("逆伝播出力: ", dx)

main()

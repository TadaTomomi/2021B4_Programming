import numpy as np

class ReLU():
  def __init__(self):
    self.mask = None
  def forward(self, x):
    self.mask = (x <= 0)
    out = x.copy()
    out[self.mask] = 0 
    return out
  def backprop(self, dout):
    dout[self.mask] = 0
    dx = dout
    return dx

def main():
  x = np.array([-0.5, 0.0, 1.0, 2.0])
  relu = ReLU()
  y = relu.forward(x)
  print("順伝播出力: ", y)
  dy = np.array([1.0, 1.0, 1.0, 1.0])
  dx = relu.backprop(dy)
  print("逆伝播出力: ", dx)

main()
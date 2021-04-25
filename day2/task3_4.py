import numpy as np

class Affine():
  def __init__(self, W, b):
    self.W = W
    self.b = b
    self.x = None
  def forward(self, x):
    self.x = x
    out = np.dot(self.x, self.W) + self.b
    return out
  def backprop(self, dout):
    dx = np.dot(dout, self.W.T)
    dW = np.dot(self.x.T, dout)
    db = np.sum(dout, axis=0)
    return dx, dW, db

def main():
  x = np.array([[1.0, 0.5], [-0.4, 0.1]])
  W = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
  b = np.array([0.1, 0.2, 0.3])
  affine = Affine(W, b)
  z = affine.forward(x)
  print("順伝播出力:")
  print(z)
  dz = np.ones((z.shape))
  dx, dW, db = affine.backprop(dz)
  print("逆伝播出力dx:")
  print (dx)
  print("逆伝播出力dW:")
  print (dW)
  print("逆伝播出力db:")
  print (db)

main()
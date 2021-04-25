class Multiply():
  def __init__(self):
    self.x = None
    self.y = None
  def forward(self, x, y):
    self.x = x
    self.y = y
    z = x * y
    return z
  def backprop(self, dz):
    dx = dz * self.y
    dy = dz * self.x
    return dx, dy

class Add():
  def __init__(self):
    self.x = None
    self.y = None
  def forward(self, x, y):
    self.x = x
    self.y = y
    z = x + y
    return z
  def backprop(self, dz):
    dx = dz
    dy = dz
    return dx, dy

def main():
  a, b, c = 2, 3, 4
  add = Add()
  mul = Multiply()
  f1 = add.forward(a, b)
  f2 = mul.forward(f1, c)
  print("順伝播出力: %d" % f2)
  dz = 1
  # da, db = 1, 1
  dab, dc = mul.backprop(dz)
  da, db = add.backprop(dab)
  print("逆伝播出力 da: %d, db: %d, dc: %d" % (da, db, dc))

main()
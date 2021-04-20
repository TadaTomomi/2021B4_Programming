import task1_2

def xor(x1, x2):
  p_nand = task1_2.p_nand
  t1 = p_nand.forward(x1, x2)
  t2 = p_nand.forward(x1, t1)
  t3 = p_nand.forward(t1, x2)
  t4 = p_nand.forward(t2, t3)
  return t4

x1_list = [1, 1, 0, 0]
x2_list = [1, 0, 1, 0]

for i in range(4):
  x1 = x1_list[i]
  x2 = x2_list[i]
  print("XOR(" + str(x1) + ", " + str(x2) +") = " + str(xor(x1, x2)))
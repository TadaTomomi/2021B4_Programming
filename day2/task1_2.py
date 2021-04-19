import task1_1

p_and = task1_1.Perceptron(0.5, 0.5, 0.7)
p_nand = task1_1.Perceptron(-0.5, -0.7, -0.7)
p_or = task1_1.Perceptron(0.7, 0.7, 0.5)

x1_list = [1, 1, 0, 0]
x2_list = [1, 0, 1, 0]

for i in range(4):
  x1 = x1_list[i]
  x2 = x2_list[i]
  print("AND(" + str(x1) + ", " + str(x2) +") = " + str(p_and.forward(x1, x2)) + "  ", end="coding")
  print("AND(" + str(x1) + ", " + str(x2) +") = " + str(p_nand.forward(x1, x2)) + "  ", end="coding")
  print("AND(" + str(x1) + ", " + str(x2) +") = " + str(p_or.forward(x1, x2)))

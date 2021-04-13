file = open('dataset/data.txt', 'r')
while True:
  data = file.readline()
  if data:
    print(data, end="")
  else:
    break
file.close()
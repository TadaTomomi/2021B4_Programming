str = "Hi He Lead Because Boron Could Not Oxidize Flourine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
list = str.replace(".", "").split()
dic = {}
for i in range(len(list)):
  idx = i + 1
  if idx in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
    dic[list[i][0:1]] = idx
  else:
    dic[list[i][0:2]] = idx
print(dic)
str = "Hi He Lead Because Boron Could Not Oxidize Flourine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
list = str.replace(".", "").split()
dic = {}
for i in range(1, len(list)+1):
  if i in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
    dic[list[i-1][0:1]] = i
  else:
    dic[list[i-1][0:2]] = i
print(dic)
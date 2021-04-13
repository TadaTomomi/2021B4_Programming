str="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
str_list=str.replace(",", "").replace(".", "").split()
list = []
for s in str_list:
  list.append(len(s))
print(list)
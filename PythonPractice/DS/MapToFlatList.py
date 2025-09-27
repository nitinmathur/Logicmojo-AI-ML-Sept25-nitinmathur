map1 = {"Mobile": {"Redmi", "Samsung", "Realme"}, "Laptop": {"Dell", "HP"}, "TV": {"Sony", "LG"}}
lst = []

for entry in map1.items():
    key = entry[0]
    for val in entry[1]:
      lst.append(key+"_"+val)
  
print(lst)

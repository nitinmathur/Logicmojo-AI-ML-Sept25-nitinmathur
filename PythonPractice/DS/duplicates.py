def dedupElements(lst):
  st = set(lst)
  return list(st)

sin = input("insert list to dedup")
lst = list(map(int, sin.split(' ')))
dlst = dedupElements(lst)
print(dlst)

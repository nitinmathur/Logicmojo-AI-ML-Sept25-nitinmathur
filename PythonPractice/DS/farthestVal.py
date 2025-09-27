sin = input("entry list elements with spaces ")
lst = list(map(int, sin.split(' ')))

mp = {}
result = {}

index = 0;
for val in lst:
  if(val in mp):
    diff = index - mp.get(val)
    if(val in result and diff > result.get(val)):
      result.update({val: diff})
  else:
    mp.update({val: index})
    result.update({val: 0})
  index +=1

# print(mp)
print(max(result.values()))

stack = []
str = input("enter expression to check for correct brackets ")
for char in str:
  if (char == '{' or char == '}' or char == '[' or char == ']' or char == '(' or char == ')'):
    if (char == '{' or char == '[' or char == '('):
      stack.append(char)
    else:
      if(len(stack) == 0):
         stack.append(char)
         break
      elif(stack[-1] == '{' and char == '}'):
        stack.pop()
      elif (stack[-1] == '[' and char == ']'):
        stack.pop()
      elif (stack[-1] == '(' and char == ')'):
        stack.pop()
      else:
        break

if (len(stack) == 0):
  print("balanced")
else:
  print("unbalanced")

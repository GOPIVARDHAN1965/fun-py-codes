s=input()
n=int(input())
x=""
l=[]
for i in range(len(s)):
  if i%n==0 and i>0:
    l.append(x)
    x=""
  if i==len(s)-1:
    x=x+s[i]
    l.append(x)
  x=x+s[i]
m=[]
x=""
for i in range(len(l)):
  if i>0:
    m.append(x)
    x=""
  for j in range(len(l[i])):
    if l[i][j] not in x:
      x=x+l[i][j]
      continue
  if i==len(l)-1:
    m.append(x)
    break
# print(m)
for i in m:
  print(i)
  

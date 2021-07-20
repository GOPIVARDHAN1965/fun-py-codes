a=input("Enter name 1")
b=input("Enter name 2")
x=sorted(a)
y=sorted(b)
n=0
for i in x:
  for j in y:
    if i.lower()==j.lower():
      n=n+1
      y.remove(j)
      break
s=len(x)+len(y)-n
l=["F","L","A","M","E","S"]
for i in range(0,s):
  n=[]
  if  len(l)==1:
      break
  j=s%len(l)
  for i in range(j,len(l)):
      n.append(l[i])
  for i in range(j):
      n.append(l[i])
  l=n
  l.pop()
if(l[0]=="F"):
  print("Friends")
elif(l[0]=="L"):
  print("Lover")
elif(l[0]=="A"):
  print("Affectionate")
elif(l[0]=="M"):
  print("Marriage")
elif(l[0]=="E"):
  print("Enemies")
else:
  print("Sisters")

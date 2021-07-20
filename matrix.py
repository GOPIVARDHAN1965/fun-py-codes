#matrix decoded
f=input().split()
f[0]=int(f[0])
f[1]=int(f[1])
ma=[]
for i in range(f[0]):
    ma.append(input())
y=""
for i in range(f[1]):
  for j in range(f[0]):
    l=str(ma[j])
    y=y+l[i]
s=["!","@","#","$","%","&"," "]
j=0
z=""
i=0
b=0
while j!=len(y):
  k=0
  while y[j] in s and j<len(y)-1 and j>1 and y[j-1] not in s:
    l=j
    while y[l] in s and l<len(y) and j<len(y):
      k+=1
      while l!=len(y)-1:
          l+=1
          break
      j+=1
    print(k)
    j=j-1
    while k>=1 and j<len(y)-1:
      z=z+" "
      j=j+1
      break
    break
  b=b+k
  while j!=len(y)-1:
      z=z+y[j]
      break
  j=j+1
  i+=1
print(z)
f=(i-1)+(b-k)
while f!=len(y):
    z=z+y[f]
    f+=1
print(z)

#test cases:
#y="This$#is% Matrix#  %!"
#y="#It#%%is$Matrix%%$script$Trinity"
#y="#  @"
#y="#It#%%is$Matrix%%$script"
#y="This%%is$Matrix%%$script"
#y="This%%isMatrix#scrpt&%!&"
#y="#  @i##U"

import math

c=int(input())
a=int(input())
b=(math.sqrt(a**2+c**2))/2
d=(math.asin(b/a))*180/3.14
print("{0:.0f}".format(d),end=u"\N{DEGREE SIGN}")

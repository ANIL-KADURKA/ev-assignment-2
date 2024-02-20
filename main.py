from addition import add

from divide import divide
from multiplication import mul

print("This is Main File")

a=int(input())
b=int(input())

x=add(a,b)
print(x)


y=divide(x)
print(y)


h=int(input())
z=mul(y,h)
print(z)

"""class O:

    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

o = O(1,2,3)
obj = ["a","b","c"]
for i  in obj:
    print(getattr(o, i))

for i  in  obj:
    setattr(o, i, (getattr(o, i) + 1))

for  i in obj:
    print(getattr(o,i))

o.a = 2
o.b = 3
o.c = 4"""

v = 1
a = 1
s = 1

print((v-(((v**2)-(2*a*s))**(1/2)))/a)

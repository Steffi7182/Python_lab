print("Area of rectangle")
l=int(input("length"))
b=int(input("breadth"))
c=lambda x,y:x*y
print("Area of rectangle:"+str(c(l,b)))
print("Area of square")
s=int(input("side of square"))
c=lambda x:x*x
print("Area of square:"+str(c(s)))
print("Area of triangle")
l=int(input("base"))
b=int(input("height"))
c=lambda x,y:x*y/2
print("Area of triangle:" +str(c(l,b)))

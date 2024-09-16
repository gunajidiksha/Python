def swap(a,b):
    c=a
    a=b
    b=c
    return a,b
x=int(input("Enter side x : "))
y=int(input("Enter side y : "))
print("After swaping: ",swap(x,y))
def quadratic_equation(a,b):
    d=(b*b)-(4*a*c)
    if d>0:
        print((-b+(d)**0.5)/(2*a))
        print((-b-(d)**0.5)/(2*a))
    elif d==0:
        print(-b/(2*a))
    else : 
        real_part = -b/(2*a)
        img_part = ((abs(d))**0.5)/(2*a)
        print(f"{real_part}+{img_part}i") 
        print(f"{real_part}-{img_part}i")

a = int(input("Enter value of a : "))
b = int(input("Enter value of b : "))
c = int(input("Enter value of c : "))

print("roots are : ",quadratic_equation(a,b))






def fibonacci(n):
    count=0
    n1=0
    n2=1
    
    if n<0:
        return "invalid"
    elif n==1:
        return "0"
    else :
        while count<=n :
            print(n1)
            nth=n1+n2
            n1=n2
            n2=nth
            count += 1
num = int(input("Enter a number : "))
print("fibonacci : ",fibonacci(num))
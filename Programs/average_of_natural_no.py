def calculate_average(n):
    total = 0
    for i in range(1,n+1):
        total+=i
    average = total/n
    return average

n = int(input("Enter a value for n: "))
average_result = calculate_average(n)
print(f"The average of the first {n} natural numbers is {average_result}")
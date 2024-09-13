principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest(in % per annumn): "))
time = float(input("Enter the duration in years: "))

simple_interest = (principal*rate*time)/100

compound_interest = principal*((1+rate/100)**time)-1

print("Principal amount " , principal)
print("Rate of interest " , rate)
print("Time in years " , time)
print("Simple interest " , simple_interest)
print("Compound interest " , compound_interest)
weight = float(input("Enter your weight : "))
unit = input("Enter (L)lbs or (K)kg : ")

if unit.upper() == 'L':
    result = weight * 0.45
    print(f"You are  {result} pounds. ")
elif unit.upper() == 'K':
    result = weight / 0.45
    print(f"You are {result} pounds . ")
else:
    print("Enter (L) for lbs or (K) for kg . ")
num1 = float(int("Enter the first number: "))
num2 = float(int("Enter the second number: "))

a = num1 + num2
s = num1 - num2
m = num1*num2

if num2 != 0:
    d = num1/num2
else:
    d = "Undefined"

print("\nAddition: ", a)
print("\nSubtraction: ", s)
print("\nMultiplication: ", m)
print("\nDivision: ", d)
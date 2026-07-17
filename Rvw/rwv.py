num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))

suma = num_1 + num_2
resta = num_1 - num_2
multiplicacion = num_1 * num_2
division = num_1 / num_2 if num_2 != 0 else "undefined (cannot divide by zero)"

print(f"The sum of {num_1} and {num_2} is: {suma}")
print(f"The difference of {num_1} and {num_2} is: {resta}")
print(f"The product of {num_1} and {num_2} is: {multiplicacion}")
print(f"The quotient of {num_1} and {num_2} is: {division}")
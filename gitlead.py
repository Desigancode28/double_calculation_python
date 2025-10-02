#this is first coding to github intro
a = 33
b = 28
valued_0 = input("Enter the operation you want: ")
valued_1 = input("Enter the second operation you want: ")
def calculator(valued, a, b):
    if valued == "addition":
        print(a + b)
    elif valued == "subtraction":
        print(a - b)
    elif valued == "multiplication":
        print(a * b)
    elif valued == "division":
        print(a / b)
    elif valued == "floor division":
        print(a // b)
    elif valued == "modulus":
        print(a % b)
    else:
        print("error operation")
# new project for double calculation
print("Enter first operation")
calculator(valued_0, a, b)
print("Enter the second operation")
calculator(valued_1, a, b)

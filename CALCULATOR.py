# A simple calculator program in PYTHON
# We will do it with the help of if...elif...else statements
# It won't have GUI


# Asking for which operation to do
print("Which operation do you want to perform:")
print()
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exponentiation")
print()
print("Enter the serial number given in front of the Operation's name")
print()
operation = int(input("Enter the operation's serial number: "))

# If the user wants to do addition
if operation == 1:
    num_1_to_add = int(input("Enter First Number To Be Added: "))
    num_2_to_add = int(input("Enter Second Number To Be Added: "))
    add_ans = int(num_1_to_add) + int(num_2_to_add)
    print()
    print("The Answer To The Addition of", num_1_to_add, "and", num_2_to_add, "is", add_ans)


# If the user wants to do subtraction
elif operation == 2:
    num_1_to_sub = int(input("Enter First Number To Be Subtracted: "))
    num_2_to_sub = int(input("Enter Second Number To Be Subtracted: "))
    sub_ans = int(num_1_to_sub) - int(num_2_to_sub)
    print()
    print("The Answer To The Subtraction of", num_1_to_sub, "and", num_2_to_sub, "is", sub_ans)


# If the user wants to do Multiplication
elif operation == 3:
    num_1_to_multiply = int(input("Enter First Number To Be Multiplied: "))
    num_2_to_multiply = int(input("Enter Second Number To Be Multiplied: "))
    multiplication_ans = int(num_1_to_multiply) * int(num_2_to_multiply)
    print()
    print("The Answer To The Multiplication of", num_1_to_multiply, "and", num_2_to_multiply, "is", multiplication_ans)



# If the user wants to do Division
elif operation == 4:
    num_1_to_div = int(input("Enter First Number To Be Divided: "))
    num_2_to_div = int(input("Enter Second Number To Be Divided: "))
    div_ans = int(num_1_to_div) / int(num_2_to_div)
    print()
    print("The Answer To The Division of", num_1_to_div, "and", num_2_to_div, "is", div_ans)


# If the user wants find out exponent
else:
    num_1_to_exp = int(input("Enter First Number To Be Exponentiated: "))
    num_2_to_exp = int(input("Enter Second Number To Be Exponentiated: "))
    exp_ans = int(num_1_to_exp) ** int(num_2_to_exp)
    print()
    print(num_1_to_exp, "Raised to the power", num_2_to_exp, "is,", exp_ans)
print()
print()
print("Thanks for Using :)")

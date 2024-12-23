# Get the operator and inputs from the user
operator = input("Please select (+,-,*,/,%) : ")
input1 = float(input("Number 1: "))
input2 = float(input("Number 2: "))

# Perform the operation based on the operator
if operator == '+':
    result = input1 + input2
elif operator == '-':
    result = input1 - input2
elif operator == '*':
    result = input1 * input2
elif operator == '/':
    if input2 != 0:
        result = input1 / input2
    else:
        result = "Error: Division by zero"
elif operator == '%':
    if input2 != 0:
        result = input1 % input2
    else:
        result = "Error: Division by zero"
else:
    result = "Invalid operator"

# Print the result
print("Result:", result)

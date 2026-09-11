def find_the_largest_details(num1, num2, num3):
    # Track the value and variable name of the largest number
    if num1 >= num2:
        if num1 >= num3:
            largest_val = num1
            var_name = "num1"
        else:
            largest_val = num3
            var_name = "num3"
    else:
        if num2 >= num3:
            largest_val = num2
            var_name = "num2"
        else:
            largest_val = num3
            var_name = "num3"
    # Constructthe formatted detailed message
    message = (
        f"Message to User: You entered three numbers, {num1}, {num2}, {num3}. "
        f"The first whole number you entered was assigned to a variable  named num1, "
        f"The second to ({num2}) to num2, and finally the third ({num3}) was assigned to num3. "
        f"which belonged to an integer variable named {var_name}."
    )
    return message

# User input prompt
num1 = int(input("Enter first integer (num1): "))
num2 = int(input("Enter second integer (num2): "))
num3 = int(input("Enter third integer (num3): "))


# Execute function and print output
output_message = find_the_largest_details(num1, num2, num3)
print("\n" + output_message)
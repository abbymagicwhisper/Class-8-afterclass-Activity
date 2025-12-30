num1 = 14
num2 = 12
num3 = 17
print("The equation is \"14 + 12 - 17\"\n14 is number1, 12 is number2 and 17 is number3")
print("First number is ",num1,"\nSecond number  is ",num2,"\nThird number is",num3)
nums_swap1 = int(input("Enter the first number that needs to be swapped: "))
nums_swap2 = int(input("Enter the second number that needs to be swapped: "))
nums_swap3 = int(input("Enter the third number that needs to be swapped: "))

if nums_swap1 == 14 and nums_swap2 == 12 and nums_swap3 == 17:
    print("The correct answer is ", 14 + 12 - 17 )
elif nums_swap1 == 14 and nums_swap2 == 17 and nums_swap3 == 12:
    print("The correct answer is ", 14 + 17 - 12 )
elif nums_swap1 == 12 and nums_swap2 == 17 and nums_swap3 == 14:
    print("The correct answer is ", 12 + 17 - 14 )
elif nums_swap1 == 12 and nums_swap2 == 14 and nums_swap3 == 17:
    print("The correct answer is ", 12 + 14 - 17 )
elif nums_swap1 == 17 and nums_swap2 == 12 and nums_swap3 == 14:
    print("The correct answer is ", 17 + 12 - 14 )
elif nums_swap1 == 17 and nums_swap2 == 14 and nums_swap3 == 17:
    print("The correct answer is ", 17 + 14 - 17 )
else:
    print("Ahh! An unexpected error has occured")
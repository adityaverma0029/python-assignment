#Q4. Write a Python program that takes an integer input from the user and prints whether the number is positive, negative, or zero. 

number = int(input("Enter any value : \n"))

if (number >= 0):
    if number == 0:
        print('Number is 0')
    else:
        print('Number is positive')
else:
    print('Number is negative')
import calculator

while True:
    menu = print('1. Addition\n 2. Subtraction\n 3. Multiplication\n 4. Division\n 5. Exit\n')
    menu_input = int(input('Enter corresponding operation number: '))
    

    if menu_input == 1:
        try:
            num1 = int(input('Enter 1st number: '))
            num2 = int(input('Enter 2nd number: '))
            result = calculator.add(num1, num2)
            print(result)
        except ValueError:
            print('Error: Enter only numbers \n')

    elif menu_input == 2:
        try:
            num1 = int(input('Enter 1st number: '))
            num2 = int(input('Enter 2nd number: '))
            result = calculator.subtract(num1, num2)
            print(result)
        except ValueError:
            print('Error: Enter only numbers \n')

    elif menu_input == 3:
        try:
            num1 = int(input('Enter 1st number: '))
            num2 = int(input('Enter 2nd number: '))
            result = calculator.multiply(num1, num2)
            print(result)
        except ValueError:
            print('Error: Enter only numbers \n')

    elif menu_input == 4:
        try:
            num1 = int(input('Enter 1st number: '))
            num2 = int(input('Enter 2nd number: '))
            result = calculator.divide(num1, num2)
            print(result)
        except ValueError:
            print('Error: Enter only numbers \n')
        except ZeroDivisionError:
            print('Zero division not possible')
        
    elif menu_input == 5:
        break

    else:
        print('Enter a valid option')
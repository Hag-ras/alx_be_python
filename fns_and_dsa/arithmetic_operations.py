def perform_operation(num1, num2, operation):
    match operation:
        case 'add':
            print('The result is ', num1 + num2)
        case 'subtract':
            print('The result is ', num1 - num2)
        case 'multiply':
            print('The result is ', num1 * num2)
        case 'divide':
            if num2==0:
                print('Cannot divide by zero.')
            else:
                print('The result is ', num1 / num2)
        case _:
            print('Invalid Operation')
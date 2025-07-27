def perform_operation(num1, num2, operation):
    match operation:
        case 'add':
            return 'The result is ' + num1 + num2
        case 'subtract':
            return 'The result is '+ num1 - num2
        case 'multiply':
            return 'The result is '+ num1 * num2
        case 'divide':
            if num2 == 0:
                return 'Cannot divide by zero.'
            else:
                return 'The result is '+  num1 / num2
        case _:
            return 'Invalid Operation'
def perform_operation(num1, num2, operation):
        if operation == 'add':
            return 'The result is ' + num1 + num2
        elif operation == 'subtract':
            return 'The result is '+ num1 - num2
        elif operation =='multiply':
            return 'The result is '+ num1 * num2
        elif operation =='divide':
            if num2 == 0:
                return 'Cannot divide by zero.'
            else:
                return 'The result is '+  num1 / num2
        else:
            return 'Invalid Operation'
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit -32) * FAHRENHEIT_TO_CELSIUS_FACTOR 
def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR +32

try:
    temp = int(input('Enter the temperature to convert: '))
except:
    raise ValueError("Invalid temperature. Please enter a numeric value.")
type_of_temp = input('Is this temperature in Celsius or Fahrenheit? (C/F): ')

if type_of_temp == 'F' or type_of_temp == 'f' :
    print(f'{temp} °F is {convert_to_celsius(temp)} °C')
elif type_of_temp == 'C' or type_of_temp == 'c' :
    print(f'{temp} °C is {convert_to_fahrenheit(temp)} °F')
else: 
    print('invalid input')

FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    try:
        temp_input = float(input("Enter the temperature to convert: "))
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == 'F':
        celsius = convert_to_celsius(temp_input)
        print(f"{temp_input:.1f}°F is {celsius}°C")
    elif unit == 'C':
        fahrenheit = convert_to_fahrenheit(temp_input)
        print(f"{temp_input:.1f}°C is {fahrenheit}°F")
    else:
        print("Invalid temperature unit. Please enter 'C' or 'F'.")

if __name__ == "__main__":
    main()

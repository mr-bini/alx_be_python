# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9  # Conversion factor from Fahrenheit to Celsius
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5   # Conversion factor from Celsius to Fahrenheit

def check_conversion_factors():
    """Check if global conversion factors are defined correctly."""
    assert FAHRENHEIT_TO_CELSIUS_FACTOR == 5 / 9, "Fahrenheit to Celsius factor is incorrect."
    assert CELSIUS_TO_FAHRENHEIT_FACTOR == 9 / 5, "Celsius to Fahrenheit factor is incorrect."
    print("Global conversion factors are defined correctly.")

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global conversion factor."""
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global conversion factor."""
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    check_conversion_factors()  # Check the conversion factors
    try:
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
        elif unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()

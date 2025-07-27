# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9  # Conversion factor from Fahrenheit to Celsius
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5   # Conversion factor from Celsius to Fahrenheit

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global conversion factor."""
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global conversion factor."""
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    print("\nTemperature Conversion Tool")
    print("--------------------------")
    
    while True:
        try:
            # Get temperature input
            temp_input = input("Enter temperature (q to quit): ").strip()
            if temp_input.lower() == 'q':
                print("Goodbye!")
                break
                
            temperature = float(temp_input)  # Convert input to float
            
            # Get unit and validate
            while True:
                unit = input("Is this in (C)elsius or (F)ahrenheit? [C/F]: ").strip().upper()
                if unit in ['C', 'F']:
                    break
                print("Invalid unit. Please enter 'C' or 'F'.")
            
            # Perform conversion
            if unit == 'C':
                converted = convert_to_fahrenheit(temperature)
                print(f"\n{temperature}°C = {converted:.2f}°F\n")
            else:
                converted = convert_to_celsius(temperature)
                print(f"\n{temperature}°F = {converted:.2f}°C\n")
                
        except ValueError:
            print("Error: Please enter a valid number for temperature.")  # Handle ValueError

if __name__ == "__main__":
    main()

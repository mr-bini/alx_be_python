# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9  # 0.555...
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5   # 1.8

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
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
                
            temperature = float(temp_input)
            
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
            print("Error: Please enter a valid number for temperature.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

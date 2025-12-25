def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9
def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin."""
    return celsius + 273.15 
def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius."""
    return kelvin - 273.15
def fahrenheit_to_kelvin(fahrenheit):
    """Convert Fahrenheit to Kelvin."""
    return (fahrenheit - 32) * 5/9 + 273.15 
def kelvin_to_fahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit."""
    return (kelvin - 273.15) * 9/5 + 32

def display_units():
    print("Units:")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")

def main():
    while True:
        print("\nTemperature Converter")
        display_units()

        # Get source unit
        from_unit = input("Convert from (1/2/3) or 'q' to quit: ")
        if from_unit.lower() == 'q':
            print("Exiting Temperature Converter. Goodbye!")
            break
        if from_unit not in ('1', '2', '3'):
            print("Invalid input. Please enter 1, 2, 3, or q.")
            continue

        # Get target unit
        to_unit = input("Convert to (1/2/3): ")
        if to_unit not in ('1', '2', '3'):
            print("Invalid input. Please enter 1, 2, or 3.")
            continue

        # Get temperature value
        try:
            temp = float(input("Enter temperature value: "))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
            continue

        # Perform conversion
        result = None
        if from_unit == '1':  # Celsius
            if to_unit == '2':
                result = celsius_to_fahrenheit(temp)
            elif to_unit == '3':
                result = celsius_to_kelvin(temp)
            else:
                result = temp  # Celsius to Celsius
        elif from_unit == '2':  # Fahrenheit
            if to_unit == '1':
                result = fahrenheit_to_celsius(temp)
            elif to_unit == '3':
                result = fahrenheit_to_kelvin(temp)
            else:
                result = temp  # Fahrenheit to Fahrenheit
        elif from_unit == '3':  # Kelvin
            if to_unit == '1':
                result = kelvin_to_celsius(temp)
            elif to_unit == '2':
                result = kelvin_to_fahrenheit(temp)
            else:
                result = temp  # Kelvin to Kelvin

        print(f"Converted temperature: {result:.2f}")

if __name__ == "__main__":
    main()
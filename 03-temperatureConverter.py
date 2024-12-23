# Get the temperature and the unit from the user
unit = input("Is the temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
temperature = float(input("Enter the temperature: "))

# Convert the temperature based on the unit
if unit == 'C':
    # Convert Celsius to Fahrenheit
    converted_temperature = (temperature * 9/5) + 32
    print(f"{temperature}°C is equal to {converted_temperature:.2f}°F.")
elif unit == 'F':
    # Convert Fahrenheit to Celsius
    converted_temperature = (temperature - 32) * 5/9
    print(f"{temperature}°F is equal to {converted_temperature:.2f}°C.")
else:
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

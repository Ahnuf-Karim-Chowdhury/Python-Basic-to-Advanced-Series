# Get the weight and the unit from the user
weight = float(input("Enter Weight: "))
unit = input("Kilograms or Pounds? (K/L): ").strip().upper()

# Convert the weight based on the unit
if unit == 'K':
    # Convert kilograms to pounds
    converted_weight = weight * 2.20462
    print(f"{weight} kilograms is equal to {converted_weight:.2f} pounds.")
elif unit == 'L':
    # Convert pounds to kilograms
    converted_weight = weight / 2.20462
    print(f"{weight} pounds is equal to {converted_weight:.2f} kilograms.")
else:
    print("Invalid unit. Please enter 'K' for Kilograms or 'L' for Pounds.")

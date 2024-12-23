def takingInput( i: int, name: str) :
    while i <= 0:
        try:
            temp = float(input(f"Enter {name} : "))
            if temp <= 0:
                print(f"{name} cannot be less than or equal to zero.")
            else:
                return temp
        except ValueError:
            print(f"Invalid input. Please enter a positive number for {name}.")

# Initialize variables
principle = 0
rate = 0
time = 0

principle = takingInput(0, "Principle")
rate = takingInput(0,"Rate")
time= takingInput(0,"Time")

total = principle * pow ((1 + rate/100),time)

print(f"Balance after {time} years : ${total:.2f}")


def divide_time_equally(hours, minutes, divisor):
    # Convert total time into minutes
    total_minutes = hours * 60 + minutes
    
    # Divide the total minutes by the divisor
    minutes_per_person = total_minutes // divisor
    remaining_minutes = total_minutes % divisor
    
    # Convert the result back to hours and minutes
    hours_per_person = minutes_per_person // 60
    minutes_per_person = minutes_per_person % 60
    
    return hours_per_person, minutes_per_person

def main():
    # Get input from user
    hours = int(input("Enter total hours: "))
    minutes = int(input("Enter total minutes: "))
    divisor = int(input("Enter the number of people (divisor): "))
    
    # Ensure divisor is greater than 0
    if divisor <= 0:
        print("Divisor must be greater than 0.")
        return
    
    # Calculate evenly distributed time
    hours_per_person, minutes_per_person = divide_time_equally(hours, minutes, divisor)
    
    # Display the result
    print(f"Each person gets {hours_per_person} hours and {minutes_per_person} minutes.")

if __name__ == "__main__":
    main()

def luhn_algorithm(card_number):
    # Step 1: Reverse the credit card number
    card_number = card_number[::-1]
    
    total_sum = 0
    for i, digit in enumerate(card_number):
        n = int(digit)
        
        # Step 2: Double every second digit
        if i % 2 == 1:
            n *= 2
            # If the doubled number is greater than 9, subtract 9
            if n > 9:
                n -= 9
        
        # Step 3: Sum all the digits
        total_sum += n
    
    # Step 4: If total_sum is divisible by 10, the card is valid
    return total_sum % 10 == 0

def validate_card_type(card_number):
    if len(card_number) == 15 and card_number[:2] in ['34', '37']:
        return "AMEX"
    elif len(card_number) == 16 and 51 <= int(card_number[:2]) <= 55:
        return "MASTERCARD"
    elif len(card_number) in [13, 16] and card_number[0] == '4':
        return "VISA"
    else:
        return "INVALID"

def credit_card_validator(card_number):
    if not card_number.isdigit():
        return "INVALID"
    
    card_type = validate_card_type(card_number)
    if card_type == "INVALID":
        return card_type
    
    # Validate using Luhn's Algorithm
    if luhn_algorithm(card_number):
        return card_type
    else:
        return "INVALID"

# Main code
def main():
    card_number = input("Enter your credit card number: ").strip()
    result = credit_card_validator(card_number)
    print(result)


main()

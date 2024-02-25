import random

def generate_random_numbers(powerball=False):
    # Generate 5 random numbers between 1 and 69
    main_numbers = [random.randint(1, 69) for _ in range(5)]
    
    # Add one more random number between 1 and 26 if powerball is True
    powerball_number = random.randint(1, 26) if powerball else None
    
    return main_numbers, powerball_number

if __name__ == "__main__":
    # Ask the user whether they want Powerball numbers
    want_powerball = input("Do you want Powerball numbers? (yes/no): ").lower()
    
    # Check the user's input
    if want_powerball == "yes":
        # Generate a list of 5 main numbers and one powerball number
        main_numbers, powerball_number = generate_random_numbers(powerball=True)
        # Format and print the generated numbers
        formatted_numbers = "  ".join(map(str, main_numbers)) + "    " + str(powerball_number)
        print("Generated random numbers:", formatted_numbers)
    elif want_powerball == "no":
        # If the user says "no," don't generate any numbers
        print("No numbers generated. Have a great day!")
    else:
        # Handle invalid input
        print("Invalid input. Please enter 'yes' or 'no'.")

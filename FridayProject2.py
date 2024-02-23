import random

def generate_random_numbers(powerball=False):
    # Generate 5 random numbers between 1 and 69
    random_numbers = [random.randint(1, 69) for _ in range(5)]
    
    # Add one more random number between 1 and 26 if powerball is True
    if powerball:
        random_numbers.append(random.randint(1, 26))
    
    return random_numbers

if __name__ == "__main__":
    # Ask the user whether they want Powerball numbers
    want_powerball = input("Do you want Powerball numbers? (yes/no): ").lower()
    
    # Check the user's input
    if want_powerball == "yes":
        # Generate a list of 6 random numbers, including the last one between 1 and 26
        random_numbers = generate_random_numbers(powerball=True)
        print("Generated random numbers:", random_numbers)
    elif want_powerball == "no":
        # If the user says "no," don't generate any numbers
        print("No numbers generated. Have a great day!")
    else:
        # Handle invalid input
        print("Invalid input. Please enter 'yes' or 'no'.")

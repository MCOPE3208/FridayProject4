# Display initial instruction
print("Answer the prompt below, then hit enter, and a new prompt will appear. After you answer all prompts, a story will appear.")

# Prompt user for input and store in variables
adjective = input("Enter an adjective: ")
large_objects = input("Enter large objects (plural): ")
body_part = input("Enter a body part: ")
restaurant = input("Enter a restaurant: ")
food1 = input("Enter a food: ")
food2 = input("Enter another food: ")
large_object = input("Enter a large object: ")

# Display the completed madlib story
print("\nYour Madlib:")
print(f"I've had a very {adjective} day. This morning, I dropped a box of {large_objects} on my {body_part}. "
      f"Then, at lunch, I went to {restaurant} for their delicious {food1}. But the waiter brought me {food2}, "
      f"which I was not hungry for. Finally, on my way home, I was cut off by a van with a large {large_object} strapped to the roof.")

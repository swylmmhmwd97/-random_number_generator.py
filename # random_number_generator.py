# random_number_generator.py

import random

def generate_random_number(lower, upper):
    return random.randint(lower, upper)

# Example usage
print(generate_random_number(1, 100)) # Output: 46

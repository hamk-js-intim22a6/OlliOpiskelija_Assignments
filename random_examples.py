import random

# Example 1: Generating a random integer between 1 and 10
random_integer = random.randint(1, 10)
print(f"Random integer between 1 and 10: {random_integer}")

# Example 2: Generating a random float between 0 and 1
random_float = random.random()
print(f"Random float between 0 and 1: {random_float}")

# Example 3: Choosing a random element from a list
choices = ['apple', 'banana', 'cherry']
random_choice = random.choice(choices)
print(f"Random choice from list: {random_choice}")

# Example 4: Shuffling a list
shuffle_list = [1, 2, 3, 4, 5]
random.shuffle(shuffle_list)
print(f"Shuffled list: {shuffle_list}")

# Example 5: Generating a random sample of elements from a list
sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random_sample = random.sample(sample_list, 3)
print(f"Random sample of 3 elements from a list: {random_sample}")

# Example 6: Generating a random floating point number within a range
random_float_range = random.uniform(1.5, 4.5)
print(f"Random float between 1.5 and 4.5: {random_float_range}")

# Example 7: Generating a random integer using randrange
random_randrange = random.randrange(0, 101, 5)  # From 0 to 100, step 5
print(f"Random integer from 0 to 100 with step 5: {random_randrange}")

# Example 8: Seed the random number generator
random.seed(10)
seeded_random = random.random()
print(f"Seeded random number: {seeded_random}")
random.seed(10)  # Resetting seed to get the same number again
print(f"Seeded random number (again to demonstrate reproducibility): {random.random()}")

# Example 9: Generating a random boolean
random_bool = random.choice([True, False])
print(f"Random boolean: {random_bool}")

# Example 10: Generating a weighted random choice
weights = [0.1, 0.2, 0.7]  # Probabilities for each choice
weighted_choice = random.choices(['low', 'medium', 'high'], weights=weights, k=1)[0]
print(f"Weighted random choice: {weighted_choice}")

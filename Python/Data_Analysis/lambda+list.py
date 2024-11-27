"""
[Practice from: Codesignal]

Write a function using a lambda that takes a dictionary of passengers with their ages and returns a list of names of adults (age >= 18).
"""

# Function to get a list of adult passengers' names
def get_adult_names(passenger_dict):
    is_adult = lambda age: age >= 18
    return [name for name, age in passenger_dict.items() if is_adult(age)]

# Example usage
passenger_dict = {
    "Alice": 30,
    "Bob": 17,
    "Charlie": 22,
    "David": 15
}
adults = get_adult_names(passenger_dict)
print(adults)  # Expected Output: ['Alice', 'Charlie']

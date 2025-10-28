"""
You are given an array audiences consisting of positive integers representing the audience size for different performances at a music festival.

Return the combined size of every audience that had the maxmium size.

The audience size of a performance is the number of people who attended that performance.

Input:
audiences1 = [100, 200, 200, 150, 100, 250]

audiences2 = [120, 180, 220, 150, 220]

Output:
250

440

Constraints: None

Edge Case: Empty input -> 0

Plan:

Dict with key value pairs 220 -> 2
Then multiply both: but find the max first
"""

def max_audience_performances(audiences):
    dictionary = {}

    for size in audiences:
        dictionary[size] = dictionary.get(size, 0) + 1
    
    max_size = max(dictionary.keys())

    for key, value in dictionary.items():
        if key == max_size:
            return key * value

audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))
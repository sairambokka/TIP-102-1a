# Nom Nom Numbers
# A number can "eat" the number to its right if it’s larger than that number.

# When it eats, it becomes the sum of both numbers.

# Keep repeating this process from left to right until no more eating can happen.

# Examples
# nom_nom([5, 3, 7])
# output = [15]

# nom_nom([5, 3, 9])
# output = [8, 9]

# nom_nom([1, 2, 3])
# output = [1, 2, 3]

# nom_nom([2, 1, 3])
# output = [3, 3]

# nom_nom([8, 5, 9])
# output = [22]

# nom_nom([6, 5, 6, 100])
# output = [17, 100]

"""
    5 3 7
    i j
    i > j:
        i + j = 8
        res = [i + j, rest]

    The process goes from left to right
    The process doesn't start from the middle
    Array length is not fixed!
    there can be a satisfactory pair in the middle somewhere, but we should start from left and move to right until the end
    two pointer? i and j or i and i + 1
    If no constraint satisfaction, move i
    else sum it up, create a new array, and reset i
"""

def nom_nom(values):
    i = 0
    while i < len(values) - 1:
        if values[i] > values[i + 1]:
            values = values[:i] + [values[i] + values[i + 1]] + values[i + 2:]
            i = 0
        else:
            i += 1

    return values
        
    

print(nom_nom([5, 3, 7]))
print(nom_nom([5, 3, 9]))
print(nom_nom([1, 2, 3]))
print(nom_nom([2, 1, 3]))
print(nom_nom([8, 5, 9]))
print(nom_nom([6, 5, 6, 100]))



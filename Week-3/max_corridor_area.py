"""
area = l * w

l = min(h1, h2)
w = (j - i)

max_area = max(max_area, area)
"""
def max_corridor_area(height):
    max_area = 0
    i = 0
    j = len(height) - 1

    while i < j:
        h = min(height[i], height[j])
        width = j - i
        area = width * h
        max_area = max(max_area, area)

        if height[i] < height[j]:
            i += 1
        else:
            j -= 1

    return max_area

print(max_corridor_area([1, 8, 6, 2, 5, 4, 8, 3, 7])) 
print(max_corridor_area([1, 1])) 
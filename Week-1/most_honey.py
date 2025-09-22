"""
Christopher Robin is helping Pooh construct the biggest hunny jar possible.

Help him write a function that accepts an integer array heights of length n. The height of each element is given by heights[i].

There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, heights[i]).

Find two lines that, together with the x-axis, form the container that holds the most honey.

Return the maximum amount of honey a container can store.

Notice that you may not slant the container.

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
most_honey(height)

height = [1, 1]
most_honey(height)

49
1

We need to maximize the area --> height * width
Height is the min of two values, width is the distance between points (j - i)

Area = (j - i) * min(height[i], height[j])

max_area = max(max_area, area)
"""

def most_honey(heights):
    max_area = 0

    for i in range(0, len(heights)):
        for j in range(1, len(heights)):
            h = min(heights[i], heights[j])
            w = j - i
            area = h * w
            max_area = max(max_area, area)

    return max_area

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(most_honey(height))

height = [1, 1]
print(most_honey(height))
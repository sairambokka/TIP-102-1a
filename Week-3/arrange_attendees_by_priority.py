"""
You are organizing a large event and need to arrange the attendees based on their priority levels. You are given a 0-indexed list attendees, where each element represents the priority level of an attendee, and an integer priority that indicates a particular level of priority.

Your task is to rearrange the attendees list such that the following conditions are met:

Every attendee with a priority less than the specified priority appears before every attendee with a priority greater than the specified priority.
Every attendee with a priority equal to the specified priority appears between the attendees with lower and higher priorities.
The relative order of the attendees within each priority group (less than, equal to, greater than) must be preserved.
Return the attendees list after the rearrangement.

Input: [9,12,5,10,14,3,10], 10
[-3,4,3,2], 2 -> [-3, 4]

Outputs:
[9,5,3,10,10,12,14] -> [9, 5, 3 | 10, 10 | 12, 14]
[-3,2,4,3]
"""

def arrange_attendees_by_priority(attendees, priority):
    less = []
    greater = []
    equal = []
    i = 0
    j = len(attendees) - 1
    k = (i + j + 1) // 2

    for n in attendees:
        if n < priority:
            less.append(n)
        if n == priority:
            equal.append(n)
        if n > priority:
            greater.append(n)
    
    return (less + equal + greater)

def arrange_attendees_by_priority_v2(attendees, priority): # Does not preserve high order
    i = 0
    low = 0
    high = len(attendees) - 1

    while i <= high:
        if attendees[i] < priority:
            attendees[i], attendees[low] = attendees[low], attendees[i]
            i += 1
            low += 1
        elif attendees[i] > priority:
            attendees[i], attendees[high] = attendees[high], attendees[i]
            high -= 1
        else:
            i += 1
        
    return attendees

print(arrange_attendees_by_priority_v2([9,12,5,10,14,3,10], 10)) 
print(arrange_attendees_by_priority_v2([-3,4,3,2], 2)) 
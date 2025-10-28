"""
You are organizing an event, and you have a 0-indexed list guests of even length, where each element represents either an attendee (positive integers) or an absence (negative integers). The list contains an equal number of attendees and absences.

You should return the guests list rearranged to satisfy the following conditions:

Every consecutive pair of elements must have opposite signs, indicating that each attendee is followed by an absence or vice versa.
For all elements with the same sign, the order in which they appear in the original list must be preserved.
The rearranged list must begin with an attendee (positive integer).
Return the rearranged list after organizing the guests according to the conditions.

Input:
[3,1,-2,-5,2,-4]
[-1,1]

Output:
[3,-2,1,-5,2,-4]
[1,-1]
"""
def rearrange_guests(guests):
    attn = []
    abst = []
    result = []
    for n in guests:
        if n < 0:
            abst.append(n)
        else:
            attn.append(n)

    for i in range(len(attn)):
        result.append(attn[i])
        result.append(abst[i])

    return result

print(rearrange_guests([3,1,-2,-5,2,-4]))  
print(rearrange_guests([-1,1]))

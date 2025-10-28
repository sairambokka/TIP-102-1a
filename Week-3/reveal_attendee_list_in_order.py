"""
You are planning a special event where each attendee has a unique registration number. These numbers are listed in the provided array attendees, but they are currently out of order.

At the event, attendees will walk on stage one by one following this special reveal process:

The person at the front of the line walks on stage (this number is revealed).
If there are still people left in line, the next person in front moves to the back of the line.
Steps 1 and 2 repeat until everyone has walked on stage.
Your task is to rearrange the attendees list before the process starts so that the attendees walk on stage by registration number in increasing order.

Write a function reveal_attendee_list_in_order(attendees) that returns an array with the correct starting order, such that when the attendees follow the above reveal process they walk on stage from smallest registration number to largest registration number.

Input: [17,13,11,2,3,5,7] -> [17, 13, 11, 7, 5, 3, 2] -> []
[1,1000]

Example Output: [2,13,3,11,5,17,7]
[1,1000]
"""
from collections import deque
def reveal_attendee_list_in_order(attendees):
    result = deque()
    l = sorted(attendees, reverse=True)

    for n in l:
        if not result:
            result.append(n)
        else:
            temp = result.pop()
            result.appendleft(temp)
            result.appendleft(n)
    return list(result)



print(reveal_attendee_list_in_order([17,13,11,2,3,5,7])) 
print(reveal_attendee_list_in_order([1,1000]))
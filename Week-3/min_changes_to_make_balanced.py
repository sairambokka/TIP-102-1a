"""
You are organizing a series of events, and each event is represented by a parenthesis in the string schedule, where an opening parenthesis ( represents the start of an event, and a closing parenthesis ) represents the end of an event. A balanced schedule means every event that starts has a corresponding end.

However, due to some scheduling issues, the current schedule might not be balanced. In one move, you can insert either a start or an end at any position in the schedule.

Return the minimum number of moves required to make the schedule balanced.

Inputs:
())
(((

Outputs:
1
3
"""
def min_changes_to_make_balanced(schedule):
    stack = []
    count = 0

    for ch in schedule:
        if ch == '(':
            stack.append(ch)
        if ch == ')':
            if stack:
                stack.pop()
            else:
                count += 1
    
    return (count + len(stack))

print(min_changes_to_make_balanced("())"))
print(min_changes_to_make_balanced("(((")) 
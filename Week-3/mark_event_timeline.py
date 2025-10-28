"""
You are organizing a large event, and you need to mark the timeline for a series of scheduled activities.

You are given two strings:

event: A short string representing an event name.
timeline: A longer string representing the full timeline for the event.
Initially, the timeline is empty and represented by a string t of the same length as timeline, where every character is '?'.

In one turn, you can "mark" the timeline by placing the event string over any valid position in t and copying its letters onto t. This replaces the corresponding '?' characters in t.

Rules:

You can only place event where it fully fits within t.
Each time you mark the timeline, the corresponding letters in t are updated.
Your goal is to perform a sequence of marks so that t becomes exactly equal to timeline.
You may use at most 10 * len(timeline) marks.
Return a list of the starting indices where you placed the event string during each mark. If it is impossible to turn t into timeline following these rules, return an empty list.

Input: "abc", "ababc"
"abca", "aabcaca"

Output:[0, 2]
[3, 0, 1]
"""
from collections import deque
def mark_event_timeline(event, timeline):
    queue = deque('?')*9
    return queue

print(mark_event_timeline("abc", "ababc"))  
print(mark_event_timeline("abca", "aabcaca")) 
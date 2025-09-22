"""
Write a function remove_dupes() that accepts a sorted array items, and removes the duplicates in-place such that each element appears only once. Return the length of the modified array. You may not create another array; your implementation must modify the original input array items.

items = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
remove_dupes(items)

Ans: 4

items = ["extract of malt", "haycorns", "honey", "thistle"]
remove_dupes(items)

Ans: 4
"""

def remove_dupes(items):
    if not items:
        return 0
    
    i = 0

    for j in range(1, len(items)):
        if items[j]!=items[i]:
            i += 1
            items[i] = items[j]
    return i + 1, items[:i + 1]

items = ["extract of malt", "haycorns", "honey", "honey", "honey", "honey", "thistle", "thistle"]
print(remove_dupes(items))

items = ["extract of malt", "haycorns", "honey", "thistle"]
print(remove_dupes(items))
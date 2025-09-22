"""
Write a function reverse_list() that takes in a list lst and returns elements of the list in reverse order. The list should be reversed in-place without using list slicing (e.g. lst[::-1]).

lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]
reverse_list(lst)

["eeyore", "roo", "piglet", "christopher robin", "pooh"]
"""

def reverse_list(lst):
    i = 0
    j = len(lst) - 1

    while(i < j):
        temp = lst[i]
        lst[i] = lst[j]
        lst[j] = temp
        i+=1
        j-=1
    return lst

lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]
print(reverse_list(lst))



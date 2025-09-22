"""
You are given an array of intervals, where each interval is represented as [start, end].

Write a function merge_intervals(intervals) that merges all overlapping intervals and returns a new array of the merged, non-overlapping intervals.
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
merge_intervals(intervals)

1, 2, 3
   2, 3, 4, 5, 6
                   8, 9, 10
				   
list1, list2

list2[1] < list1[1]:
list1[1] = list2[1]
intervals.delete(list2)

intervals = [[1, 4], [4, 5]]
merge_intervals(intervals)

[[1, 6], [8, 10], [15, 18]]
[[1, 5]]
"""

def merge_intervals(intervals):
	intervals.sort(key=lambda x: x[0])
	merged = []
	for interval in intervals:
		if not merged or merged[-1][1] < interval[0]:
			merged.append(interval)
		else:
			merged[-1][1] = max(merged[-1][1], interval[1])
	print(merged)
	
    

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
merge_intervals(intervals)

intervals = [[1, 4], [4, 5]]
merge_intervals(intervals)
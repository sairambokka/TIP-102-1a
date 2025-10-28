"""
Understand - Find the diff and return the app with max diff
Plan - Sort the list, max = 6, min = 0, current_diff = v[max] - v[min]
        if diff < current_diff:
            result = key
            diff = current_diff
Assumption: List size is 7
"""

def most_varied_app(app_usage):
    result = ""
    diff = 0
    # for k, v in app_usage.items(): # O(n)
    #     sorted_v = sorted(v) # O(klogk) -> If we assume it is 7, then it is O(1)
    #     current_diff = sorted_v[6] - sorted_v[0]
    #     if current_diff > diff:
    #         result = k
    #         diff = current_diff

    for k, v in app_usage.items(): # O(n)
        current_diff = max(v) - min(v) # O(k) -> O(7)
        if current_diff > diff:
            result = k
            diff = current_diff
    
    return result # O(n * k) // O(n) and Space is O(1)


app_usage = {
    "Instagram": [60, 55, 65, 60, 70, 55, 60],
    "YouTube": [100, 120, 110, 100, 115, 105, 120],
    "Snapchat": [30, 35, 25, 30, 40, 35, 30]
}

app_usage_2 = {
    "Twitter": [15, 15, 15, 15, 15, 15, 15],
    "Reddit": [45, 50, 55, 50, 45, 50, 55],
    "Facebook": [80, 85, 80, 85, 80, 85, 80]
}

app_usage_3 = {
    "TikTok": [80, 100, 90, 85, 95, 105, 90],
    "Spotify": [40, 45, 50, 45, 40, 45, 50],
    "WhatsApp": [60, 60, 60, 60, 60, 60, 60]
}

print(most_varied_app(app_usage))
print(most_varied_app(app_usage_2))
print(most_varied_app(app_usage_3))
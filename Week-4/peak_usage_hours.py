"""


"""

def peak_usage_hours(screen_time):
    m = 0
    index = 0
    for i in range(0, len(screen_time) - 2):
        ans = screen_time[i] + screen_time[i + 1] + screen_time[i + 2]
        if ans > m:
            m = ans
            index = i
    
    return (index, m)


screen_time = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240]
screen_time_2 = [5, 15, 10, 20, 30, 25, 50, 40, 35, 45, 60, 55, 65, 75, 70, 85, 95, 90, 100, 110, 105, 115, 120, 125]
screen_time_3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

print(peak_usage_hours(screen_time))
print(peak_usage_hours(screen_time_2))    
print(peak_usage_hours(screen_time_3)) 
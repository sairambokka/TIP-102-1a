"""
Given two lists of strings artists and set_times of length n, write a function lineup() that maps each artist to their set time.

An artist artists[i] has set time set_times[i]. Assume i <= 0 < n and len(artists) == len(set_times).

Inputs:
artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"] - List[Strings]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"] - List[Strings]

Output:
{"Kendrick Lamar": "9:30 PM", "Chappell Roan": "5:00 PM", "Mitski": "2:00 PM", "Rosalía": "7:30 PM"} - Dict

Constraints:
len(artists) == len(set_times)

Edge:
Empyt list (Artists or Settimes) -> {}

Plan:

"""

def lineup(artists, set_times):
    lineup = {}

    if not artists or not set_times:
        return {}

    for i in range(len(artists)):
        lineup[artists[i]] = set_times[i]

    return lineup


artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

print(lineup(artists1, set_times1))
print(lineup(artists2, set_times2))
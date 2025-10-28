"""
As part of the festival, attendees cast votes for their favorite set. Given a dictionary votes that maps attendees id numbers to the artist they voted for, return the artist that had the highest number of votes. If there is a tie, return any artist with the top number of votes.

Input:
votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

Output:

SZA
Ethel Cain
"""

def best_set(votes):
    list = votes.values()
    counter = {}

    for vote in list:
        counter[vote] = counter.get(vote, 0) + 1

    max_votes = max(counter.values())
    
    for key, value in counter.items():
        if value == max_votes:
            return key
    
    

votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print(best_set(votes1))
print(best_set(votes2))
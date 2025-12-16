data = """1001:Alice
1002:Bob
1003:Alice
ERROR_READING_LINE
1004: Charlie
1005:Alice
1006:Bob
1007:   
1008:David"""

with open("votes.txt", "w") as f:
    f.write(data)
temp_dictionary = {}
total_votes = 0
with open("votes.txt", "r") as file:
    for line in file:
        if not ":" in line:
            continue
        id, name = line.strip().split(":", 1)
        name.strip()
        if not name:
            continue
        if name in temp_dictionary:
            temp_dictionary[name] += 1
            total_votes +=1
        else:
            temp_dictionary[name] = 1
            total_votes += 1
winner = None
max_vote = 0
for name, vote in temp_dictionary.items():
    if vote > max_vote:
        max_vote = vote
        winner = name
with open("result.txt", "w") as result:
    result.write(f"OFFICIAL ELECTION RESULTS\n")
    result.write(f"-------------------------\n")
    for name in temp_dictionary:
        result.write(f"{name}: {temp_dictionary[name]} votes ({temp_dictionary[name]/total_votes*100:.2f}%)\n")
    result.write(f"\n-------------------------\n")
    result.write(f"Total Valid Votes: {total_votes}\n")
    result.write(f"WINNER: {winner}")

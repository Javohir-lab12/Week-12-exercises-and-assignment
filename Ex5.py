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
result = {}
with open("votes.txt", "r") as file:
    print("OFFICIAL ELECTION RESULTS")
    print("-------------------------")
    for line in file:
        if ":" in line:
            continue
        id, name = line.strip().split()
        if not isinstance(name, str):
            continue
        


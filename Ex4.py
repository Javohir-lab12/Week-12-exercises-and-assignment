# Note the messy spacing and casing
data = """  john smith - 1990
SARAH CONNOR - 1984
  kylo REN - 1995
LARA croft - 1992"""

with open("raw_users.txt", "w") as f:
    f.write(data)
with open("raw_users.txt", "r") as file:
    for line in file:
        line = line.strip().replace(" -","").split()
        first_name, last_name, birth_year = line
        first_name = first_name.lower()
        first_name = first_name[0].upper() + first_name[1:]
        last_name = last_name.lower() 
        last_name = last_name[0].upper() + last_name[1:]
        birth_year = int(birth_year)
        age = 2025-birth_year
        with open("clean_profiles.txt", "a") as result:
            result.write(f"Name: {first_name} {last_name} (Age: {age})\n")
# File 1: Words to ignore
stops = """the
is
at
on
a
and"""

with open("stopwords.txt", "w") as f:
    f.write(stops)

# File 2: The text to analyze
story = """The cat sat on the mat. 
The cat is a good cat. 
Is the dog on the mat? No, the dog is at the park."""

with open("story.txt", "w") as f:
    f.write(story)
stopwords = []
punctuations = [".", ",", "?", "!"]
result = {}
with open("stopwords.txt", "r") as file1:
    for line in file1:
        line = line.strip()
        stopwords.append(line)
with open("story.txt", "r") as file2:
    for line in file2:
        words = line.strip().lower().split()
        for word in words:
            for c in word:
                if c in punctuations:
                    word = word.replace(c, "")
            if word in stopwords:
                continue
            elif word in result:
                result[word] += 1
            else:
                result[word] = 1
with open("analysis.txt", "w") as file3:
    file3.write("WORD FREQUENCY REPORT\n")
    file3.write("---------------------\n")
    for word, count in result.items():
        file3.write(f"{word}: {count}\n")
entry = []
single = []
with open("input4.txt", "r") as f:
    for count, line in enumerate(f):
        while line != '\n':
            single.append(line)
        while line == '\n':
            entry.append(single)
            single = []
            break

print(count)

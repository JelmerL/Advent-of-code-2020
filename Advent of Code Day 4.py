entry = []
single = []
#read in the source file
with open("input4.txt", "r") as f:
    for line in f:
        line = line.replace("\n","")
        if line!='\n':
            single.append(line)
        if line=='':
            entry.append(single)
            single =[]

print(entry[2])
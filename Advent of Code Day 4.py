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

for count, item in enumerate(entry):
    print(type(entry))
print(entry[2])
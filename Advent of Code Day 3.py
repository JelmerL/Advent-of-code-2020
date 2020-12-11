matrix = []
with open("input3.txt", "r") as f:
    for line in f:
        line = line * 74
        line = line.replace("n", '')
        matrix.append(line)

# matrix = [item.replace("\n",'') for item in matrix]e

treecount = []
slopex = 0
slopey = 0

slopedeltay = [1, 1, 1, 1, 2]
slopedeltax = [1, 3, 5, 7, 1]

for count, item in enumerate(slopedeltay):
    trees = 0
    slopey = 0
    slopex = 0
    while slopey < 323:
        location = matrix[slopey][slopex]
        slopex += slopedeltax[count]
        slopey += slopedeltay[count]
        if location == '#':
            trees += 1
    treecount.append(trees)

print(treecount[0] * treecount[1] * treecount[2] * treecount[3] * treecount[4])
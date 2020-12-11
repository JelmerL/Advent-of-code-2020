import itertools
import re
expenses1 = [line.strip() for line in open('input.txt')]
expenses = [int(i) for i in expenses1]
permutations =  list(itertools.permutations(expenses, r=3))
i=[]
j=0
while i!=2020:
    j+=1
    i=sum(permutations[j])
 
values = list(permutations[j])
print(values[0]*values[1]*values[2])

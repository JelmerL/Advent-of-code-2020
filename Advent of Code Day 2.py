import re

with open("input2.txt", "r") as temp_file:
    passwords = [line.rstrip('\n') for line in temp_file]

passwords = [item.replace(":", '') for item in passwords]
passwords = [item.split() for item in passwords]
numbers =[]
character =[]
password = []
correct = 0
for items in passwords:
    for count, item in enumerate(items):
        if count == 0:
            numbers.append(item)

numbers = [number.split("-") for number in numbers]
numbers = [[int(x) for x in y] for y in numbers]

for items in passwords:
    for count, item in enumerate (items):
        if count== 1:
            character.append(item)

for items in passwords:
    for count, item in enumerate(items):
        if count == 2:
            password.append(item)


#for i, items in enumerate(password):
 #   matches = items.count(character[i])
  #  print(matches)
   # print(i)
    #if matches>=numbers[i][0] and matches<=numbers[i][1]:
     #   correct += 1
      #  print("YES")
    #else:
    #    print("NO")

for i, items in enumerate(password):
    word = password[i]
    number = numbers[i][0]-1
    number2 = numbers[i][1]-1
    letter = character[i]

    lettermatch1 = items[number]
    lettermatch2 = items[number2]

    if (lettermatch1==letter) is not (lettermatch2 == letter):
        correct +=1
    


print(correct)

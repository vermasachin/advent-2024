import re

day3_sample = ""
day3 = ""

with open("../inputs/day3_sample", 'r') as file:
    day3_sample = file.read()

with open("../inputs/day3", 'r') as file:
    day3 = file.read()


sol1 = 0
sol2 = 0
do = True

pattern = "mul\([0-9]{1,3},[0-9]{1,3}\)|don't\(\)|do\(\)"
match = re.findall(pattern, day3)

for i in range(len(match)):
    if (re.search("mul\([0-9]{1,3},[0-9]{1,3}\)", match[i])):
        first_num = re.findall("[0-9]{1,3}",match[i])[0]
        second_num = re.findall("[0-9]{1,3}",match[i])[1]
        sol1 += int(first_num) * int(second_num)
        if (do == True):
            sol2 += int(first_num) * int(second_num)
    elif(re.search("don't\(\)", match[i])):
        do = False
    elif(re.search("do\(\)", match[i])):
        do = True

print(sol1)
print(sol2)
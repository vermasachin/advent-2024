day1_sample = open("../inputs/day1_sample", "r")
day1 = open("../inputs/day1", "r")

left_col = []
right_col = []

for line in day1:
    left_col.append(int(line.split(" ")[0]))
    right_col.append(int(line.split(" ")[3]))


left_col.sort()
right_col.sort()

sol1 = 0
sol2 = 0

for i in range(len(left_col)):
    sol1 += abs(left_col[i] - right_col[i])
    sol2 += left_col[i] * right_col.count(left_col[i])

print(sol1)
print(sol2)


day2_sample = open("../inputs/day2_sample", "r")
day2 = open("../inputs/day2", "r")

sol1 = 0
sol2 = 0

def check_safeness(row):
    inc_count = 0
    dec_count = 0
    same_count = 0
    
    for i in range(len(row) - 1):
        if abs(row[i] - row[i+1]) > 3 or row[i] == row[i+1]:
            same_count += 1
        if row[i] < row[i+1]:
            inc_count += 1
        elif row[i] > row[i+1]:
            dec_count += 1

    if bool(inc_count) ^ bool(dec_count) and not bool(same_count):
        return True
    return False

for line in day2:
    row = [int(item.strip()) for item in line.split()]
    safe = check_safeness(row)
    if safe:
        sol1 += 1
        sol2 += 1
    else:
        for i in range(len(row)):
            new_row = row.copy()
            new_row.pop(i)
            safe = check_safeness(new_row)
            if safe:
                sol2 += 1
                break

print(sol1)
print(sol2)
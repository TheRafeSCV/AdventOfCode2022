sum = 0
list_sums = []
with open('data.txt') as f:
    lines = f.readlines()
    for line in lines:
        if (line[0] != '\n'):
            sum += int(line)
            list_sums.append(sum)
        else:
            sum = 0
            continue
print(max(list_sums))

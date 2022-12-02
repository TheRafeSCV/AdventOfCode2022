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

top_elf_cal = max(list_sums)
list_sums.remove(top_elf_cal)
second_top_cal = max(list_sums)
list_sums.remove(second_top_cal)
third_top_cal = max(list_sums)

print(str(top_elf_cal + second_top_cal + third_top_cal))

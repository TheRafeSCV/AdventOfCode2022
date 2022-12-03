list_chars = []
list_vals = []
with open('data.txt') as f:
    lines = [line.rstrip() for line in f]
    groups_of_3 = list(zip(*[iter(lines)]*3))

    for group in groups_of_3:
        first_set_unique_chars = ''.join(set(group[0]))
        second_set_unique_chars = ''.join(set(group[1]))
        third_set_unique_chars = ''.join(set(group[2]))
        for char in first_set_unique_chars:
            if char in second_set_unique_chars and char in third_set_unique_chars:
                list_chars.append(char)
            else:
                continue

# print(list_chars)
# print(len(list_chars))

for char in list_chars:
    if char == char.lower():
        list_vals.append(ord(char) - 96)
    else:
        list_vals.append(ord(char) - 38)

# print(list_vals)
# print(len(list_vals))
print(sum(list_vals))

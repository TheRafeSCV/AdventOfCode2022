list_chars = []
list_vals = []
with open('data.txt') as f:
    lines = [line.rstrip() for line in f]
    for line in lines:
        half = int(len(line) / 2)
        first_half = line[:half]
        second_half = line[half:]
        # keep only unique chars
        first_half_adj = ''.join(set(first_half))
        second_half_adj = ''.join(set(second_half))
        for char in first_half_adj:
            if char in second_half_adj:
                list_chars.append(char)
            else:
                continue

for char in list_chars:
    if char == char.lower():
        list_vals.append(ord(char) - 96)
    else:
        list_vals.append(ord(char) - 38)

# print(list_chars)
# print(list_vals)
print(sum(list_vals))

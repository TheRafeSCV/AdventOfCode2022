num_overlap = 0
with open('data.txt') as f:
    lines = f.read().splitlines()
    for line in lines:
        num_grp1, num_grp2 = line.split(',')
        num1, num2 = num_grp1.split('-')
        num3, num4 = num_grp2.split('-')
        num1 = int(num1)
        num2 = int(num2)
        num3 = int(num3)
        num4 = int(num4)
        if num1 <= num3 <= num4 <= num2 or num3 <= num1 <= num2 <= num4:
           num_overlap +=1
print(num_overlap)

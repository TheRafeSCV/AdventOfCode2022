i = 0
sum = 0

'''
A - Rock (1)
B - Paper (2)
C - Sciccor (3)
X - Rock
Y - Paper
Z - Sciccor   

Lost - 0
Draw - 3
Won - 6
'''

with open('data.txt') as f:
    lines = [line.rstrip() for line in f]
    while i < len(lines):
        if (lines[i][0] == 'A') & (lines[i][-1] == 'Y'):
            sum += 8
        elif (lines[i][0] == 'A') & (lines[i][-1] == 'X'):
            sum += 4
        elif (lines[i][0] == 'A') & (lines[i][-1] == 'Z'):
            sum += 3
        elif (lines[i][0] == 'B') & (lines[i][-1] == 'Y'):
            sum += 5
        elif (lines[i][0] == 'B') & (lines[i][-1] == 'X'):
            sum += 1
        elif (lines[i][0] == 'B') & (lines[i][-1] == 'Z'):
            sum += 9
        elif (lines[i][0] == 'C') & (lines[i][-1] == 'Y'):
            sum += 2
        elif (lines[i][0] == 'C') & (lines[i][-1] == 'X'):
            sum += 7
        elif (lines[i][0] == 'C') & (lines[i][-1] == 'Z'):
            sum += 6
        else:
            sum += 0
        i += 1
print(sum)

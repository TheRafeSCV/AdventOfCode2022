with open('data.txt') as f:
    datastrem = f.read()
    for i in range(len(datastrem)):
        if len(set(datastrem[i - 4 : i])) == 4:
            break
    print(i)
    
with open('data.txt') as f:
    datastrem = f.read()
    for i in range(len(datastrem)):
        if len(set(datastrem[i - 14 : i])) == 14:
            break
    print(i)

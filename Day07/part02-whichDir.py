dict_dirs_sizes = {}
list_paths = []
dir_size = 0

lines = [line for line in open('data.txt').read().strip().split('\n')]

for line in lines:
    if line == '$ cd ..':
        list_paths = list_paths [:-1]
    elif line.startswith('$ cd '):
        list_paths.append(line[5:])
        dict_dirs_sizes[str(list_paths)] = [[], 0]        
    elif line.startswith('dir'):
        dict_dirs_sizes[str(list_paths)].append([line[4:], 0])
    elif not line.startswith('$'):
        size, name = line.split(' ')
        size = int(size)
        dict_dirs_sizes[str(list_paths)].append([name, size])
        tempPath = list_paths
        while len(tempPath) > 1:
            tempPath = tempPath[:-1]
            dict_dirs_sizes[str(tempPath)][1] += size
    else:
        continue
list_smlst_lrg_dir = []
for key,value in dict_dirs_sizes.items():
    file_size = 0
    for val in value:
        if type(val) == list and len(val) == 2:
            file_size += val[1]
        elif type(val) == int:
            file_size += val
    if 70_000_000 - 42_476_859 + file_size > 30_000_000:
        list_smlst_lrg_dir.append((key, file_size))

list_smlst_lrg_dir = sorted(list_smlst_lrg_dir, key= lambda x: x[1])
print(list_smlst_lrg_dir[0])

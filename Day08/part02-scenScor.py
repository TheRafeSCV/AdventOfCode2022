with open('data.txt') as lines:
    line = lines.read().splitlines()

    grid = [[int(height) for height in item] for item in line]
    # print(grid)
    def tree_visible(tree_height, x, y):
        num_of_non_visible_sides = 0
        top = 0
        right = 0
        bottom = 0
        left = 0

        a = x - 1
        while a >= 0:
            top += 1
            if tree_height <= grid[a][y]:
                num_of_non_visible_sides += 1
                break
            a -= 1
        b = y + 1
        while b < len(grid[x]):
            right += 1
            if tree_height <= grid[x][b]:
                num_of_non_visible_sides += 1
                break
            b += 1
        c = x + 1
        while c < len(grid):
            bottom += 1
            if tree_height <= grid[c][y]:
                num_of_non_visible_sides += 1
                break
            c += 1
        d = y - 1
        while d >= 0:
            left += 1
            if tree_height <= grid[x][d]:
                num_of_non_visible_sides += 1
                break
            d -= 1
        return [num_of_non_visible_sides != 4, top, right, bottom, left]

    num_of_visible_trees = 0
    visibility_of_tress = []

    for i, row in enumerate(grid[1:-1], 1):
        for j, tree in enumerate(row[1:-1], 1):
            [is_visible, top, right, bottom, left] = tree_visible(tree, i, j)
            visibility_of_tress.append(top * right * bottom * left)

print(max(visibility_of_tress))

def make_forest(file):
    trees = []
    for line in file:
        trees.append(list(line.strip('\n')))
    return trees


def count_visible(forest):
    rows = len(forest)
    cols = len(forest[0])

    visible_trees = 0

    for row in range(0, rows):
        # outer rows
        if row == 0 or row == rows-1:
            visible_trees += len(forest[row])
        # inner rows
        else:
            for col in range(0, cols):
                # outer columns
                if col == 0 or col == cols-1:
                    visible_trees += 1
                # inner columns
                else:
                    visible_trees += get_visibility(forest, row, col)
    print(visible_trees)


def get_visibility(forest, cur_row, cur_col):
    visible_tree = 1
    cur_height = forest[cur_row][cur_col]

    # check above
    for row in range(0, cur_row):
        if forest[row][cur_col] >= cur_height:
            visible_tree = 0
            break
    if visible_tree == 1:
        return visible_tree

    visible_tree = 1
    # check below
    for row in range(cur_row+1, len(forest)):
        if forest[row][cur_col] >= cur_height:
            visible_tree = 0
            break
    if visible_tree == 1:
        return visible_tree

    # check to the left
    visible_tree = 1
    for col in range(0, cur_col):
        if forest[cur_row][col] >= cur_height:
            visible_tree = 0
            break
    if visible_tree == 1:
        return visible_tree

    # check to the right
    visible_tree = 1
    for col in range(cur_col+1, len(forest[0])):
        if forest[cur_row][col] >= cur_height:
            visible_tree = 0
            break

    return visible_tree

def get_scenic_scores(forest):
    rows = len(forest)
    cols = len(forest[0])

    high_score = 0

    # look at all of the trees
    for row in range(rows):
        for col in range(cols):
            high_score = look_from_tree(forest, row, col, high_score)

    print(high_score)

def look_from_tree(forest, cur_row, cur_col, high_score):
    tree_counts = [0, 0, 0, 0]
    cur_height = forest[cur_row][cur_col]

    # look up
    for row in range(cur_row-1, -1, -1):
        tree_counts[0] += 1
        if forest[row][cur_col] >= cur_height:
            break

    # look down
    for row in range(cur_row+1, len(forest)):
        tree_counts[1] += 1
        if forest[row][cur_col] >= cur_height:
            break

    # look left
    for col in range(cur_col-1, -1, -1):
        tree_counts[2] += 1
        if forest[cur_row][col] >= cur_height:
            break

    # look right
    for col in range(cur_col+1, len(forest[0])):
        tree_counts[3] += 1
        if forest[cur_row][col] >= cur_height:
            break

    result = 1
    for count in tree_counts:
        result *= count

    if result > high_score:
        return result
    else:
        return high_score


if __name__ == "__main__":
    with open("input/day8_input", "r") as file:
        forest = make_forest(file)
        print(forest)
        count_visible(forest)
        get_scenic_scores(forest)

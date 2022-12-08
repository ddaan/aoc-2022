test_text = """30373
25512
65332
33549
35390"""


def get_file(name):
    with open(name) as file:
        lines = file.read().splitlines()
    return lines


def get_visible_trees(matrix):
    size_y = len(matrix)
    size_x = len(matrix[0])

    visible_trees = (size_x * 2) + (size_y * 2) - 4
    scores = []
    for y in range(1, size_y - 1):
        for x in range(1, size_x - 1):
            tree_height = matrix[y][x]

            from_left = list(matrix[y][0:x])
            from_right = list(matrix[y][x + 1:])
            from_top = [matrix[t][x] for t in range(0, y)]
            from_bottom = [matrix[t][x] for t in range(y + 1, size_y)]

            is_visible = tree_height > max(from_left) or \
                         tree_height > max(from_right) or \
                         tree_height > max(from_top) or \
                         tree_height > max(from_bottom)

            visible_trees += 1 if is_visible else 0

            from_top.reverse()
            from_left.reverse()

            try:
                score_left = [pos for pos, height in enumerate(from_left) if tree_height <= height][0] + 1
            except IndexError:
                score_left = len(from_left)

            try:
                score_right = [pos for pos, height in enumerate(from_right) if tree_height <= height][0] + 1
            except IndexError:
                score_right = len(from_right)

            try:
                score_top = [pos for pos, height in enumerate(from_top) if tree_height <= height][0] + 1
            except IndexError:
                score_top = len(from_top)

            try:
                score_bottom = [pos for pos, height in enumerate(from_bottom) if tree_height <= height][0] + 1
            except IndexError:
                score_bottom = len(from_bottom)

            scores.append(score_left * score_right * score_top * score_bottom)

    return visible_trees, max(scores)


def test():
    matrix = test_text.split("\n")
    print(get_visible_trees(matrix))
    assert get_visible_trees(matrix) == (21, 8)


def main():
    test()
    lines = get_file('input')
    print(get_visible_trees(lines))


if __name__ == "__main__":
    main()

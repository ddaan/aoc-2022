text_input = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

test_input_part_2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

# X, Y
directions = {
    'U': (0, -1),
    'D': (0, 1),
    'L': (-1, 0),
    'R': (1, 0)
}


def get_file(name):
    with open(name) as file:
        lines = file.read().splitlines()
    return lines


class Grid:

    def __init__(self, tail_length=1) -> None:
        # Coordinagte X, Y
        self.head_location = (0, 0)
        self.tail_length = tail_length
        self.tail_location = {}
        self.tail_history = {tuple([0, 0])}
        self.tail_prev_location = {}

        for knot in range(0, self.tail_length):
            self.tail_location[knot] = (0, 0)
            self.tail_prev_location[knot] = (0, 0)

    def move(self, line):
        direction, steps = line.split(' ')
        for step in range(1, int(steps) + 1):
            new_x = self.head_location[0] + directions[direction][0]
            new_y = self.head_location[1] + directions[direction][1]
            self.head_location = (new_x, new_y)

            for knot in range(0, self.tail_length):
                if knot == 0:
                    x_diff = self.head_location[0] - self.tail_location[knot][0]
                    y_diff = self.head_location[1] - self.tail_location[knot][1]
                else:
                    x_diff = self.tail_location[knot - 1][0] - self.tail_location[knot][0]
                    y_diff = self.tail_location[knot - 1][1] - self.tail_location[knot][1]

                print(knot, x_diff, y_diff, self.tail_location[knot])
                if abs(x_diff) > 1 or abs(y_diff) > 1:
                    x_diff_sign = -1 if x_diff < 0 else 1
                    y_diff_sign = -1 if y_diff < 0 else 1

                    if x_diff == 0:
                        new_x = self.tail_location[knot][0]
                        new_y = self.tail_location[knot][1] + y_diff_sign
                        self.tail_location[knot] = new_x, new_y

                    elif y_diff == 0:
                        new_x = self.tail_location[knot][0] + x_diff_sign
                        new_y = self.tail_location[knot][1]
                        self.tail_location[knot] = new_x, new_y

                    # If it is in different row AND column, it will need to move diagonally
                    else:
                        new_x = self.tail_location[knot][0] + x_diff_sign
                        new_y = self.tail_location[knot][1] + y_diff_sign
                        self.tail_location[knot] = new_x, new_y

                    print('move knot', knot, 'to', self.tail_location[knot])
                    if knot + 1 == self.tail_length:
                        self.tail_history.add(self.tail_location[knot])

        print(self.tail_history)
        print(len(self.tail_history))


def test():
    grid = Grid()
    lines = text_input.split('\n')
    for line in lines:
        grid.move(line)

    assert (len(grid.tail_history)) == 13

    grid = Grid(tail_length=9)
    lines = text_input.split('\n')
    for line in lines:
        grid.move(line)

    assert (len(grid.tail_history)) == 1

    grid = Grid(tail_length=9)
    lines = test_input_part_2.split('\n')
    for line in lines:
        grid.move(line)

    assert (len(grid.tail_history)) == 36



def main():
    test()
    lines = get_file('input')
    grid = Grid()
    for line in lines:
        grid.move(line)
    print (len(grid.tail_history))

    grid = Grid(tail_length=9)
    for line in lines:
        grid.move(line)
    print (len(grid.tail_history))


if __name__ == "__main__":
    main()

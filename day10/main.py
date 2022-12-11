import math

test_input = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""


def get_file(name):
    with open(name) as file:
        lines = file.read().splitlines()
    return lines


class Device():

    def __init__(self) -> None:
        self.cycle = 0
        self.value = 1
        self.signal_strength = 0
        self.watch_list = [20, 60, 100, 140, 180, 220]
        self.watch_list_total = 0
        self.display = [list('.' * 40) for _ in range(0, 6)]
        self.draw_pixel()

    @property
    def row(self):
        return math.floor((self.cycle - 1) / 40)

    @property
    def pos(self):
        return (self.cycle - 1) % 40

    def parse_line(self, line):
        if line == 'noop':
            self.add_cycle()
        else:
            command, value = line.split(' ')
            if command == 'addx':
                self.add_cycle()
                self.add_cycle()
                self.add_value(int(value))

    def add_cycle(self):
        self.cycle += 1
        self.update_signal_strength()
        self.draw_pixel()
        if self.cycle in self.watch_list:
            self.watch_list_total += self.signal_strength
            print(f"For cycle {self.cycle} the signal strength = {self.signal_strength}")

    def draw_pixel(self):
        print (f"self.cycle {self.cycle}, self.row {self.row}, self.pos {self.pos}, self.value {self.value}")
        self.display[self.row][self.pos] = '#' if self.value in [self.pos - 1, self.pos, self.pos + 1] else '.'

    def add_value(self, value):
        self.value += value
        self.update_signal_strength()

    def update_signal_strength(self):
        self.signal_strength = self.cycle * self.value


def test():
    lines = test_input.split('\n')
    d = Device()
    for line in lines:
        d.parse_line(line)
    print (d.watch_list_total)
    assert d.watch_list_total == 13140
    test_result = [
        '##..##..##..##..##..##..##..##..##..##..',
        '###...###...###...###...###...###...###.',
        '####....####....####....####....####....',
        '#####.....#####.....#####.....#####.....',
        '######......######......######......####',
        '#######.......#######.......#######.....'
    ]
    for i, row in enumerate(d.display):
        print (''.join(row))
        print(test_result[i])
        assert ''.join(row) == test_result[i]


def main():
    test()
    lines = get_file('input')
    d = Device()
    for line in lines:
        d.parse_line(line)

    print (d.watch_list_total)
    for i, row in enumerate(d.display):
        print (''.join(row))

if __name__ == "__main__":
    main()

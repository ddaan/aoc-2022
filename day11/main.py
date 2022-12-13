from copy import deepcopy
from math import prod

monkeys = {}
class Monkey():

    def __init__(self, monkey_nr, starting_items:[], operation:str, test_divisble_by, test_true, test_false):
        self.monkey_nr = int(monkey_nr)
        self.items = starting_items
        self.operation = operation
        self.test_divisble_by = test_divisble_by
        self.test_true = int(test_true)
        self.test_false = int(test_false)
        self.total_inspects = 0
        self.moncky_mod = None

    @classmethod
    def from_monkey_def(cls, lines):
        """  Example:
        Monkey 0:
          Starting items: 79, 98
          Operation: new = old * 19
          Test: divisible by 23
            If true: throw to monkey 2
            If false: throw to monkey 3
        """
        monkey_nr = lines[0].split(' ')[1][0]
        items_str = lines[1].split(':')[1]
        items = [int(x) for x in items_str.strip().replace(' ','').split(',')]
        operation_str = lines[2].split('=')[1]
        operation = operation_str.strip()
        test_divisble_by = int(lines[3].split('divisible by ')[1])
        test_true = lines[4].split(' monkey ')[1]
        test_false = lines[5].split(' monkey ')[1]
        return cls(monkey_nr, items, operation, test_divisble_by, test_true, test_false)

    def keep_lvl_manageble(self, new):
        if self.moncky_mod:
            return new % self.moncky_mod
        else:
            return new // 3

    def inspect(self, item):
        old = item
        new = eval(self.operation)  # Sets new
        new = self.keep_lvl_manageble(new)

        if new % self.test_divisble_by == 0:
            # print (f"Throw {new} to {self.test_true}")
            monkeys[self.test_true].items.append(new)
        else:
            # print (f"Throw {new} to {self.test_false}")
            monkeys[self.test_false].items.append(new)

        self.total_inspects += 1

    def inspect_all_items(self):
        # print(f"{self.monkey_nr} has items {self.items}")
        for item in deepcopy(self.items):
            # print(f'{self.monkey_nr} inspects {item}')
            self.inspect(item)
        self.items = []


def get_file(name):
    with open(name) as file:
        lines = file.read().splitlines()
    return lines


def test():
    lines = get_file('testinput')
    for monkey_list in [lines[i:i + 7] for i in range(0, len(lines), 7)]:
        m = Monkey.from_monkey_def(monkey_list)
        monkeys[m.monkey_nr] = m

    for x in range(0, 20):
        for monkey in monkeys.values():
            monkey.inspect_all_items()

        for monkey in monkeys.values():
            print(monkey.monkey_nr, monkey.items)

    assert monkeys[0].items == [10, 12, 14, 26, 34]
    assert monkeys[1].items == [245, 93, 53, 199, 115]
    assert monkeys[2].items == []
    assert monkeys[3].items == []

    import pdb; pdb.set_trace()
    assert monkeys[0].total_inspects == 101
    assert monkeys[1].total_inspects == 95
    assert monkeys[2].total_inspects == 7
    assert monkeys[3].total_inspects == 105

    two_most_inspects = sorted([m.total_inspects for m in monkeys.values()])
    total = two_most_inspects[-1] * two_most_inspects[-2]
    assert total == 10605

def test_part2():
    lines = get_file('testinput')
    for monkey_list in [lines[i:i + 7] for i in range(0, len(lines), 7)]:
        m = Monkey.from_monkey_def(monkey_list)
        monkeys[m.monkey_nr] = m

    moncky_mod = prod([m.test_divisble_by for m in monkeys.values()])
    for monkey in monkeys.values():
        monkey.moncky_mod = moncky_mod

    for x in range(1, 10001):
        for monkey in monkeys.values():
            monkey.inspect_all_items()

        if x in [1, 20, 1000]:
            for monkey in monkeys.values():
                print(x, monkey.monkey_nr, monkey.total_inspects)

            import pdb; pdb.set_trace()

    assert monkeys[0].total_inspects == 52166
    assert monkeys[1].total_inspects == 47830
    assert monkeys[2].total_inspects == 1938
    assert monkeys[3].total_inspects == 52013

    two_most_inspects = sorted([m.total_inspects for m in monkeys.values()])
    total = two_most_inspects[-1] * two_most_inspects[-2]
    assert total == 2713310158

def part1():
    lines = get_file('input')
    for monkey_list in [lines[i:i + 7] for i in range(0, len(lines), 7)]:
        m = Monkey.from_monkey_def(monkey_list)
        monkeys[m.monkey_nr] = m

    for x in range(0, 20):
        for monkey in monkeys.values():
            monkey.inspect_all_items()

    for monkey in monkeys.values():
        print(monkey.monkey_nr, monkey.items)

    two_most_inspects = sorted([m.total_inspects for m in monkeys.values()])
    total = two_most_inspects[-1] * two_most_inspects[-2]
    print(total)


def part2():
    lines = get_file('input')
    for monkey_list in [lines[i:i + 7] for i in range(0, len(lines), 7)]:
        m = Monkey.from_monkey_def(monkey_list)
        m.is_part_2 = True
        monkeys[m.monkey_nr] = m

    moncky_mod = prod([m.test_divisble_by for m in monkeys.values()])
    for monkey in monkeys.values():
        monkey.moncky_mod = moncky_mod

    for x in range(0, 10000):
        for monkey in monkeys.values():
            monkey.inspect_all_items()

        for monkey in monkeys.values():
            print(x, monkey.monkey_nr, monkey.total_inspects)

    for monkey in monkeys.values():
        print(monkey.monkey_nr, monkey.items)

    two_most_inspects = sorted([m.total_inspects for m in monkeys.values()])
    total = two_most_inspects[-1] * two_most_inspects[-2]
    print(total)

def main():
    test_part2()
    part2()


if __name__ == "__main__":
    main()

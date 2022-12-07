import string

items = string.ascii_lowercase + string.ascii_uppercase


def get_file(name):
    with open(name) as file:
        lines = file.readlines()
    return lines


class Stack:

    def __init__(self) -> None:
        super().__init__()
        self.stack = {}

    def load_initial_stack(self, lines):
        size_of_stack = int(max(lines[-1].split(' ')))
        self.stack = {nr: [] for nr in range(1, size_of_stack + 1)}
        inventory = lines[:-1]
        inventory.reverse()
        for line in inventory:
            inventory = [line[i:i + 4] for i in range(0, len(line), 4)]
            for pos, crate in enumerate(inventory):
                crate = crate.replace(' ', '').replace('\n', '').replace('[', '').replace(']', '')
                if crate:
                    self.stack[pos + 1].append(crate)

    def move(self, amount, from_pos, to_pos):
        for x in range(0, amount):
            crate = self.stack[from_pos].pop()
            self.stack[to_pos].append(crate)

    def move_9001(self, amount, from_pos, to_pos):
        crates = self.stack[from_pos][-amount:]
        self.stack[to_pos].extend(crates)
        self.stack[from_pos] = self.stack[from_pos][:-amount]


def test_initial_stack():
    text = '    [D]\n' \
           '[N] [C]\n' \
           '[Z] [M] [P]\n' \
           ' 1   2   3'
    stack = Stack()
    lines = text.split('\n')
    stack.load_initial_stack(lines)
    print(stack.stack)
    assert stack.stack[1] == ['Z', 'N']
    assert stack.stack[2] == ['M', 'C', 'D']
    assert stack.stack[3] == ['P']
    return stack


def test_move(stack):
    text = \
        'move 1 from 2 to 1\n' \
        'move 3 from 1 to 3\n' \
        'move 2 from 2 to 1\n' \
        'move 1 from 1 to 2'
    lines = text.split('\n')
    for line in lines:
        _, amount, _, from_pos, _, to_pos = line.split(' ')
        print (int(amount), int(from_pos), int(to_pos))
        stack.move(int(amount), int(from_pos), int(to_pos))

    assert stack.stack[1] == ['C']
    assert stack.stack[2] == ['M']
    assert stack.stack[3] == ['P', 'D', 'N', 'Z']

def test_move_9001(stack):
    text = \
        'move 1 from 2 to 1\n' \
        'move 3 from 1 to 3\n' \
        'move 2 from 2 to 1\n' \
        'move 1 from 1 to 2'
    lines = text.split('\n')
    for line in lines:
        _, amount, _, from_pos, _, to_pos = line.split(' ')
        print (int(amount), int(from_pos), int(to_pos))
        stack.move_9001(int(amount), int(from_pos), int(to_pos))

    assert stack.stack[1] == ['M']
    assert stack.stack[2] == ['C']
    assert stack.stack[3] == ['P', 'Z', 'N', 'D']


def main():
    stack = test_initial_stack()
    test_move(stack)

    stack = Stack()
    lines = get_file('input')
    initial_stack = lines[0:9]
    stack.load_initial_stack(initial_stack)
    for line in lines[10:]:
        _, amount, _, from_pos, _, to_pos = line.split(' ')
        print (int(amount), int(from_pos), int(to_pos))
        stack.move(int(amount), int(from_pos), int(to_pos))

    print (stack.stack)
    last_item = ''
    for pos, stack in stack.stack.items():
        last_item += stack.pop()
    print(last_item)

    # part 2

    stack = test_initial_stack()
    test_move_9001(stack)

    stack = Stack()
    lines = get_file('input')
    initial_stack = lines[0:9]
    stack.load_initial_stack(initial_stack)
    for line in lines[10:]:
        _, amount, _, from_pos, _, to_pos = line.split(' ')
        print (int(amount), int(from_pos), int(to_pos))
        stack.move_9001(int(amount), int(from_pos), int(to_pos))

    print (stack.stack)
    last_item = ''
    for pos, stack in stack.stack.items():
        last_item += stack.pop()
    print(last_item)

if __name__ == "__main__":
    main()

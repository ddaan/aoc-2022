import string

items = string.ascii_lowercase + string.ascii_uppercase


def get_file(name):
    with open(name) as file:
        lines = file.readlines()
    return lines

def overlaps(line):
    range_a, range_b = line.split(',')
    from_a, to_a = range_a.split('-')
    from_a, to_a = int(from_a), int(to_a) + 1
    from_b, to_b = range_b.split('-')
    from_b, to_b = int(from_b), int(to_b) + 1
    set_range_a = set(range(int(from_a), int(to_a)))
    set_range_b = set(range(int(from_b), int(to_b)))
    return len(set_range_a.intersection(set_range_b)) > 0

def fully_contains_other(line):
    range_a, range_b = line.split(',')
    from_a, to_a = range_a.split('-')
    from_a, to_a = int(from_a), int(to_a) + 1
    from_b, to_b = range_b.split('-')
    from_b, to_b = int(from_b), int(to_b) + 1
    set_range_a = set(range(int(from_a), int(to_a)))
    set_range_b = set(range(int(from_b), int(to_b)))
    print('------')
    print(line)
    print('.' * (from_a) + ''.join([str(x % 10) for x in range(from_a, to_a)]) + ('.' * (100 - to_a)))
    print('.' * (from_b) + ''.join([str(x % 10) for x in range(from_b, to_b)]) + ('.' * (100 - to_b)))
    contains = len(set_range_a - set_range_b) == 0 or len(set_range_b - set_range_a) == 0
    print(str(contains)+'\n')
    return contains


def test_fully_contains():
    assert fully_contains_other('2-4,6-8') is False
    assert fully_contains_other('2-3,4-5') is False
    assert fully_contains_other('5-7,7-9') is False
    assert fully_contains_other('2-8,3-7') is True
    assert fully_contains_other('6-6,4-6') is True
    assert fully_contains_other('2-6,4-8') is False

    assert fully_contains_other('44-44,44-67') is True
    assert fully_contains_other('7-69,69-69') is True
    assert fully_contains_other('3-74,73-73') is True
    assert fully_contains_other('8-78,9-75') is True
    assert fully_contains_other('43-51,51-52') is False


def main():
    test_fully_contains()
    lines = get_file('input')
    total = 0
    for line in lines:
        total += 1 if fully_contains_other(line.strip()) else 0
    print(total)

    total = 0
    for line in lines:
        total += 1 if overlaps(line.strip()) else 0

    print(total)

    if __name__ == "__main__":
        main()
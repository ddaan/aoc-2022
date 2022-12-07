import string

items = string.ascii_lowercase + string.ascii_uppercase

def get_file(name):
    with open(name) as file:
        lines = file.readlines()
    return lines

def process_line(line):
    line = line.strip()
    split = len(line.strip()) // 2
    first_halve, second_halve = set(line[:split]), set(line[split:])
    overlap = first_halve & second_halve
    return [items.find(x) + 1 for x in overlap]

def process_group(lines):
    line_set = [set(l) for l in lines]
    overlap = line_set[0] & line_set[1] & line_set[2]
    return [items.find(x) + 1 for x in overlap]

def main():
    lines = get_file('input')
    priorities = []
    for line in lines:
        priorities.extend(process_line(line.strip()))

    print(sum(priorities))

    priorities = []
    import pdb; pdb.set_trace()
    for i in range(0, len(lines), 3):
        group = [l.strip() for l in lines[i : i + 3]]
        try:
            priorities.extend(process_group(group))
        except Exception:
            print(group)

    print(sum(priorities))


if __name__ == "__main__":
    main()
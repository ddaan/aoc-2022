from collections import defaultdict


def get_file(name):
    with open(name) as file:
        lines = file.readlines()
    return lines

def main():
    elves_calory = {}
    elve_nr = 1
    lines = get_file('input')
    for line in lines:
        line = line.strip()
        if len(line) == 0:
            elve_nr += 1
        else:
            current_calory = elves_calory.get(elve_nr, 0)
            elves_calory[elve_nr] = current_calory + int(line)

    top_three = sorted(elves_calory, key=elves_calory.get)[-3:]
    print(sum([elves_calory.get(elve_nr) for elve_nr in top_three]))

if __name__ == "__main__":
    main()
from collections import defaultdict


def get_file(name):
    with open(name) as file:
        lines = file.readlines()
    return lines

def main():
    kind_of_play_points = {
        'X': 1,
        'Y': 2,
        'Z': 3,
    }
    beats = {
        'A': 'Z',
        'B': 'X',
        'C': 'Y',
    }

    looses = {
        'A': 'Y',
        'B': 'Z',
        'C': 'X',
    }
    draw = {
        'A': 'X',
        'B': 'Y',
        'C': 'Z',
    }

    lines = get_file('input')
    total_points = 0
    for line in lines:
        line = line.strip()
        player_a_plays, player_b_plays = line.split(' ')
        if player_b_plays == 'X':
            # Need tot loose
            player_b_plays = beats[player_a_plays]
        elif player_b_plays == 'Y':
            player_b_plays = draw[player_a_plays]
        else:
            player_b_plays = looses[player_a_plays]

        total_points += kind_of_play_points.get(player_b_plays)
        if beats[player_a_plays] == player_b_plays:
            total_points += 0
        elif draw[player_a_plays] == player_b_plays:
            total_points += 3
        else:
            total_points += 6

    print (total_points)

if __name__ == "__main__":
    main()
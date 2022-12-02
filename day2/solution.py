with open("input.txt", 'r') as f:
    lines = f.readlines()

lines = [x.strip() for x in lines]

# Question 1:

score_dict = {
        'X': {
            'A': 3,
            'B': 0,
            'C': 6
        },
        'Y': {
            'A': 6,
            'B': 3,
            'C': 0
        },
        'Z': {
            'A': 0,
            'B': 6,
            'C': 3
        }
}

points_dict = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

def score_game(game):
    opp, player = game.split(' ')
    return score_dict[player][opp] + points_dict[player]
    
print('Question 1: ', sum(score_game(x) for x in lines))

# Question 2:

play_dict = {
        'X': {
            'A': 'Z',
            'B': 'X',
            'C': 'Y'
        },
        'Y': {
            'A': 'X',
            'B': 'Y',
            'C': 'Z'
        },
        'Z': {
            'A': 'Y',
            'B': 'Z',
            'C': 'X'
        }
}

def find_play(game):
    opp, result = game.split(' ')
    return f'{opp} {play_dict[result][opp]}'

print('Question 2: ', sum(score_game(find_play(x)) for x in lines))

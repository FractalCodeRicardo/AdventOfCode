O_ROCK = "A"
O_PAPPER = "B"
O_SCISSORS = "C" 

M_ROCK = "X"
M_PAPPER = "Y"
M_SCISSORS = "Z" 


def get_rounds():
    f = open("02 input.txt", "r")

    content = f.read()
    lists = content.split("\n")

    return lists 

def score_outcome(opponent_shape, my_shape):
    if my_shape == M_ROCK and opponent_shape == O_SCISSORS: return 6 
    if my_shape == M_PAPPER and opponent_shape == O_ROCK: return 6
    if my_shape == M_SCISSORS and opponent_shape == O_PAPPER: return 6

    if my_shape == M_ROCK and opponent_shape == O_ROCK: return 3 
    if my_shape == M_PAPPER and opponent_shape == O_PAPPER: return 3
    if my_shape == M_SCISSORS and opponent_shape == O_SCISSORS: return 3

    return 0

def score_shape(my_shape):
    if my_shape == M_ROCK: return 1
    if my_shape == M_PAPPER: return 2
    if my_shape == M_SCISSORS: return 3

    return 0

def score_round(opponent_shape, my_shape):
    outcome = score_outcome(opponent_shape, my_shape)
    shape = score_shape(my_shape)

    return outcome + shape

def solve():
    rounds = get_rounds()

    total_score = 0
    for round in rounds:
        shapes = round.split(" ")
        opponent_shape = shapes[0]
        my_shape = shapes[1]

        score = score_round(opponent_shape, my_shape)
        print(score)
        total_score += score
    
    print(total_score)

solve()






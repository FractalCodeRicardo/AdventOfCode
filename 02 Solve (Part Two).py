O_ROCK = "A"
O_PAPPER = "B"
O_SCISSORS = "C" 

M_ROCK = "X"
M_PAPPER = "Y"
M_SCISSORS = "Z" 

R_LOSE = "X"
R_DRAW = "Y"
R_WIN = "Z" 

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

def calculate_shape(opponent_shape, result):
    if opponent_shape == O_SCISSORS and result == R_WIN: return M_ROCK
    if opponent_shape == O_PAPPER and result == R_WIN: return M_SCISSORS
    if opponent_shape == O_ROCK and result == R_WIN: return M_PAPPER

    if opponent_shape == O_SCISSORS and result == R_DRAW: return M_SCISSORS
    if opponent_shape == O_PAPPER and result == R_DRAW: return M_PAPPER
    if opponent_shape == O_ROCK and result == R_DRAW: return M_ROCK

    if opponent_shape == O_SCISSORS and result == R_LOSE: return M_PAPPER
    if opponent_shape == O_PAPPER and result == R_LOSE: return M_ROCK
    if opponent_shape == O_ROCK and result == R_LOSE: return M_SCISSORS

    raise Exception("Error")

def score_round(opponent_shape, my_shape):
    outcome = score_outcome(opponent_shape, my_shape)
    shape = score_shape(my_shape)

    return outcome + shape

def solve():
    rounds = get_rounds()

    total_score = 0
    for round in rounds:
        letters = round.split(" ")

        opponent_shape = letters[0]
        result = letters[1]

        my_shape = calculate_shape(opponent_shape, result)

        score = score_round(opponent_shape, my_shape)
        print(score)
        total_score += score
    
    print(total_score)

solve()






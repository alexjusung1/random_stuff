from functools import wraps
import numpy as np
import random
import time

HEIGHT, WIDTH, BOMB_COUNT = 4, 4, 0
BOMB_MATRIX = ((1, 1, 1), (1, 9, 1), (1, 1, 1))
VERBOSE = True

# def print_board(board):
#     print('\n'.join(''.join(row) for row in board))

def input_verification(func):
    @wraps(func)
    def input_verification_wrapper(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if VERBOSE:
                    print(e)
                print('Try again...')
    return input_verification_wrapper
            
@input_verification
def location_input():
    i, j = map(int, input('Input your starting location (i, j): ').rstrip().split(', '))
    if not (0 <= i < HEIGHT and 0 <= j < WIDTH):
        raise ValueError('Invalid starting location')
    return i, j

def gen_board():
    i, j = location_input()
    seed = hash(time.time())
    random.seed(seed)
    no_bombs = [x*WIDTH + y for x in range(max(0, i-1), min(HEIGHT, i+2)) for y in range(max(0, j-1), min(WIDTH, j+2))]
    no_bomb_length = HEIGHT * WIDTH - len(no_bombs)
    board = [0 for _ in range(no_bomb_length)]
    for bomb in random.sample(range(no_bomb_length), BOMB_COUNT):
        board[bomb] = 1
    for no_bomb in no_bombs:
        board.insert(no_bomb, 0)
    print(f'Board generated with seed {seed}...')
    return np.array(board, dtype=np.int_).reshape(HEIGHT, WIDTH)

def main():
    board = gen_board()
    

if __name__ == '__main__':
    main()
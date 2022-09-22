import heapq
import numpy as np
from typing import List
from collections import defaultdict
import math
#import cProfile

def solve_puzzle(init_board: List[List[int]]) -> List[int]:
    init_board = np.array(init_board, dtype=int)
    m, n = init_board.shape
    solved_board = np.arange(1, m*n+1).reshape(m, n)
    solved_board[-1, -1] = 0
    if (m < 2 or n < 2):
        if np.array_equal(init_board, solved_board):
            return []
        raise Exception('Puzzle not solvable')
    i, j = np.where(init_board == 0)
    i, j = i[0], j[0]

    cached_result = {}
    # --- Manhattan heuristic functions ---
    def heuristic_manhattan(board) -> int:
        total = 0
        for i, row in enumerate(board):
            for j, num in enumerate(row):
                if num:
                    i_prime, j_prime = divmod(num-1, n)
                    total += abs(i - i_prime) + abs(j - j_prime)
        cached_result[board.tobytes()] = total
        return total
    def heuristic_manhattan_delta(next_board, cur_h, zero_i, zero_j, other_i, other_j) -> int:
        '''Calculates heuristic using the previous heuristic'''
        if next_board.tobytes() in cached_result:
            return cached_result[next_board.tobytes()]
        i_prime, j_prime = divmod(next_board[zero_i, zero_j]-1, n)
        if zero_i == other_i:
            if other_j < zero_j <= j_prime or j_prime <= zero_j < other_j:
                return cur_h - 1
            return cur_h + 1
        else:
            if other_i < zero_i <= i_prime or i_prime <= zero_i < other_i:
                return cur_h - 1
            return cur_h + 1

    # --- Hamming heuristic functions (not implemented yet) ---
    def heuristic_hamming(board):
        pass
    def heuristic_hamming_delta(board):
        pass

    init_heuristic = heuristic_manhattan(init_board)

    poss_board = []
    # push in structure of (f_score, g_score, zero_i, zero_j, path, board)
    heapq.heappush(poss_board, (init_heuristic, 0, i, j, [], init_board))

    g_scores = defaultdict(lambda: math.inf)

    while poss_board:
        cur_f, cur_g, i, j, cur_path, cur_board = heapq.heappop(poss_board)
        if cur_g >= g_scores[cur_board.tobytes()]:
            continue

        if cur_f == cur_g:
            # cur_h is zero -> heuristic is zero -> cur_board == solved_board
            # only works for admissible heuristics
            return cur_path

        g_scores[cur_board.tobytes()] = cur_g
        zero_neighbors = [pos for pos in ((i-1, j), (i+1, j), (i, j-1), (i, j+1))
                            if -1 < pos[0] < m if -1 < pos[1] < n]

        next_g = cur_g + 1
        for other_i, other_j in zero_neighbors:
            next_board = np.copy(cur_board)
            next_board[i, j], next_board[other_i, other_j] = next_board[other_i, other_j], next_board[i, j]
            if next_g < g_scores[next_board.tobytes()]:
                next_path = cur_path.copy()
                next_path.append(cur_board[other_i, other_j])
                next_h = heuristic_manhattan_delta(next_board, cur_f-cur_g, i, j, other_i, other_j)
                heapq.heappush(poss_board, (next_h + next_g, next_g, other_i, other_j, next_path, next_board))
    
    raise Exception('No solution found!')

if __name__ == '__main__':
    m, n = map(int, input('Input the dimensions of the puzzle (m, n): ').rstrip().split())
    board = []
    for _ in range(m):
        board.append(list(map(int, input().rstrip().split())))
    print(solve_puzzle(board))
    #cProfile.run('print(solve_puzzle(board))')
# -----------------------------------------------------------------------------
# Author: Alexander Lubrano
# Course: CS 325 - Analysis of Algorithms
# Date: 03/01/2022
# Description:
#
# -----------------------------------------------------------------------------

import heapq


def solve_puzzle(board, src, dest):
    """

    :param board:
    :param src:
    :param dest:
    :return:
    """

    rows, cols = len(puzzle), len(puzzle[0])
    visited = set()

    pq = [(0, src[0]-1, src[1]-1, '')]    # (cells traversed, row, col, moves)
    visited.add((src[0]-1, src[1]-1))

    while len(pq) > 0:
        dist, cur_row, cur_col, moves = heapq.heappop(pq)

        if cur_row == dest[0] - 1 and cur_col == dest[1] - 1:
            puzz_sol = (dist-1, moves)
            return puzz_sol

        dirs = {'D': (cur_row + 1, cur_col), 'U': (cur_row - 1, cur_col),
                'R': (cur_row, cur_col + 1), 'L': (cur_row, cur_col - 1)}

        for direction in dirs:

            next_row, next_col = dirs[direction][0], dirs[direction][1]

            if 0 <= next_row < rows and 0 <= next_col < cols:
                next_cell = (next_row, next_col)

                if next_cell not in visited and \
                        board[next_row][next_col] != '#':

                    heapq.heappush(pq, (dist+1, next_row,
                                        next_col, moves+direction))
                    visited.add(next_cell)

    return None


if __name__ == '__main__':

    puzzle = [['-', '-', '-', '-', '-'],
              ['-', '-', '#', '-', '-'],
              ['-', '-', '-', '-', '-'],
              ['#', '-', '#', '#', '-'],
              ['-', '#', '-', '-', '-']]

    start = (1, 3)
    end = (3, 3)

    solution = solve_puzzle(puzzle, start, end)
    print(solution)

    start = (1, 1)
    end = (5, 5)

    solution = solve_puzzle(puzzle, start, end)
    print(solution)

    start = (1, 1)
    end = (5, 1)

    solution = solve_puzzle(puzzle, start, end)
    print(solution)
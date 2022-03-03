# -----------------------------------------------------------------------------
# Author: Alexander Lubrano
# Course: CS 325 - Analysis of Algorithms
# Date: 03/01/2022
# Description: This BFS algorithm uses a priority queue and dynamic programming
#     to allow a user to find the minimum number of cells that must be
#     traversed to reach a destination cell in a 2D Puzzle matrix from a
#     starting cell. This matrix is of size M rows by N columns, where M and N
#     are both at least 3 and can be different sizes. Each cell of the puzzle
#     must be either a hyphen "-" or a pound sign "#", which denote open cells
#     and barrier cells, respectively. From the starting cell (a, b), the
#     allowed moves to get to the destination cell (x, y) are up, down, left,
#     and right to directly adjacent cells. If there is a path, the algorithm
#     returns a 2-tuple of the minimum traversed cells (not including start
#     and destination cells) and the moves the algorithm took to arrive there.
#
# -----------------------------------------------------------------------------

import heapq


def solve_puzzle(board, src, dest):
    """
    Takes a 2D puzzle matrix, a source cell, and destination cell. The matrix
    must be of size M by N, where M >= 3 and N >= 3 and can be different sizes.
    Each cell must have either a "-" or "#" that denote open and barrier cells,
    respectively.

    Finds the minimum number of cells that must be traversed to reach the
    destination cell from the source cell using BFS, a priority queue, and
    dynamic programming.

    :param board: 2D array with "-" or "#" in all cells
    :param src: 2-tuple coord. to source cell (src row, src column)
    :param dest: 2-tuple coord. to destination cell (dest row, dest column)
    :return: 2-tuple containing (min traversed cells: int, moves from src: str)
    """

    rows, cols = len(puzzle), len(puzzle[0])
    visited = set()

    # Init the first entry in the priority queue with distance 0, src row, src
    # column, and empty moves string, then add to visited set
    pq = [(0, src[0]-1, src[1]-1, '')]    # (cells traversed, row, col, moves)
    visited.add((src[0]-1, src[1]-1))

    # Loops until solution is found or all reachable cells have been checked
    while len(pq) > 0:

        # Pops the minimum distance 4-tuple off the priority queue
        dist, cur_row, cur_col, moves = heapq.heappop(pq)

        # If dest cell has been reached, return the current distance and moves
        # it took to get there
        if cur_row == dest[0] - 1 and cur_col == dest[1] - 1:
            puzz_sol = (dist-1, moves)
            return puzz_sol

        # Dictionary of possible moves {Down, Up, Right, Left}
        dirs = {'D': (cur_row + 1, cur_col), 'U': (cur_row - 1, cur_col),
                'R': (cur_row, cur_col + 1), 'L': (cur_row, cur_col - 1)}

        # Iterate through moves
        for new_move in dirs:
            # Get next row and column coordinates
            next_row, next_col = dirs[new_move][0], dirs[new_move][1]
            # If both coordinates fall within the bounds of the puzzle board
            if 0 <= next_row < rows and 0 <= next_col < cols:
                next_cell = (next_row, next_col)

                # And if the next cell is unvisited and not a barrier cell
                if next_cell not in visited and \
                        board[next_row][next_col] != '#':
                    # Push to priority queue with new dist, new row, new col,
                    # and new move concatenated with current move string
                    heapq.heappush(pq, (dist + 1, next_row,
                                        next_col, moves + new_move))
                    visited.add(next_cell)

    # Reaches here if no path was found
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
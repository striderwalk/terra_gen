import random

from tiles import TILES, neighbour_map


def find_emtpy(board) -> list:
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == TILES.empty:
                return (i, j)


def is_valid(board, current, pos: tuple) -> bool:
    y, x = pos
    neighbours = []
    if y < len(board) - 1:
        neighbours.append(board[y + 1][x])

    if y > 0:
        neighbours.append(board[y - 1][x])

    if x < len(board) - 1:
        neighbours.append(board[y][x + 1])

    if x > 0:
        neighbours.append(board[y][x - 1])

    # diagonals
    if y < len(board) - 1 and x < len(board) - 1:
        neighbours.append(board[y + 1][x + 1])

    if y < len(board) - 1 and x > 0:
        neighbours.append(board[y + 1][x - 1])

    if y > 0 and x < len(board) - 1:
        neighbours.append(board[y - 1][x + 1])

    if y > 0 and x > 0:
        neighbours.append(board[y - 1][x - 1])

    options = neighbour_map[current]
    # check that no neighbours are banned
    for neighbour in neighbours:
        if neighbour not in options and neighbour != TILES.empty:
            return False

    empty_count = neighbours.count(TILES.empty)

    # check that no neighbours exceed the maximum required count
    for tile, count_range in options.items():
        if neighbours.count(tile) + empty_count > count_range[1]:
            return False

    # check that neighbours meet minimum requirements
    for tile, count_range in options.items():
        if neighbours.count(tile) + empty_count >= count_range[0]:
            return True

    return False


def solve(board) -> bool:
    stack = []
    stack.append(board)

    while stack:
        current_board = stack.pop()
        # print_board(board)
        pos = find_emtpy(current_board)
        if pos:
            i, j = pos

        else:
            return current_board

        tile_list = list(TILES)
        tile_list.remove(TILES.empty)
        random.shuffle(tile_list)

        for num in tile_list:
            if is_valid(current_board, num, (i, j)):
                new_board = [row[:] for row in current_board]
                new_board[i][j] = num
                stack.append(new_board)

    return False


def generate_board(size):
    board = [[TILES.empty for _ in range(size)] for _ in range(size)]
    if current_board := solve(board):
        return current_board
    else:
        print(*board, sep="\n")
        raise RuntimeError("Could not generate board")

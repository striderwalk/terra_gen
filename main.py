import sys
import pygame

from generator import generate_board, solve
from tiles import COLOURS, TILES


TRANS = {
    TILES.empty: " ",
    TILES.water: ".",
    TILES.sand: "#",
    TILES.grass: "&",
    TILES.forest: "|",
}


def print_board(board):
    for i in board:
        for j in i:
            print(TRANS[j], end="")
        print()
    print()


def main():
    sys.setrecursionlimit(4096)
    size = 46

    board = generate_board(size)

    scale = int(600 / size)

    pygame.init()

    win = pygame.display.set_mode((600, 600))

    while True:
        for i in range(len(board)):
            for j in range(len(board[i])):
                pygame.draw.rect(
                    win,
                    COLOURS[board[i][j]],
                    (i * scale, j * scale, scale, scale),
                )
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                board = generate_board(size)

        pygame.display.update()


if __name__ == "__main__":
    main()

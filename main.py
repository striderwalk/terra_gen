import random
import sys
import pygame
from consts import SIZE

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
    print("Starting!")

    board = generate_board(SIZE)

    scale = int(600 / SIZE)

    pygame.init()

    win = pygame.display.set_mode((600, 600))

    while True:
        # get the board
        try:
            _update = next(board)
            update = _update
        except StopIteration:
            pass
        # draw the board
        (i, j), tile = update
        pygame.draw.rect(
            win,
            COLOURS[tile],
            (i * scale, j * scale, scale, scale),
        )
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                board = generate_board(SIZE)
                win.fill((0, 0, 0))

        pygame.display.update()


if __name__ == "__main__":
    main()

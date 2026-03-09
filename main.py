import pygame as pg
from chessEngine import GameState
from board import Board

pg.init()

fps = 20
Images_path = {}


def loadImages():
    pieces = [
        "br",
        "bn",
        "bb",
        "bq",
        "bk",
        "bb",
        "bn",
        "br",
        "bp",
        "wr",
        "wb",
        "wq",
        "wk",
        "wb",
        "wn",
        "wr",
        "wp",
    ]
    for piece in pieces:
        Images_path[piece] = pg.image.load("assets/" + piece + ".png")


def drawGameState(screen, gs, board):
    board.drawBoard(screen)

    board.drawPieces(screen, gs.board, Images_path)


def main():
    board = Board()
    screen = pg.display.set_mode((board.WIDTH, board.HEIGHT))
    clock = pg.time.Clock()
    screen.fill(pg.Color("white"))
    selected_piece = None
    gs = GameState()
    loadImages()
    running = True
    temp = 1
    while running:
        for e in pg.event.get():

            if e.type == pg.QUIT:
                running = False
            if e.type == pg.MOUSEBUTTONDOWN:
                print("yes")
               
                if (selected_piece != None and board.coorToPos(pg.mouse.get_pos()) != selected_piece):

                    mouse_pos = board.coorToPos(pg.mouse.get_pos())

                    gs.board[selected_piece[0]][selected_piece[1]], gs.board[mouse_pos[0]][mouse_pos[1]] = (".", gs.board[selected_piece[0]][selected_piece[1]])
                    selected_piece = None
                selected_piece = board.coorToPos(pg.mouse.get_pos())

        drawGameState(screen, gs, board)
        pg.display.flip()
        clock.tick(fps)


main()

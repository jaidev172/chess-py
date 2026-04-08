import pygame as pg
from chessEngine import GameState
from board import Board


pg.init()
pg.mixer.init()

fps = 20
Images_path = {}

sounds = {
    "move": pg.mixer.Sound("assets/sound/move-self.wav"),
    "capture": pg.mixer.Sound("assets/sound/capture.wav"),
    "check": pg.mixer.Sound("assets/sound/move-check.wav"),
    "game-start": pg.mixer.Sound("assets/sound/game-start.wav"),
    "game-end":pg.mixer.Sound("assets/sound/game-end.wav")

}



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
        Images_path[piece] = pg.image.load("assets/img/" + piece + ".png")

def play_sound(key, loops=0):
    if key in sounds:
        sounds[key].play()


def drawGameState(screen, gs, board,selected_piece,p,k):
    
    board.drawBoard(screen,selected_piece,p,k)
    # board.test(gs.board)
    board.drawPieces(screen, gs.board, Images_path)


def main():
    p,k=[],[]
    board = Board()
    screen = pg.display.set_mode((board.WIDTH, board.HEIGHT))
    clock = pg.time.Clock()
    screen.fill(pg.Color("white"))
    selected_piece = None
    gs = GameState()
    gs.create_board()
    loadImages()
    running = True
    temp = 1
    drawGameState(screen, gs, board,selected_piece,p,k)
    play_sound("game-start")
    while running:
        for e in pg.event.get():

            if e.type == pg.QUIT:
                play_sound("game-end")
                running = False

            if e.type == pg.MOUSEBUTTONDOWN:
                
                print(f"corr{board.coorToPos(pg.mouse.get_pos())}")
                if (selected_piece != None and board.coorToPos(pg.mouse.get_pos()) != selected_piece):
                     
                     moved=gs.move_piece(selected_piece,gs.board,board.coorToPos(pg.mouse.get_pos()),p,k)
                     p,k=[[8,8]],[[8,8]]
                     if moved :
                         play_sound("move")
                     selected_piece=None

                     
                else :
                 selected_piece = board.coorToPos(pg.mouse.get_pos())
                 print(f"selected firest{selected_piece}")
                 if gs.board[selected_piece[0]][selected_piece[1]] !='.':
                    p,k=gs.board[selected_piece[0]][selected_piece[1]].getValidMoves(gs.board)


        drawGameState(screen, gs, board,selected_piece,p,k)

        pg.display.flip()
        clock.tick(fps)


main()

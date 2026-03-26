import pygame as pg

preset=[["white","gray"]]
preset.append(["#ebecd0","#779556"])#tan,green
print(preset[0])
select_colour=pg.Color("#e5c4aa")
class Board:
    def __init__(self):
        self.DIMENSION = 8
        self.WIDTH = self.HEIGHT = 552

        self.sq_size = self.HEIGHT // self.DIMENSION

    def drawBoard(self, screen,selected_piece):
        colors = [pg.Color(preset[1][0]), pg.Color(preset[1][1])]
        for r in range(self.DIMENSION):
            for c in range(self.DIMENSION):
                current_color = colors[((r + c) % 2)]
                # print(f"current color is {current_color}")
                # print((r + c) % 2)
                if selected_piece!=None :
                    print(selected_piece[0])            
                    if selected_piece[0]==[c,r]:

                        current_color=select_colour


                    # print(selected_piece)
                    # prevous=selected_piece
                
                pg.draw.rect(screen,current_color,pg.Rect(c * self.sq_size, r * self.sq_size, self.sq_size, self.sq_size ))

    def drawPieces(self, screen, board, Images_path):
        for r in range(self.DIMENSION):
            for c in range(self.DIMENSION):
                current_img = board[r][c]
                if current_img != ".":
                    screen.blit(Images_path[current_img],((c * self.sq_size) + 3, (r * self.sq_size) + 7))

    def coorToPos(self, pos):
        return (pos[0] // self.sq_size, pos[1] // self.sq_size)

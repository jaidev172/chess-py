import pieces as p
class GameState:

    def __init__(self):
        self.board = [
            [None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None],
        ]
        self.whiteTomove = True
        self.moveLog = []

    def create_board(self):
        self.board[0][0]=p.rook("rook","B",[0,0])             #black
        self.board[0][1]=p.kinght("kinght","B",[0,1])
        self.board[0][2]=p.bishop("bishop","B",[0,2])
        self.board[0][3]=p.queen("queen","B",[0,3])
        self.board[0][4]=p.king("king","B",[0,4])
        self.board[0][5]=p.bishop("bishop","B",[0,5])
        self.board[0][6]=p.kinght("kinght","B",[0,6])
        self.board[0][7]=p.rook("rook","B",[0,7])

      
        for r in range(0,8):
                
            self.board[1][r]=p.pawn('pawn',"B",[1,r])
            self.board[6][r]=p.pawn('pawn',"W",[6,r])


        self.board[7][0]=p.rook("rook","W",[0,0])             #white
        self.board[7][1]=p.kinght("kinght","W",[0,1])
        self.board[7][2]=p.bishop("bishop","W",[0,2])
        self.board[7][3]=p.queen("queen","W",[0,3])
        self.board[7][4]=p.king("king","W",[0,4])
        self.board[7][5]=p.bishop("bishop","W",[0,5])
        self.board[7][6]=p.kinght("kinght","W",[0,6])
        self.board[7][7]=p.rook("rook","W",[0,7])
        for r, row in enumerate(self.board):
            for c, cell in enumerate(row):
               print(f"Row {r}, Col {c}: {type(cell).__name__}")


        def move_piece(self,selected_piece,board):
                    mouse_pos = board.coorToPos(pg.mouse.get_pos())

                    board[selected_piece[0][1]][selected_piece[0][0]], board[mouse_pos[1]][mouse_pos[0]] = (".", board[selected_piece[0][1]][selected_piece[0][0]])
                    board[mouse_pos[1]][mouse_pos[0]].pos=[mouse_pos[1],mouse_pos[0]]
                    
                    selected_piece = None


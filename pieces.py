class piece:
    def __init__(self,type:str,colour:str,pos:list):

        self.type=type
        self.colour=colour
        self.pos=pos
    def img_path(self):
        if self.colour=="B":
            self.img_path="assets"+"/"+self.type+".png"

    def piece_code(self):
        return self.colour.lower()+self.type[0]



class pawn(piece):
    def __init__(self, type, colour, pos):
        super().__init__(type, colour, pos)
        self.firstmove=True

    def getValidMoves(self,board):
        print(f"pos of pawn {self.pos}")
        pos_path=[[8,8]]
        kill=[]
        pos=self.pos
        NB = lambda a, b: a if b == 8 or b == -1 else b
        if self.colour=="B": 
           
            op = lambda a, b: a + b 
        else:
            op = lambda a, b: a - b

        if self.firstmove==True:
            if board[op(pos[0],1)][pos[1]]=="." and board[op(pos[0],2)][pos[1]]==".":
                pos_path=[[op(pos[0],1),pos[1]],[op(pos[0],2),pos[1]]]
            elif board[op(pos[0],1)][pos[1]]==".":
                pos_path=[[op(pos[0],1),pos[1]]]
            self.firstmove=False
        else:
             
            if board[op(pos[0],1)][pos[1]]==".":
                pos_path=[[op(pos[0],1),pos[1]]]

        move=[(op(pos[0],1),NB(pos[1],pos[1]+1)),(op(pos[0],1),NB(pos[1],pos[1]-1))]

        for moves in move:
            if moves[0]==pos[0] or moves[1]==pos[1]:
                continue
            if board[moves[0]][moves[1]]!="." and board[moves[0]][moves[1]].colour!=self.colour:
                kill.append(list(moves))
        if kill==None:
                kill=[8,8]
        return pos_path,kill



        # if move[0]==pos : 
        #     move[0]=None
        # if move[1]==pos:
        #     move[1]=None
        # if     

       


    
    def moves(self):
        pass
class king(piece):

    def __init__(self, type, colour, pos):
        super().__init__(type, colour, pos)
        self.FirstMove=True
    def getValidMoves(self,board):
        pos_path=[]
        kill=[]
        pos=self.pos
        moves=[]
        colour=self.colour
         #[(-1,-1)   (-1,1)  (-1,+1)
         # (1,-1)    (1,1)   (1,+1)
         # (+1,-1    (+1,1)  (+1,+1))]

            
        moves.extend([
            [pos[0],pos[1]+1],
            [pos[0],pos[1]-1],
            [pos[0]-1,pos[1]],
            [pos[0]+1,pos[1]],
            [pos[0]-1,pos[1]-1],
            [pos[0]-1,pos[1]+1],
            [pos[0]+1,pos[1]-1],
            [pos[0]+1,pos[1]+1]
            ])

        
        for r,c in moves:

            if r !=-1 and r!=8 and c!=-1 and c!=8 :
                if board[r][c]==".":
                    pos_path.append([r,c])
                
                elif board[r][c].colour != colour:
                    kill.append([r,c])
        
        return pos_path,kill


            



    
    def moves(self):
        pass

class queen(piece):
     def moves(self):
         pass
     
class rook(piece):
    def moves(self):

        pass

class kinght(piece):
    def __init__(self, type, colour, pos):
        super().__init__(type, colour, pos)
    def piece_code(self):
        return self.colour.lower()+self.type[2]
    def getValidMoves(self,board):
        pos_path=[]
        kill=[]
        pos=self.pos
        moves=[]
        colour=self.colour
        invalid = {-1, -2, 8, 9}

        moves.extend([[pos[0]-1,pos[1]-2],
                      [pos[0]-2,pos[1]-1],
                      [pos[0]-2,pos[1]+1],
                      [pos[0]-1,pos[1]+2],
                      [pos[0]+1,pos[1]+2],
                      [pos[0]+2,pos[1]-1],
                      [pos[0]+2,pos[1]-1],
                      [pos[0]+1,pos[1]-2]
                      ])
        print(moves)
        for r,c in moves:

            if r not in invalid and c not in invalid :
                if board[r][c]==".":
                    pos_path.append([r,c])
                
                elif board[r][c].colour != colour:
                    kill.append([r,c])
        
        return pos_path,kill

class bishop(piece):
    def moves(slef):
        pass




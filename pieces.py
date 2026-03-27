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
    firstmove=True

    
    def moves(self):
        pass
class king(piece):

    
    def moves(self):
        pass

class queen(piece):
     def moves(self):
         pass
     
class rook(piece):
    def moves(self):

        pass

class kinght(piece):
    def moves(self):
        pass
     

class bishop(piece):
    def moves(slef):
        pass




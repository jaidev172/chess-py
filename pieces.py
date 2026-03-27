class piece:
    def __init__(self,type,colour,pos):

        self.type=type
        self.colour=colour
        self.pos=pos
    def img_path(self):
        if self.colour=="b":
            self.img_path="assets"+"/"+self.type+".png"




class pawn(piece):
    firstmove=True

    
    def moves(self):
        pass
class king(piece):

    
    def moves(self):

class queen(piece):
     
    


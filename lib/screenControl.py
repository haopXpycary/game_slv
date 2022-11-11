import copy
import os

# color
class col:
    White     = 0
    Green     = 1
    DarkGreen = 7
    Blue      = 2
    Purple    = 3
    Orange    = 4
    Black     = 5
    Red       = 6

def cprint(x,y,other,color=col.White,bgcolor=col.Black):
    if not other: return;
    scon = "\033[%d;%dH" %(y,x)
    
    if color == col.Black: con = "\033[30m"
    elif color == col.Red: con = "\033[31m"
    elif color == col.Green: con = "\033[32m"
    elif color == col.Orange: con = "\033[33m"
    elif color == col.Blue: con = "\033[34m"
    elif color == col.Purple: con = "\033[35m"
    elif color == col.DarkGreen: con = "\033[36m"
    elif color == col.White: con = "\033[37m"
    
    
    if bgcolor == col.Black: bgcon = "\033[40m"
    elif bgcolor == col.Red: bgcon = "\033[41m"
    elif bgcolor == col.Green: bgcon = "\033[42m"
    elif bgcolor == col.Orange: bgcon = "\033[43m"
    elif bgcolor == col.Blue: bgcon = "\033[44m"
    elif bgcolor == col.Purple: bgcon = "\033[45m"
    elif bgcolor == col.DarkGreen: bgcon = "\033[46m"
    elif bgcolor == col.White: bgcon = "\033[47m"
    
    print(scon+con+bgcon+other,end="")

class screenControl:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
        self.screen = []
        for i in range(self.y):
            self.screen.append([])
            for j in range(self.x):
                self.screen[i].append([' ',col.White,col.Black])
                
        self.nscreen = copy.deepcopy(self.screen)
        
    def update(self,x,y,pic,color=col.White,bgcolor=col.Black):
        if x > self.x or y > self.y: return;
        self.nscreen[y][x] = [pic,color,bgcolor];
    
    def update_word(self,x,y,word,color=col.White,bgcolor=col.Black):
        i = 0;
        for j in str(word):
            self.update(x+i,y,j,color,bgcolor)
            i += 1;

    def show(self):
        for i in range(self.y):
            for j in range(self.x):
                if self.screen[i][j] != self.nscreen[i][j]:
                    cprint(j+1,i+1,self.nscreen[i][j][0],self.nscreen[i][j][1],self.nscreen[i][j][2]);
        self.screen = copy.deepcopy(self.nscreen)

    def get(self,x,y):
        return self.nscreen[y][x];

    def clear(self):
        os.system("clear");
        self.screen = []
        for i in range(self.y):
            self.screen.append([])
            for j in range(self.x):
                self.screen[i].append([' ',col.White,col.Black])
                
        self.nscreen = copy.deepcopy(self.screen)

if __name__ == "__main__":
    '''
    sb = screenControl(10,20)
    sb.show();
    sb.update(1,2,'1',col.Red);
    sb.show();
    sb.update(2,2,sb.get(1,2),col.White);
    '''
    cprint(0,0,'+',col.Red)
    cprint(3,3,'+',col.Red)
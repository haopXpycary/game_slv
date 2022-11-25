import os
import sys
import copy

sys.path.append(os.path.dirname(__file__) + os.sep + '../')

from const_data import cstd

def cprint(x,y,other,color=cstd.White,bgcolor=cstd.Black):
    if not other: return;
    scon = "\033[%d;%dH" %(y,x)
    
    if color == cstd.Black: con = "\033[30m"
    elif color == cstd.Red: con = "\033[31m"
    elif color == cstd.Green: con = "\033[32m"
    elif color == cstd.Orange: con = "\033[33m"
    elif color == cstd.Blue: con = "\033[34m"
    elif color == cstd.Purple: con = "\033[35m"
    elif color == cstd.DarkGreen: con = "\033[36m"
    elif color == cstd.White: con = "\033[37m"
    
    
    if bgcolor == cstd.Black: bgcon = "\033[40m"
    elif bgcolor == cstd.Red: bgcon = "\033[41m"
    elif bgcolor == cstd.Green: bgcon = "\033[42m"
    elif bgcolor == cstd.Orange: bgcon = "\033[43m"
    elif bgcolor == cstd.Blue: bgcon = "\033[44m"
    elif bgcolor == cstd.Purple: bgcon = "\033[45m"
    elif bgcolor == cstd.DarkGreen: bgcon = "\033[46m"
    elif bgcolor == cstd.White: bgcon = "\033[47m"
    
    print(scon+con+bgcon+other,end="")

class screenControl:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
        self.screen = []
        for i in range(self.y):
            self.screen.append([])
            for j in range(self.x):
                self.screen[i].append([' ',cstd.White,cstd.Black])
                
        self.nscreen = copy.deepcopy(self.screen)
        
    def update(self,x,y,pic,color=cstd.White,bgcolor=cstd.Black):
        if x > self.x or y > self.y: return;
        self.nscreen[y][x] = [pic,color,bgcolor];
    
    def update_word(self,x,y,word,color=cstd.White,bgcolor=cstd.Black,byte_len=1):
        i = 0;
        for j in str(word):
            if byte_len == 1:
                self.update(x+i,y,j,color,bgcolor)
            elif byte_len == 2:
                self.update(x+i,y,j,color,bgcolor)
                i += 1;
            i += 1;

    def show(self):
        for i in range(self.y):
            for j in range(self.x):
                if self.screen[i][j] != self.nscreen[i][j]:
                    cprint(j+1,i+1,self.nscreen[i][j][0],self.nscreen[i][j][1],self.nscreen[i][j][2]);
        self.screen = copy.deepcopy(self.nscreen)
        sys.stdout.flush();

    def get(self,x,y):
        return self.nscreen[y][x];

    def clear(self):
        os.system("clear");
        self.screen = []
        for i in range(self.y):
            self.screen.append([])
            for j in range(self.x):
                self.screen[i].append([' ',cstd.White,cstd.Black])
                
        self.nscreen = copy.deepcopy(self.screen)

if __name__ == "__main__":
    '''
    sb = screenControl(10,20)
    sb.show();
    sb.update(1,2,'1',cstd.Red);
    sb.show();
    sb.update(2,2,sb.get(1,2),cstd.White);
    '''
    cprint(0,0,'+',cstd.Red)
    cprint(3,3,'+',cstd.Red)
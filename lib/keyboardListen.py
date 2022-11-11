import sys
import tty
import termios
import threading

class keyboardListen(threading.Thread):
    def __init__(self):
        super().__init__()
        self.ch = None;
        self.stop = False;

        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        tty.setraw(sys.stdin.fileno(), termios.TCSANOW)
        self.getch = sys.stdin.read
        
    def run(self):
        while not self.stop:
            self.ch = self.getch(1)

if __name__ == "__main__":
    import time
    #监听键盘
    get = keyboardListen()
    get.start()
    pressKey = get.ch
    get.ch = None;
    
    while True:
        pressKey = get.ch
        if pressKey != None:
            print(pressKey)

        get.ch = None;
        time.sleep(0.1);
import time

from lib.keyboardListen import keyboardListen
from screenOutput import plr,msgoc,sc,ply;

#隐藏光标
print("\033[?25l",end="")

#监听键盘
get = keyboardListen()
get.start()
pressKey = get.pressKey
get.pressKey = None;

while True:
    pressKey = get.pressKey
    if pressKey != None:
        if pressKey == "w":
            plr.walk(ply.Up)
        elif pressKey == "s":
            plr.walk(ply.Down)
        elif pressKey == "a":
            plr.walk(ply.Left)
        elif pressKey == "r":
            plr.walk(ply.Right)

    get.pressKey = None;
    time.sleep(0.1);
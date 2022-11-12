import time
import os

from const_data import cstd

from lib.keyboardListen import keyboardListen
from lib.screenControl import screenControl

from screenOutputControl import msgOutputControl, output_msg
from initPlayer import init_player
from drawScreenFramework import draw_screen_framework

# 隐藏光标
print("\033[?25l",end="");

# 清空屏幕
os.system("clear");

# 监听键盘
get = keyboardListen()
get.start()
get.pressKey = None;
pressKey = get.pressKey

# 初始化玩家数据
plr = init_player();

sc = screenControl(cstd.MAXSCRX+1,cstd.MAXSCRY+1);
# 绘制屏幕边框
draw_screen_framework(sc);
sc.show();

msgoc = msgOutputControl();
# 显示玩家信息
output_msg(msgoc,plr,sc);
sc.show();

while True:
    pressKey = get.pressKey
    if pressKey != None:
        if pressKey == "w":
            plr.walk(cstd.Up)
        elif pressKey == "s":
            plr.walk(cstd.Down)
        elif pressKey == "a":
            plr.walk(cstd.Left)
        elif pressKey == "r":
            plr.walk(cstd.Right)

    get.pressKey = None;
    time.sleep(0.1);
import time
import os
import sys

from const_data import cstd

from lib.keyboardListen import keyboardListen
from lib.screenControl import screenControl
from lib.recordLog import relogger

from defs.weather import timeSystem

from screenOutputControl import msgOutputControl, output_msg
from initPlayer import init_player
from drawScreenFramework import draw_screen_framework
from drawMap import draw_map,clear_map

# 设置日志
logfile = open("log/main.log","w");
_logger = relogger(logfile);
logout = _logger.logout
logout("Starting...",getframe=sys._getframe());

whrts = timeSystem();
whrts.debug(logout)
logout("wheather.timeSystem return: ",whrts.get_time());

# 隐藏光标
print("\033[?25l",end="");

# 清空屏幕
os.system("clear");

logout("Listening keyboard.")
# 监听键盘
get = keyboardListen()
get.start()
get.ch = None;
pressKey = get.ch

logout("Initialing palyer data.")
# 初始化玩家数据
plr = init_player();

logout("Drawing framework.")
sc = screenControl(cstd.MAXSCRX+1,cstd.MAXSCRY+1);
# 绘制屏幕边框
draw_screen_framework(sc);
sc.show();

logout("Show player message.")
msgoc = msgOutputControl();
# 显示玩家信息
output_msg(msgoc,plr,sc,whrts);
sc.show();

logout("Drawing map.")
draw_map(sc,plr);
sc.show();

logout("Main expression.")
while True:
    pressKey = get.ch
    if pressKey != None:
        if pressKey == "w":
            plr.walk(cstd.Up)
        elif pressKey == "s":
            plr.walk(cstd.Down)
        elif pressKey == "a":
            plr.walk(cstd.Left)
        elif pressKey == "d":
            plr.walk(cstd.Right)
        elif pressKey == "p":
            exit();

        sc.update(94,27,pressKey)

        
        logout("wheather.timeSystem return: ",whrts.get_time());

    draw_map(sc,plr);
    output_msg(msgoc,plr,sc,whrts);

    sc.show(); 
    clear_map(sc,plr)

    get.ch = None;
    time.sleep(0.05);
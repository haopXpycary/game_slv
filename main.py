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
from initThings import initial_material
from drawScreenFramework import draw_screen_framework
from drawMap import draw_map,clear_map
from layoutMap import layoutMap

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

# 初始化物品
logout("Initialing material data.")
thing = dict()
initial_material(thing,logout=logout)

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

# 初始化地图
lym = layoutMap(thing)

# 绘制地图
logout("Drawing map.")
draw_map(sc,plr,lym.map);
sc.show();

logout("Main expression.")
while True:
    pressKey = get.ch
    if pressKey != None:    
        get.ch = None;
        if pressKey == "w":
            plr.walk(cstd.Up,lym.map)
        elif pressKey == "s":
            plr.walk(cstd.Down,lym.map)
        elif pressKey == "a":
            plr.walk(cstd.Left,lym.map)
        elif pressKey == "d":
            plr.walk(cstd.Right,lym.map)
        elif pressKey == "p":
            exit();

        sc.update(94,27,pressKey)

    draw_map(sc,plr,lym.map);
    output_msg(msgoc,plr,sc,whrts);
    sc.show(); 
    clear_map(sc,plr)
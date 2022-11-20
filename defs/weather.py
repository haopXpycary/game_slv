import math
import time
from saved_msg import savedMsg
from const_data import cstd


class timeSystem:
    def __init__(self):
        # 年月日时分秒, 游戏1min=现实1s
        self.time = 0;
        self.smsg = savedMsg();

        if self.smsg["time"]:
            self.time = self.smsg["time"];

        self.current_time = time.time()
        self.start_time = self.current_time - self.time;
        
        self.time_data = self._get_time_defference_data(self.time);

        # 用于debug的函数，默认为空
        self.logout = lambda *L: None;

    # 获取时间差并整理为时间数据
    def _get_time_defference_data(self,time_difference):
        months = (0,31,59,90,120,151,181,212,243,273,304,334,365)
        day = math.floor(time_difference / 60 / 24);
        
        year = 0
        while (day-365*(year+1)) > 0: year += 1;
        day = day - 365*year;

        month = 0;
        while (day-months[month]) > 0: month += 1;

        day = day-months[month];

        hour = math.floor(time_difference / 60 % 24);
        min = math.floor(time_difference % 60);
        second = math.floor(time_difference*60%60);

        return [year,month,day,hour,min,second];
        
    # 时间数据相加
    def _sum_time_data(self,time_data1,time_data2):
        time_data = []
        for i in range(len(time_data1)):
            time.append(time_data1[i]+time_data2[i]);


    def get_time(self):
        #self.logout("time",self.time,'|',"current time",self.current_time,"|","start time",self.start_time,"|","time_data",self.time_data);
        time_difference = time.time() - self.current_time;
        # self.logout("time difference",time_difference)

        # min
        self.time_data[4] += math.floor(time_difference % 60);
        
        while self.time_data[4] > 60: 
            self.time_data[3] += 1;
            self.time_data[4] -= 60;

        while self.time_data[3] > 24: 
            self.time_data[2] += 1;
            self.time_data[3] -= 24;

        # self.time_data = self._sum_time_data(self.time_data,self._get_time_defference_data(time_difference));

        if time_difference >= 1:
            self.current_time = time.time();
        self.save_time();
        return self.time_data;

    def save_time(self):
        self.smsg["time"] = time.time() - self.start_time;

    def get_wheather(self):
        if self.time_data[1] / 3 <= 1:
            return cstd.Spring
        elif self.time_data[1] / 3 <= 2:
            return cstd.Summer
        elif self.time_data[1] / 3 <= 3:
            return cstd.Autumn
        elif self.time_data[1] / 3 <= 4:
            return cstd.Winter

    def debug(self,logout):
        self.logout = logout;
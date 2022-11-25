import time
import os

from psutil import Process

from const_data import cstd

def output_msg(msgoc,plr,sc,whrts):
    time_data = whrts.get_time();
    msgoc.update("Canlender [%s]" %whrts.get_wheather()[:3],"%d-%d-%d" %(time_data[0],time_data[1],time_data[2]))
    msgoc.update("Time","%02d:%02d" %(time_data[3],time_data[4]));
    msgoc.update("Name",plr.name);
    msgoc.update("x,y","%d,%d" %(plr.x,plr.y));
    msgoc.update("Health",plr.health/plr.maxHealth,"float");
    msgoc.update("Protect",plr.protect);
    msgoc.update("Attack",plr.attack);
    msgoc.update("Magic",plr.magic/plr.maxMagic,"float");
    msgoc.update("Satisfaction",plr.satisfaction/plr.maxSatisfaction,"float");
    msgoc.update("Level",plr.level);
    msgoc.update("Exp",plr.exp/cstd.level_up_need_exp(plr.level),"float");
    msgoc.update("Memory","%.6fM" %(Process(os.getpid()).memory_info().rss/1024/1024))
    msgoc.update("Cpu","%f%%" %(Process(os.getpid()).cpu_percent()))
    msgoc.draw(sc);

class msgOutputControl:
    def __init__(self):
        self.all = dict();
        maxwords = 20;
        maxweight = 27;

    def update(self,word,value_,type="str"):
        self.all[word] = (value_,type);

    def remove(self,word):
        del self[word];

    def draw(self,sc):
        j = 1;
        for i in self.all.keys():
            if self.all[i][1] == "str":
                sc.update_word(93,j,"{:<15s}:{}".format(i,self.all[i][0]));

            # 以进度条的形式显示数据0.01~1.00
            if self.all[i][1] == "float":
                sc.update_word(93,j,"{:<15s}:{:>10s}<".format(i,
                    ("█"*int(self.all[i][0]*10//1))+
                    ("▌"*int(self.all[i][0]*10*10%10//5))
                ));
            j += 1;
    
    @staticmethod
    def output_description(sc,msg):
        sc.update_word(93,22,msg,byte_len=2);

    @staticmethod
    def clear_description(sc):    
        for i in range(6):
            sc.update_word(93,22+i,"　"*13,byte_len=2)
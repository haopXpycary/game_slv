from defs.player import player
from const_data import cstd

def init_player():
    plr = player()
    plr.initBaseMsg("xpycary","male","54")
    plr.initPlace(0,0,cstd.Right,">")
    plr.initBaseAttributes(baseHealth=20,baseProtect=0,baseAttack=10,baseMagic=10)
    plr.initDevelopableAttributes(5,3,3,3)
    plr.initLevel()
    plr.initSkills([0,0,0,0,0])
    plr.initBackpack()
    plr.initArmor()
    plr.initSatisfaction()
    plr.statisticsAttributes();

    return plr
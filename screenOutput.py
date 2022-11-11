from drawScreen import sc;
from msgContorl import msgOutputControl;
from defs.player import player,ply


msgoc = msgOutputControl();

plr = player()
plr.initBaseMsg("xpycary","male","54")
plr.initPlace(0,0,ply.Right,">")
plr.initBaseAttributes(baseHealth=20,baseProtect=0,baseAttack=10,baseMagic=10)
plr.initDevelopableAttributes(5,3,3,3)
plr.initLevel()
plr.initSkills([0,0,0,0,0])
plr.initBackpack()
plr.initArmor()
plr.initSatisfaction()
plr.statisticsAttributes();

msgoc.update("Name",plr.name);
msgoc.update("x,y","%d,%d" %(plr.x,plr.y));
msgoc.update("Health",plr.health/plr.maxHealth,"float");
msgoc.update("Protect",plr.protect);
msgoc.update("Attack",plr.attack);
msgoc.update("Magic",plr.magic/plr.maxMagic,"float");
msgoc.update("Satisfaction",plr.satisfaction/plr.maxSatisfaction,"float");
msgoc.update("Level",plr.level);
msgoc.update("Exp",plr.exp/ply.level_up_need_exp(plr.level),"float");

msgoc.draw(sc);
sc.show();
input();
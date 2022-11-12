from const_data import cstd

class basePlayer:
    def initBaseMsg(self,name,sex=cstd.Undefine,age=cstd.Undefine):
        self.name = name
        self.sex  = sex
        self.age  = age
        
class levelSystemMixIn(basePlayer):
    def initLevel(self,level=1,experience=0):
        self.level = level
        self.exp = experience

    def initDevelopableAttributes(self,developableHealth,developableProtect,developableAttack,developableMagic):
        self.developableHealth  = developableHealth
        self.developableProtect = developableProtect
        self.developableAttack  = developableAttack
        self.developableMagic   = developableMagic

    def addExp(self,experience):
        self.experience += experience
        while self.experience >= cstd.level_up_need_exp(self.level):
            self.level += 1
            self.baseHealth  += self.developableHealth
            self.baseProtect += self.developableProtect
            self.baseAttack  += self.developableAttack
            self.baseMagic   += self.developableMagic

# 移动系统
class moveSystemMinIn(basePlayer):
    # 初始化玩家位置信息
    # @param x,y: 玩家初始坐标
    # @param headfor: 玩家朝向
    # @param pic: 玩家的图像
    def initPlace(self,x,y,headfor,pic):
        self.x = x
        self.y = y
        self.headfor = headfor
        self.pic = pic

    # 移动
    def walk(self,headfor):
        self.headfor = headfor
        if headfor == cstd.Right:
            self.x += 1
        elif headfor == cstd.Left and self.x >= 1:
            self.x -= 1
        elif headfor == cstd.Down:
            self.y += 1
        elif headfor == cstd.Up and self.y >= 1:
            self.y -= 1

    # 传送
    def tp(self,x,y):
        self.x,self.y = x,y

class  backpackSystemMixIn(basePlayer):
    def initBackpack(self):
        self.backpack = dict();
        
    def addThing(self,thing,number=1):
        if thing.ID in self.backpack.keys():
            self.backpack[self.backpack.key.index(thing)] += number
        else:
            self.backpack[thing] = number
    
    def removeThing(self,thing,number=1):
        if self.haveThing(thing,number):
            self.backpack[self.backpack.key.index(thing)] -= number
            
    def haveThing(self,thing,number=1):
        if thing in self.backpack.keys():
            if self.backpack[self.backpack.key.index(thing)] >= number:
                return True
        return False

class armorSystemMixIn(basePlayer):
    def initArmor(self):
        # self.equipmentBar = [headbar,necklacebar,breastplateBar,pantsBar,shoeBar]
        self.equipmentBar = [0,0,0,0,0]
        self.equipmentProvidedAttack  = 0
        self.equipmentProvidedHealth  = 0
        self.equipmentProvidedMagic   = 0
        self.equipmentProvidedProtect = 0
        self.equipmentProvidedRestoreHealth = 0
        self.equipmentProvidedRestoreMagic  = 0
        
    def wearThing(self,armor):
        if self.equipmentBar[armor.protectionType]:
            self.addThing(self.equipmentBar[armor.protectionType])
        self.removeThing(armor)
        self.equipmentBar[armor.protectionType] = armor
        self._statisticsEquipmentProvided()

    def putDownThing(self,thing,armor):
        if armor in self.equipmentBar:
            del self.equipmentBar[self.equipmentBar.index(armor)]
            self.addThing(armor)

    def _statisticsEquipmentProvided(self):
        for i in self.equipmentBar:
            if not i: continue;
            self.equipmentProvidedAttack  = i.providedAttack
            self.equipmentProvidedHealth  = i.providedHealth
            self.equipmentProvidedMagic   = i.providedMagic
            self.equipmentProvidedProtect = i.providedProtect
            self.equipmentProvidedRestoreHealth = i.porvidedRestoreHealth
            self.equipmentProvidedRestoreMagic  = i.providedRestoreMagic

class layoutSystem(basePlayer):
    def handheldThing(self,weaponry):
        if self.handheld[0]:
            self.addThing(self.handheld[0])
        self.removeThing(weaponry)
        self.equipmentBar[0] = weaponry
        self.statisticsEquipmentProvided()
        
    def layoutThing(self,thing):
        if self.haveThing(thing):
            self.removeThing(thing,1)
            self.thing.layout(self.x,self.y)

class skillSystemMixIn(basePlayer):
    def initSkills(self,skills):
        # :skills = (skill_1:skill,skill_2:skill,...,skill_5:skill)
        self.skills = skills
        
    def launchSkills(self,choice):
        if self.magic >= self.skills[choice].consumedMagic:
            self.magic -= self.skills[choice].consumedMagic
            self.skill[choice].launch(self)

class attributeSystemMixIn(basePlayer):
    def initBaseAttributes(self,baseHealth,baseProtect,baseAttack,baseMagic):
        self.baseHealth  = baseHealth
        self.baseProtect = baseProtect
        self.baseAttack  = baseAttack
        self.baseMagic   = baseMagic
        
    def addHealth(self,number):
        if self.health + number <= self.maxHealth:
            self.health += number
        else:
            self.health = self.maxHealth

    def lowerHealth(self,number):
        self.health -= number
        
    def addMagic(self,number):
        if self.health + number <= self.maxMagic:
            self.magic += number
        else:
            self.magic = self.maxMagic

    def lowerMagic(self,number):
        self.magic -= number

class satisfactionSystemMixIn(basePlayer):
    def initSatisfaction(self):
        self.satisfaction = 100
        self.maxSatisfaction = 100
        
    def addSatisfaction(self,number):
        self.satisfaction += number
        if self.satisfaction > self.maxSatisfaction:
            self.satisfaction = self.maxSatisfaction;

    def lowerSatisfaction(self,number):
        self.satisfaction -= number

class player(levelSystemMixIn,moveSystemMinIn,backpackSystemMixIn,armorSystemMixIn,attributeSystemMixIn,skillSystemMixIn,
    satisfactionSystemMixIn):
    buffs = []
    def statisticsAttributes(self):
        self.maxHealth = self.baseHealth  + self.equipmentProvidedHealth
        self.health    = self.maxHealth
        self.maxMagic  = self.baseMagic   + self.equipmentProvidedMagic 
        self.magic     = self.maxMagic
        self.protect   = self.baseProtect + self.equipmentProvidedProtect
        self.attack    = self.baseAttack  + self.equipmentProvidedAttack 
        self.restoreHealth = self.equipmentProvidedRestoreHealth
        self.restoreMagic  = self.equipmentProvidedRestoreMagic
        
    def update(self):
        pass

if __name__ == "__main__":
    sb = player()
    sb.initBaseMsg("xpycary","male","54")
    sb.initPlace(0,0,cstd.Right,">")
    sb.initBaseAttributes(baseHealth=20,baseProtect=0,baseAttack=10,baseMagic=10)
    sb.initDevelopableAttributes(5,3,3,3)
    sb.initLevel()
    sb.initSkills([0,0,0,0,0])
    sb.initBackpack()
    sb.initArmor()
    
    for i,j in vars(sb).items():
        print("%32s" %i,":",j)
    input("Input [Enter] To Exit.")
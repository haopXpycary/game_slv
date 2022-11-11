
        
    
    

class behavingPlayer_attackMixIn(basePlayer):
    def haveAttack(self):
        if self.handheld:
            self.handheld.durable -= 1
            return (self.attack,self.handheld[0].enchanting,self.handheld[0].buffTime)
        return (self.attack,0,0)
        
   
        
class behavingPlayer_armorMixIn(basePlayer):

    
   
            
        
    
        

        
class behavingPlayer_additionalMixIn(basePlayer):
    def initAdditionalAttributes(self):
        self.additionalHealth  = 0
        self.additionalMagic   = 0
        self.additionalProtect = 0
        self.additionalAttack  = 0
        self.additionalRestoreHealth = 0
        self.additionalRestoreMagic  = 0
    def initInscription(self):
        self.inscriptions = []
        
    def increaseHealth(self,number):  self.additionalHealth += number
    def decreaseHealth(self,number):  self.additionalHealth -= number
    def increaseMagic(self,number):   self.additionalMagic  += number
    def decreaseMagic(self,number):   self.additionalMagic  -= number
    def increaseAttack(self,number):  self.additionalAttack += number
    def decreaseAttack(self,number):  self.additionalAttack -= number
    def increaseProtect(self,number): self.additionalProtect += number
    def decreaseProtect(self,number): self.additionalProtect -= number
    def increaseRestoreHealth(self,number): self.additionalRestoreHealth += number
    def decreaseRestoreHealth(self,number): self.additionalRestoreHealth -= number
    def increaseRestoreMagic(self,number):  self.additionalRestoreMagic += number
    def decreaseRestoreMagic(self,number):  self.additionalRestoreMagic -= number
    def addInscription(self,inscription):
        if self.haveThing(inscription):
            self.inscriptions.append(inscription)
            self.removeThing(inscription)
            self.statisticsInscription()
        
    def removeInscription(self,inscription):
        if inscription in self.inscriptions:
            del self.inscriptions[self.inscriptions.index(inscription)]
            self.addThing(inscription)
            self.statisticsInscription()
            
    def statisticsInscription(self):
        '''
        for i in self.inscriptions:
            if i.addintionType == Health: self.additionalHealth += i.addintionValue
            elif i.addintionType == Protect: self.additionalProtect += i.addintionValue
            elif i.addintionType == Magic: self.additionalMagic += i.addintionValue
            elif i.addintionType == Attack: self.additionalAttack += i.addintionValue
            elif i.addintionType == RestoreHealth: self.additionalRestoreHealth += i.addintionValue
            elif i.addintionType == RestoreMagic: self.additionalRestoreMagic += i.addintionValue
        '''
        pass

class behavingPlayer_moneyMixIn(basePlayer):
    def initMoney(self):
        self.money = 0
    
    def addMoney(self,number): self.money += number
    def Money(self,number): self.money -= number
    

        

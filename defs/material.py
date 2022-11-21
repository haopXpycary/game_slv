class baseThing:
    def __init__(self,ID,pic):
        self.ID = ID
        self.pic = pic
        
class layoutThing(baseThing):
    events = []
    # howGet = {thing:time}
    # willGet = {thing:number}
    # {"id":"1","name":"rock","type":"material","pic":"#","color":0,"howGets":{"handbreak":15},"willGets":{"1":1},"description":"平平无奇的石头"}
    def __init__(self,def_json):
        super().__init__(def_json["id"],def_json["pic"])
        self.type = "layoutThing"
        self.howGets    = def_json["howGets"]
        self.name = def_json["name"]
        self.color     = def_json["color"]
        self.couldPass  =  def_json["couldPass"]
        self.willGet   = def_json["willGets"]
        self.event = []

    def addEvent(self,event):
        self.events.append(event)
    
    def layout(self,x,y):
        self.x = x
        self.y = y
        return self

    def debug(self,layout):
        self.layout = layout

if __name__ == "__main__":
    pass
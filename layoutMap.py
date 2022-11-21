import random
import copy

class layoutMap:
    def __init__(self,thing):
        self.map = []
        for i in range(20):
            self.map.append(copy.deepcopy(thing["rock"]).layout(random.randint(0,40),random.randint(0,20)))
        
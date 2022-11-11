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
            if self.all[i][1] == "float":
                sc.update_word(93,j,"{:<15s}:{:>10s}<".format(i,
                    ("█"*int(self.all[i][0]*10//1))+
                    ("▌"*int(self.all[i][0]*10*10%10//5))
                ));

            j += 1;
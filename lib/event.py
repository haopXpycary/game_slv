class _event:
    e = dict();
    def add_event(self,who,do,what=None):
        if do in self.e:
            self.e[do].append((who, what));
        else:
            self.e[do] = [(who, what),]

    def remove_event(self,who,do,what=None):
        if do in self.e:
            if what == "lasted":
                if self.e[do]:
                    self.e[do].pop()
            else:
                if tuple(who,what) in self.e[do]:
                    self.e[do].remove((who,what))
    
    def get_all_event(self):
        return self.e

event = _event();

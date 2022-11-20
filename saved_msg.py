import pickle
import shutil
import os

class savedMsg:
    def __init__(self):
        self.target_file_name = "res/data.pkl"
        self.target_file_name_bak = "res/data_bak.pkl"
        # 行为线，每次保存、更新数据自增1
        self.behaverline = "behaverline";
        self._get_data_from_file();

    def _get_data_from_file(self):
        try:
            self.saved_file = open(self.target_file_name,"rb");
        except FileNotFoundError:
            self.saved_file = open(self.target_file_name,"ab");
        try:
            self.baked_file = open(self.target_file_name_bak, "rb");
        except FileNotFoundError:
            self.baked_file = open(self.target_file_name_bak, "ab");

        try:
            self.data = pickle.load(self.saved_file);
        except EOFError:
            self.data = dict();
        try:
            self.data_bak = pickle.load(self.baked_file);
        except EOFError:
            self.data_bak = dict();

        self.saved_file.close();
        self.baked_file.close();
        # 初始化行为线
        if not self.data.get(self.behaverline, False): self.data[self.behaverline] = 0;
        if not self.data_bak.get(self.behaverline,False): self.data_bak[self.behaverline] = 0;
        
        # 判断当前文件与备份文件的新旧
        if not self._test_datafile_behaverline():
            self.data = self.data_bak;

    def saved(self):
        with  open(self.target_file_name,"wb") as f:
            pickle.dump(self.data,f);
        shutil.copyfile(self.target_file_name, self.target_file_name_bak)

    # @return:: True:数据文件较新 False:备份文件较新
    def _test_datafile_behaverline(self):
        if self.data[self.behaverline] < self.data_bak[self.behaverline]:
            return False
        return True

    def __getitem__(self,name):
        return self.data.get(name, None);

    def __setitem__(self,name,val):
        self.data[name] = val;
        # 更新行为线
        self.data[self.behaverline] += 1;
        self.saved();

    def __delitem__(self,name):
        del self.data[name];
        self.saved();

if __name__ == "__main__":
    smsg = savedMsg();
    # smsg["dddd"] = "cc";
    del smsg["dddd"]
    print(smsg["dddd"])
    smsg.saved()
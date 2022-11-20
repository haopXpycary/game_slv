import sys
import time
import threading
import os
import traceback

class relogger:
    def __init__(self,output=None):
        if not output: output = sys.stdout
        self.output = output;

    def logout(self,*msg,getframe=None):
        self.name = os.path.splitext(os.path.split(traceback.extract_stack()[-2][0])[1])[0] + '.' + traceback.extract_stack()[-2][2]
        self.output.write(time.strftime(f"<{self.name}>[%y-%m-%d %H:%M:%S] "))
        if getframe:
            self.output.write("(Line: %-3s Function: %-12s Filename: %s) " %(getframe.f_lineno,getframe.f_code.co_name,getframe.f_code.co_filename[getframe.f_code.co_filename.rfind("\\")*getframe.f_code.co_filename.rfind("/")*(-1)+1:]));
        for i in msg:
            if i == "|": self.output.write("\n\t\t")
            self.output.write(str(i));
            self.output.write(" ");
        self.output.write("\n");
        self.output.flush();

if __name__ == "__main__":
    import os
    logger = relogger();
    logout = logger.logout

    logout("hello");
    logout("world",getframe=sys._getframe());
    def cc():
        logout("3333",getframe=sys._getframe());
    cc();

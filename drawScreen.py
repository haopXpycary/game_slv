from lib.screenControl import col,screenControl

MAXSCRX = 120;
MAXSCRY = 30;

sc = screenControl(MAXSCRX+1,MAXSCRY+1);
sc.clear();

for i in range(1,MAXSCRX):
    sc.update(i,0,'-');
    sc.update(i,MAXSCRY,'-');
    sc.update(i,MAXSCRY-2,'-');
    if i % 4 == 0:
        sc.update(i,MAXSCRY,'+');
        sc.update(i,MAXSCRY-1,'|');
        sc.update(i,MAXSCRY-2,'+');

for i in range(1,MAXSCRY):
    sc.update(0,i,'|');
    sc.update(MAXSCRX,i,'|');

for i in range(1,MAXSCRY):
    sc.update(MAXSCRX-28,i,'|');

for i in range(MAXSCRX-28,MAXSCRX):
    sc.update(i,MAXSCRY-9,'-');

sc.update(0,0,'+');
sc.update(MAXSCRX,0,'+');
sc.update(0,MAXSCRY,'+');
sc.update(MAXSCRX,MAXSCRY,'+');
sc.update(0,MAXSCRY-2,'+');
sc.update(MAXSCRX,MAXSCRY-2,'+');
sc.update(MAXSCRX-28,MAXSCRY-2,'+');
sc.update(MAXSCRX-28,MAXSCRY-9,'+');
sc.update(MAXSCRX-28,0,'+');
sc.update(MAXSCRX,MAXSCRY-9,'+');

# sc.update(1,1,'█',col.Red);
# sc.update(91,27,'▌',col.Red);
sc.show();
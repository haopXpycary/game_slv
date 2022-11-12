from const_data import cstd

# 绘制边框
def draw_screen_framework(sc):
    for i in range(1,cstd.MAXSCRX):
        sc.update(i,0,'-');
        sc.update(i,cstd.MAXSCRY,'-');
        sc.update(i,cstd.MAXSCRY-2,'-');
        if i % 4 == 0:
            sc.update(i,cstd.MAXSCRY,'+');
            sc.update(i,cstd.MAXSCRY-1,'|');
            sc.update(i,cstd.MAXSCRY-2,'+');

    for i in range(1,cstd.MAXSCRY):
        sc.update(0,i,'|');
        sc.update(cstd.MAXSCRX,i,'|');

    for i in range(1,cstd.MAXSCRY):
        sc.update(cstd.MAXSCRX-28,i,'|');

    for i in range(cstd.MAXSCRX-28,cstd.MAXSCRX):
        sc.update(i,cstd.MAXSCRY-9,'-');

    sc.update(0,0,'+');
    sc.update(cstd.MAXSCRX,0,'+');
    sc.update(0,cstd.MAXSCRY,'+');
    sc.update(cstd.MAXSCRX,cstd.MAXSCRY,'+');
    sc.update(0,cstd.MAXSCRY-2,'+');
    sc.update(cstd.MAXSCRX,cstd.MAXSCRY-2,'+');
    sc.update(cstd.MAXSCRX-28,cstd.MAXSCRY-2,'+');
    sc.update(cstd.MAXSCRX-28,cstd.MAXSCRY-9,'+');
    sc.update(cstd.MAXSCRX-28,0,'+');
    sc.update(cstd.MAXSCRX,cstd.MAXSCRY-9,'+');

# sc.update(1,1,'█',col.Red);
# sc.update(91,27,'▌',col.Red);
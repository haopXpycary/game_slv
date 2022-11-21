def draw_map(sc, plr, map):
    sc.update(plr.x, plr.y, plr.pic)
    for i in map:
        sc.update(i.x, i.y, i.pic)

def clear_map(sc, plr):
    sc.update(plr.x, plr.y, " ")

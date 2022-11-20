def draw_map(sc, plr):
    sc.update(plr.x, plr.y, plr.pic)

def clear_map(sc, plr):
    sc.update(plr.x, plr.y, " ")

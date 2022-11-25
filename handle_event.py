def handle_event(event,msgoc,sc,logout=None):
    if not logout: logout = lambda *L:None;
    i = event.get_all_event();
    # logout("event.get_all_event()>i: ",i);

    # j:事件名，k事件名对应的事件列表(发起者1，被发起者1),(发起者2，被发起者2),...
    for j,k in zip(i.keys(),i.values()):
        for l in k:
            if j == "touch":
                if len(l) == 2:
                    msgoc.output_description(sc,l[1].description)
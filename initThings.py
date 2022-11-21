from demjson import decode

from defs.material import layoutThing

def initial_material(thing,logout=None):
    if not logout: logout = lambda *L:None;
    material_json_file = open(r"defs/res/material.json","r");

    for i in material_json_file.readlines():
        material_json = decode(i);
        logout(material_json);
        mate = layoutThing(material_json);
        
        thing[mate.name] = mate;
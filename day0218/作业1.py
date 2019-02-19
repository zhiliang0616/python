def Method(curentclass,parentclass,attrdict):
    dictclss={}
    for k,v in attrdict.items():
        if not k.startswith("__"):
            dictclss[curentclass.lower()+k.lower()]=v
            if k.startswith("temp"):
                dictclss.pop(curentclass.lower()+k.lower())
    print(dictclss)
    return type(curentclass,(),attrdict)
class NPC(metaclass=Method):
    Name = "zzy"
    SPEED=10
    tempage=20





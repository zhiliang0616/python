import types
class Person(object):
    '''动态添加类方法'''
    def __init__(self,_name):
        self.name=_name
"动态添加一个类方法"
@classmethod
def desc(cls):
    return cls.__doc__
Person.de=desc
print(Person.de())
"动态添加一个实例方法"
def setname(self,newname):
    self.name=newname
p=Person("zzy")
p.setn=types.MethodType(setname,p)
p.setn("zzz")
print(p.name)
"动态添加一个静态方法"
@staticmethod
def getname():
    return p.name

Person.getn=getname
print(Person.getn())

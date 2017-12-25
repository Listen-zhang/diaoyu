class jicheng:
    def aa(self):
        print("123123")
    def __init__(self):
        print("jicheng")
class jichang1:
    def aa(self):
        print("123123213131")
    def __init__(self,a):
        print("jicheng1",a)
class jicheng2(jichang1,jicheng):
    def __init__(self,a):
        print("jicheng2")
        jichang1.aa(self)
d = jicheng2("123")



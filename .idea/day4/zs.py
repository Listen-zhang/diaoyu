# import  types
#
# def fe(n):
#     print("fe:22")
#     if type(n) == types.FunctionType:
#          return n()+22
#     return n+22
# def s(n):
#     print("s30")
#     if type(n) == types.FunctionType:
#         return n()+30
#     return n+30
#
# @fe
# @s
# def di ():
#     print("di 20")
#     return 20
#
#
# print(int(di))
class a:
    def __myname(self,ff=None):
        self.ff = ff
    def __init__(self,c=None):
         self.c = c
    def b(self,name):
        print(name,self.c,self.ff)

b = a()
b.ff="456"
b.c="456"
b.b("13")


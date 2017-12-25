# f = open("G:/file/a/test.txt")
# of = open("G:/file/b/test.txt","w")
# for line in f:
#     of.write(line)
# print("ok")
# f = open("G:/file/a/pic.bmp",'rb')
# of = open("G:/file/b/pic.bmp",'wb')
# # of.write(f.read())
# f.seek(0,2)
# size = f.tell()
# print(round(size/1024/1024,2),"MB")
# f.seek(0,0)
# ofSize = 0
# while True:
#     if ofSize>size:
#         break
#     str = f.readline(1024*10)
#     of.write(str)
#     of.flush()
#     ofSize += 1024*10
# print("ok")

import pickle,pprint
class Person:
    name = None
    age = None
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return ("name:{0},age:{1}".format(self.name,self.age))
p = Person('zs',18)
f = pickle.dump(p,open("d:/dw/person.data",'wb'))
pprint.pprint(pickle.load(open("d:/dw/person.data",'rb')))




# class Aex(Exception):
#     def __str__(self):
#         return "Aex"
#
# class Bex(Exception):
#     def __str__(self):
#         return "Bex"
# class Cex(Exception):
#     def __str__(self):
#         return "Cex"
#
# n = int(input("请输入整数"))
# try:
#     if n == 1:
#         raise Aex()
#     if n == 2:
#         raise Bex()
#     if n == 3:
#         raise Cex()
#     print("ok")
# except(Aex,Bex,Cex) as e:
#     print(e)

# import shutil
#
# shutil.copytree("G:/file/a","G:/file/c")
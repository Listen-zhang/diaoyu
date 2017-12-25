f = open("D:/游戏/a/a.txt");
out= open("D:/游戏/b/b_1.txt","w");
for i in f:
    out.write(i)
f = open("D:/游戏/a/xin.jpg","rb");
out= open("D:/游戏/b/xinixn.jpg","wb");
out.write( f.read())
f.seek(0,2)
print(f.tell())


# class stu:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return ("名字{0}年龄{1}".format(self.name, self.age))
# hh = stu("zhang",16)
# print(hh)
#
# import shutil
# #复制文件
# # shutil.copyfile('listfile.py', 'd:/test.py')
# #复制目录
# shutil.copytree('D:/游戏/a', 'D:/游戏/b/a')
# #其余可以参考shutil下的函数
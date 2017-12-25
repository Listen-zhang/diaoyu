import os
import shutil
import pymysql
print("Microsoft Windows [版本 10.0.15063]"+
"(c) 2017 Microsoft Corporation。保留所有权利。")
def help(cmd=None):
    if cmd is None:
        with   open("../mycmd/help.txt", "r", encoding="utf-8") as f:
         for i in f:
          print(i,end='')
    else:
      with  open(cmd+".txt", "r", encoding="utf-8") as f:
        for i in f:
            print(i, end='')
def cd(cmd=None):
    if cmd is None:
     print("指令无效")
    else:
     os.chdir(cmd)
def dir(cmd =None):
     for i in  os.listdir(cmd):
         print(i)
def remove(cmd=None):
    if cmd is None:
        print("...")
    else:
        os.remove(cmd)
        print("删除成功")
a={"help":help,"cd":cd,"dir":dir,"remove":remove}
while 1==1:
    kay=input(os.path.dirname(os.getcwd())+"-->")
    if kay=="esc":
        break
    keyAndOption = kay.split(' ')
    print(keyAndOption)
    cmd = a[keyAndOption[0]]
    if(len(keyAndOption)==1):
       cmd()
    else:
       cmd(keyAndOption[1])
       # print(d.read())

# os.listdir(dirname)：列出dirname下的目录和文件
# os.getcwd()：获得当前工作目录
# os.curdir:返回当前目录（'.')
# os.chdir(dirname):改变工作目录到dirname
# os.path.isdir(name):判断name是不是一个目录，name不是目录就返回false
# os.path.isfile(name):判断name是不是一个文件，不存在name也返回false
# os.path.exists(name):判断是否存在文件或目录name
# os.path.getsize(name):获得文件大小，如果name是目录返回0L
# os.path.abspath(name):获得绝对路径
# os.path.normpath(path):规范path字符串形式
# os.path.split(name):分割文件名与目录（事实上，如果你完全使用目录，它也会将最后一个目录作为文件名而分离，同时它不会判断文件或目录是否存在）
# os.path.splitext():分离文件名与扩展名
# os.path.join(path,name):连接目录与文件名或目录
# os.path.basename(path):返回文件名
# os.path.dirname(path):返回文件路径
# os.remove(dir) #dir为要删除的文件夹或者文件路径
# os.rmdir(path) #path要删除的目录的路径。需要说明的是，使用os.rmdir删除的目录必须为空目录，否则函数出错。
# os.path.getmtime(name) ＃获取文件的修改时间
# os.stat(path).st_mtime＃获取文件的修改时间
# os.stat(path).st_ctime #获取文件修改时间
# os.path.getctime(name)#获取文件的创建时间
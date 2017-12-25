
'''
面向对象编程
  类
     继承：多继承
     类中所有的__开头的方法都是内置的来自于父类
  对象
     创建对象和调用函数一样
  方法
      类方法
      对象方法
      构造方法
      静态方法
'''


class person:
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name

    def show(self, s):  # this  show(s){}
        print(self.__first_name)
        print(self.__last_name)
        print(self.full_name, s)  # print(propterty(full_name),s)

    @property
    def full_name(self):
        return self.__first_name + '.' + self.__last_name

    @full_name.setter
    def full_name(self, full_name):
        self.__first_name = full_name[:full_name.index(".")]
        self.__last_name = full_name[full_name.index(".") + 1:]


p = person("wang", "wu")
p.show("haha")
print(p.full_name)
p.full_name = "li.si"
p.show("heihei")


'''
函数：独立定义，独立调用
def foo():
    pass
foo()
方法：依赖定义，依赖调用
A
  def foo()
     pass
A().foo()

学习函数
    语法
        def  函数名称(参数):
             #函数体
    参数：普通
          关键参数
          动态参数

 1.
变量作用域
    全局  本地  闭包  局部

    什么情况下产生新的作用域
        def
        class
2.
函数作为参数：回调
3.
函数返回值可以有多个
------------------------------------------
函数 装饰  @



class method object



'''
# def foo(n,m):
#     print("第一个参数是{0}，第二个参数是{1}".format(n,m))
# foo(5,4)
#
# def foo2(n=0,m=0):
#     print("第一个参数是{0}，第二个参数是{1}".format(n,m))
# foo2(m=5,n=4)
# foo2()
# def foo3(*args):
#     sum=0
#     for n in args:
#         sum = sum + n
#     return  sum
# rs=foo3(1)
# print(rs)
# rs=foo3(1,2,3,4)
# print(rs)
#
# abc="g" #Global
# #nonlocal
# def testscope():
#     a="aaa"
#     def ts():
#         nonlocal a
#         a="bbb"
#         print(a)
#     print(a)
#     ts()
#     print(a)
#     # ts()
# testscope()
# def ts():
#     a="aa"
#     if True :
#         b ="bb"
#     print(a)
#     print(b)
# ts()

# def selectone(data,r):
#     for a in data :
#         if r(a) :
#             return a
#
# def guizi(d):
#     return d % 3 == 0
# def xinguizi(d):
#     return d % 7 == 0
# print(selectone([1,2,4,5,6,7,8.9],xinguizi))
# def daxiao(n,n1):
#     if n > n1 :
#         n,n1=n1,n
#     return n,n1
# a,b=daxiao(7,3)
# print(a,b)

# 装饰
# 火锅
# 麻辣锅底  金品肥牛 极品羊肉  什么蔬菜双拼

import types


def jingpinfeiniu(n):
    print("金品肥牛：￥38")
    if type(n) == types.FunctionType:
        return n() + 38
    return n + 38


def shucai(n):
    print("什么蔬菜双拼:$7")
    if type(n) == types.FunctionType:
        return n() + 7
    return n + 7


@shucai
@jingpinfeiniu
def mala():
    print("麻辣锅底：$12")
    return 12


# shcai(jingpinfeiniu(mala))

# qian=shucai(jingpinfeiniu(mala()))

print("狗消费：" + str(mala))


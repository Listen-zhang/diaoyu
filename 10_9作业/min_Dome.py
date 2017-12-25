#1.两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵：
# 第一种方法
X = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]
Y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

# 迭代输出行
for i in range(len(X)):
    # 迭代输出列
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]

for r in result:
    print(r)

#第二种方法
x = [[12,7,3],
        [4,5,6],
        [7,8,9]]

y = [[5,8,1],
        [6,7,3],
        [4,5,9]]
z= []
for i in range(3):
    z.append([])
for i in range(3):
    for j in range(3):
        z[i].append(x[i][j]+y[i][j])
print(z)
# 2.使用 random 随机生成两个矩阵：
# 第一种方法
import random
print("random")
i = []
for a in range(9):
    randArray = random.random()
    randArray = int(randArray*100)
    i.append(randArray)
print(i)


#第二种方法
import random
random.randint(1,100)

#3.有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# 第一种方法
d = [1, 2, 3, 4]
def getnum(num, digit, length):
    num1 = num

    for i in range(len(digit)):
        num = num1 * 10 + digit[i]
        if length == 3:
            yield num
        elif length < 3:
            for j in getnum(num, digit[:i] + digit[i + 1:], length + 1):
                yield j


digit = list(getnum(0, d, 1))
print("%r 共可以组成%d个三位数字 " % (d, len(digit)))
print("它们是:%r" % digit)

nlist=[]
for i in range(1,5):
    for j in range(1,5):
        for z in range(1,5):
            if i != j and j !=z and i != z :
                x =[i,j,z]
                if x not in nlist:
                    nlist.append(x)
for x in nlist:
    print(x)
#print [(x, y, z) for x in xrange(1,5) for y in xrange(1,5) for z in xrange(1,5) if ((x != y) and (y != z) and (x != z))]
# 4.一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
# 第一种方法
for i in range(1, 1000):
    for j in range(1, 1000):
        for k in range(1, 1000):
            if (i + 100) == j * j and (i + 268) == k * k:
                print(i)

#第二种方法 优化
import math

for z in range(10000):
    x = int(math.sqrt(100 + z))
    y = int(math.sqrt(268 + z))
    if (x * x == (100 + z)) and (y * y == (z + 268)):
        print(z)

#5.输入三个整数x,y,z，请把这三个数由小到大输出
def sort_int(a, b, c):
    L = [a, b, c]
    L.sort()
    return L

x, y, z = sort_int(100, 10, 1)
print(x, y, z)

# 6.斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
# 第一种方法
# 获取用户输入数据
nterms = int(input("你需要几项？"))

# 第一和第二项
n1 = 0
n2 = 1
count = 2

# 判断输入的值是否合法
if nterms <= 0:
    print("请输入一个正整数。")
elif nterms == 1:
    print("斐波那契数列：")
    print(n1)
else:
    print("斐波那契数列：")
    print(n1, ",", n2, end=" , ")
    while count < nterms:
        nth = n1 + n2
        print(nth, end=" , ")
        # 更新值
        n1 = n2
        n2 = nth
        count += 1

# 第二种方法
num = int(input("输入一个整数："))
f1=0
f2=1
if num <=0:
    print("请输入一个正整数！")
elif num==1:
    print("斐波拉契数列：%d"%f1)
else:
    print("斐波拉契数列：",end="")
    print(f1,f2,end=" ")
    for n in range(1,num-1):
        f=f1+f2
        f1,f2=f2,f
        print(f,end=" ")

#7.将一个列表的数据复制到另一个列表中。
#第一种方法
a = [1,2,3,4]
b = []
for i in a:
    b.append(i)
print(b,a)
print(id(b),id(a))

#第二种方法
import copy

a = [1,2,3,4]
b = a
d = copy.copy(a)
b[0] = 'b'
print(a,b,d)
print(id(a),id(b),id(d))





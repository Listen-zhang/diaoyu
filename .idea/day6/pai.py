class person:
    def __init__(self,name=None,age=None):
        self.name =name
        self.age=age
    def __str__(self):
        return "我是{0}，今年{1}岁".format(self.name,self.age)
    def __add__(self, other):
        return person(self.name+other.name,self.age+other.age)
    def __lt__(self, other):
        if self.name == other.name:
            return  other.age < self.age
        else:
            return self.name< other.name



p=person(name="张三",age=19)
p1=person(name="张三",age=19)
print(p+p1)
ps=[person("zhangsan",19),person("lisi",16),person("zhangsan",21),person("wangwu",23),]
print("-----------未排序-----------------")
for p1 in ps:
    print(p1)
print("-----------排序后-----------")
for p1 in sorted(ps):
    print(p1)

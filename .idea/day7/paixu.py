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
            return self.name.encode("gbk")< other.name.encode("gbk")




ps=[person("张三",19),person("李四",16),person("张三",21),person("王五",23),]
print("-----------未排序-----------------")
for p1 in ps:
    print(p1)
print("-----------排序后-----------")
for p1 in sorted(ps):
    print(p1)

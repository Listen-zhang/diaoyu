class Animal:
    def eat(self):
        print("")
class Dog(Animal):
    def cry(self):
        print("Wang!Wang！")
    def eat(self):
        print("I love meat")

class Cat(Animal):
    def cry(self):
        print("Miao!Miao！")
    def  catching(self):
        print("")
    def eat(self):
        print("I love fish")
dog = Dog()
dog.eat()
dog.cry()
print( dir(dog))
print("dog是Dog的实例吗？",isinstance(dog,Dog))
print("狗是动物的实例吗？",isinstance(dog,Animal))
cat = Cat()
cat.cry()
cat.eat()
print( dir(cat))
print(isinstance(cat,Cat))
print("狗是猫的实例吗？",isinstance(dog,Cat))

class Person(object):
    def __init__(self, name, age=18):
        self.name = name
        self.__age = 18

    @property
    def age(self):
        return self.__age


xm = Person('xiaoming')  # 定义一个人名小明
print(xm.age)  # 结果为18
# xm.age = -4  # 报错无法给年龄赋值
xm.name = 'a'
print(xm.name)

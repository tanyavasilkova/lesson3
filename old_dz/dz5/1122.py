class Dog:
    paws = 4
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def bark(cls, times):
        print('The dog barks {} times and has {} paws'.format(
        times, cls.paws))

    @staticmethod
    def get_description():
        return 'Собака - млекопитающее с 4 лапами и хвостом. Умеет лаять'
    def temp(self):
        print('Im temp')


print(Dog.bark(3))

d = Dog('Lola', 12)
d.paws = 15
print(d.paws)
print(d.bark(7))

print(Dog.temp())










import datetime







class MyInterval:
    class_end = datetime.datetime.now()

    def __init__(self, end=None):
        if end is None:
            self.end = self.class_end


    def get_len(self):
        return self.class_end - self.end

    def reset_get(self):
        self.class_end = datetime.datetime(1991, 1, 1)

my_int = MyInterval(datetime.datetime(2018,11,24,8,13,0))
print(my_int.class_end)
my_int.reset_get()
print(MyInterval.class_end)
print(my_int.class_end)

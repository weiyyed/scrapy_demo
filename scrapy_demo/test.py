import json
class Test_new():
    def __init__(self):
        print("-----init----")
    def __new__(cls, *args, **kwargs):
        print(hex(id(cls)))
        print("___new____")
        return object.__new__(cls) #必须要返回这个对象,对象的引用,才会执行__init__
t=Test_new()
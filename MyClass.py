class MyClass:
    num=10
    def __init__(self,v):
		
        self.v=v*MyClass.num
    def getNum(self):
        print(self.num)
		

a= MyClass(100);
#print(MyClass.v)
print(a.v)
a.getNum()
print(MyClass.num)
print(a.num)
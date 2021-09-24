#class =>collection of methods
#object =>instance of a class

class Myclass:
    "This is a class1"
    a=10
    def show(self):
       
        print("This is some text")

#direct call
print(Myclass.a)
print(Myclass.show)
print(Myclass.__doc__)


#objects
obj=Myclass()
obj.show()
print(obj.a)


#constructor -simple
class Myclass1:
    def __init__(self):
        print("This is constructor")
#creating object for print constructor
p1=Myclass1()

#parametrized constructor
class calculate:
    def __init__(self,num1,num2):
        self.a=num1
        self.b=num2
    def getdata(self):
        print("num 1 =%d ,num 2 = %d"%(self.a,self.b))

p2=calculate(10,20)
p2.getdata()




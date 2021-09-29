
#Generators 
#holds values
#yield,next

#simple 
def showvalue():
    num=1
    print("First Number")
    return num
    # num +=1
    # print("Second Number")
    # return num

#print(showvalue())

#Generators Example
def test_gen():
    num=1
    print("First Number")
    yield num
    num +=1
    print("Second Number")
    yield num
    num +=1
    print("Third Number")
    yield num

#calling 
obj=test_gen()
print(next(obj))
print(next(obj))
print(next(obj))

#Example -2
#-reverse of word
def str_reverse(word): #python
    lenght=len(word)  # 6
    #stop,start,skippping value , 3 , -1,-1 => 3-1=2 -1=1
    for k in range(lenght-1,-1,-1): 
        yield word[k]

#calling with loop
for i in str_reverse("Python"):
    print(i)


#Decorators - calling a function or a class as an argument
def show(msg):
    print(msg)

#simple
show("Hello World")

#calling function as an argument
p1=show
p1("Hello Python")

#example
def incre(num):
    return num+1
def decr(num):
    return num-1

def operator(funcname,num):
    result=funcname(num)
    return result

#calling
print(incre(5))
#decorators
print(operator(incre,8))
print(operator(decr,6))
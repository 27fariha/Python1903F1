#holds data in sequence
#next() , __next__()
#stopIteration

number_list=[1,2,3,4,5,6]

#--simple loop
for i in number_list:
    print(i)

#iteration
#convert list iterator
test_list=iter(number_list)
print(next(test_list))
print(test_list.__next__())
print(test_list.__next__())
print(test_list.__next__())
print(test_list.__next__())
print(test_list.__next__())#6


#example 2
class PowerofTwo:
    def __init__(self,max=0):
        self.maximum=max
    def __iter__(self):
        self.number=0
        return self
    def __next__(self):
        if self.number <= self.maximum:
            output=2**self.number
            self.number+=1
            return output
        else:
            raise StopIteration

p=PowerofTwo(8)
number=iter(p)
print(next(number))
print(next(number))
print(next(number))
print(next(number))
print(next(number))
print(next(number))
print(next(number))
print(next(number))
print(next(number))
print(next(number))
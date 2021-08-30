import datetime
import math
from math import pi
import sys
from sys import path
#loops
#for,while,do-while,foreach

#for(int i =0;i<=10;i++){print}
for i in range(30):  #0-29
    print(i)

#while
count =0
while(count < 10):
    count=count+1 # 1 = 1+1 =>2
    print(count) 


#if else
if(count == 0):
    print("Yes")
else:
    print("No")

#if else if
num=6
if(num == 1 ):
    print("One")
elif(num ==2):
    print("Two")
elif(num ==3):
    print("Three")
else:
    print("Nothing to Match")

#loops
for i in range(2,30,3):
    print(i)

#list print
a=['wadood', 'haider', 'zubair', 'naeem', 'Hammad', 'sana', 'ayesha', 'abc', 'haris']
for x in a:
    print(x)


#loop with else block
count1=0
while (count1<3):
    count1=count1+1
    print(count1)
else:
    print("End Loop")

#pass keyword
""" while True:
    print("Hi")
    pass """


#print current datetime
time=datetime.datetime.now()
print(time)


#print value of pi =4.142

pi = math.pi
print(pi)

#direct calling 
print(pi)


#calling sys lib
print(sys.path)
print(path)
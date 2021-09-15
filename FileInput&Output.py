import os
#mode: w =write,create new 
#r= read
#a=append /write
#b=binary mode

#create file
f=open('data.txt','w') 
f.write("Hello World \n")
f.write("This is Python Programming")
f.close()

#location
print(os.getcwd())

#read file 
text=open('data.txt','r')#by default read mode
t1=text.read()
print(t1)

#read single line
f1=open('data.txt','r')
t2=f1.readline()
print(t2)

#read in binary mode
f3=open('data.txt','rb')
t3=f3.read()
print(t3)

#append 
f4=open('data.txt','a')
f4.write("\nThis is some text\n this is some text too")
f4.close()

a=open('data.txt')
b=a.read()
print(b)

#method /Function
f5=open("data.txt","wb")
print("File name is :",f5.name)
print("File No is :",f5.fileno())
#print("File close is :",f5.close())
print("Return Value :",f5.isatty())

#Next function 
file1=open("test.txt",'w')
file1.write("This is Line Number One\n")
file1.write("This is Line Number Two\n")
file1.write("This is Line Number Three\n")
file1.write("This is Line Number Four\n")
file1.write("This is Line Number Five\n")
file1.close()

file1Read=open("test.txt","r")
print("Name of the file is ",file1Read.name)
for i in range(5):
    line=next(file1Read)
    print("Line No is %d - %s" % (i,line))
file1Read.close()
#print(__file__)

#Readline 
file1Read=open('test.txt','r')
print(file1Read.readline())
print(file1Read.readline(12)) #0 to 12

#seek
file1Read.read()
file1Read.seek(3) #3
print("Seek \n :",file1Read.read())

#tell -pointer location
print(file1Read.tell())

#turncate
data1=open('data.txt','w')
data1.write("Hello \n")
data1.close()

data1=open('data.txt','r+')
data1.truncate(1)
data1.close()

data1=open('data.txt','r')
print(data1.read())


#writelines
sequence=["This is Line Number One\n","This is Line Number Two\n","This is Line Number Three\n"]
f2=open("data.txt",'w')
f2.writelines(sequence)

#saving object in file 
#int -number
a , b , c=11,22,33
#string
name="abcd"
#dict
dictt={'a':1,'b':2}
#list
lst=[1,2,3,4]

sample=open('sample.txt','w')
sample.write("a= %s ,b= %s ,c= %s \n" % (a,b,c))
sample.write("String is : %s \n "%name)
sample.write(str(dictt))
sample.write(str(lst))
sample.close()


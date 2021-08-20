#single line comment 
'''
multi line comment 
abc
'''
#string,numbers,float,list,tuples,sets,dictionaries
#datatypes 
    #int
num=123
print(num)

#check datatype
print(type(num))


#string
name="Anvcv"
print(type(name))

#concatenate
print("my name is "+name)
print("My Age is ",num)
print("My name is %s and age is %d" % (name,num))

sentence="My name is Fariha And I'm Doign Master in CS"
print(sentence[:18])
print(sentence[21:])
print(sentence[0:17])

#if sentence =="Fariha"
r="isss" in sentence   #true/false
print("values of r is =",r)
ab='Fariha' in sentence
print(ab)

#if sentence !="Fariha"
b="And" not in sentence 
print("Value of b is =",b)
abc='z' not in sentence 
print(abc)


#float
f=1.234
print(type(f))


#string Build in Methods
str1="hello.this#.is.me.pYthon.and.i.have.been.using.in.AI"
#capitalize
cap=str1.capitalize()
print(cap)
#center
sample="Apple"
cen=sample.center(40,'6')
print(cen)
#lowercase
print(str1.lower())
#uppercase
print(str1.upper())
#check string leng
print(str1.__len__())
print(len(str1))
#check lower or not 
print(str1.islower())
#max string
print(max(str1))
#min
print(min(str1))

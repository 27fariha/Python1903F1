#single line comment 
'''
multi line comment 
abc
'''

#datatypes 
    #int
num=123
print(num)

#check datatype
print(type(num))


#string
name="A"
print(type(name))

#concatenate
print("my name is "+name)
print("My Age is ",num)
print("My name is %s and age is %d"% (name,num))
sentence="My name is Fariha And I'm Doign Master in CS"
print(sentence[0:17])
ab='Fariha' in sentence
abc='z' not in sentence 
print(ab)
print(abc)


#float
f=1.234
print(type(f))


#string Build in Methods
str1="hello this is me python and i have been using in AI"
#capitalize
cap=str1.capitalize()
print(cap)
#center
sample="Apple"
cen=sample.center(30,"U")
print(cen)
#lowercase
print(str1.lower())
#uppercase
print(str1.upper())
#check string leng
print(str1.__len__())
#check lower or not 
print(str1.islower())
#max string
print(max(str1))
#min
print(min(str1))

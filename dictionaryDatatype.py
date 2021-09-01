#key value pair 
#key = value => json
# reperesent in { key1:value1,......}

#1st MEthod 
#key = string
dict1={}
dict1['Name'] ="Abc"
dict1['Age'] = 20
dict1['Batchcode']="1903F1"
print(dict1)
print(dict1['Age'])

#2nd Method
#key=int
dict2={1:'A',2:'B',3:'C',4:'D',4:'E'}
print(dict2)
print(dict2[3])

#check type 
print(type(dict1))

#lenght
print(len(dict1))
print(len(dict2))

#multiple inheritence 
students={  1:{'Name':"Haris"}, 2:{'Name':'Aiman'} ,3:{'Name':"Haider"} ,4:{'Name':"Ayesha"} }
print(students)
print(students[1])


#loop with dict
for key in dict1:
    print(key)


#key(), values() , items()

print(dict1.values()) # print Values 
print(dict2.keys())   # print keys
print(students.items())  #key value items


#remove
del students[4]
print(students)


#clear 
dict1.clear()   #remove all values 
print(dict1)

#del entire dict
#del dict1
print(dict1)


#update values 
new_dic={5:{'Name':"Hammad"},6:{'Name':"Naeem"}}
students.update(new_dic)
print(students)
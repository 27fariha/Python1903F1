#string,numbers,float,list,tuples,sets,dictionaries


#[]
#index start with 0
students=["wadood","haider","zubair","naeem","sana","ayesha"]
print(students[0])
print(students[4])
print(len(students))
print(students)

#concatenate List
finallist=[4,5]+[6,7]
print(finallist)

#print 0 to 50
#for int i=0 ;i<=50;i++
for x in range(50):
    print(x) 

#built in methods

#add values in existing list
students.append("haris")
print(students)

#add value in location
students.insert(2,"Hammad")
print(students)

#remove element from list
students.remove("naeem")
print(students)

#revers list
students.reverse()
print(students)

#remove from last 
students.pop()
print(students)

#remove from specific location
students.pop(2)
print(students)


#slicing lists
print(students[0:4]) #select first 4 data
print(students[:4])  #select through start 
print(students[2:])  # Index 2 through end 
print(students[::2]) #skip 2 values from starts 
#string,numbers,float,list,tuples,sets,dictionaries


#represent ->[]
#index start with 0
students=["wadood","haider","zubair","naeem","sana","ayesha"] #0-5
print(students[0]) #wadood
print(students[4]) #sana
print(len(students)) # 6
print(students)

#concatenate List
list1=[1,2,3,4]
list2=[5,6,7,8]
final_list=list1+list2
print(final_list)
final_list1=[1,2,3,4]+[5,6,7,8]
print(final_list1)


#built in methods

#add values in existing list
students.append("abc")
students.append("haris")
print("Append : %s "% students)

#add value in location
students.insert(4,"Hammad")
print("Insert Specific Location : %s " % students)

#remove element from list
students.remove("naeem")
print("Remove : %s "% students)

#remove from last 
students.pop()
print("Remove from Last :%s "% students)

#remove from specific location
students.pop(2)
print("Remove from location: %s"%students)


#revers list
students.reverse()
print("Reverse List :%s"%students)
print(students[0])

#slicing lists
print(students[0:6])
print(students[2:])
print(students[:4])

print(students[0:4]) #select first 4 data
print(students[:4])  #select through start 
print(students[2:])  # Index 2 through end 
print(students[::2]) #skip 2 values from starts 
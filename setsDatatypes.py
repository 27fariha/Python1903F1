# represent with {}
#store data and update 
#index - no index number in sets
#print(a[2])

#1st Method 
a ={1,2,3,4,5,6,7}
print(a)

#2nd Method
b=set((3,4,5,6,7,8))
print(b)

#check
print(type(b))

#lenght
print(len(b))

#loop with sets
for x in a:
    print(x)

#condition
if 10 in a:
    print("Yes")
else:
    print("No")

#add value 
a.add(9)
print(a)

#add 2 sets
""" z=a+b
print(z) """
a.update(b)
print(a)

#remove
#1
a.remove(9)
print(a)
#2
a.discard(3)
print(a)
#3 -delete left value
a.pop()
print(a)

#joins
set1={"a","b","c","d","e"}
set2={"b","d","u","i","w"}

#union
set3=set1.union(set2)
print(set3)

#intersection -- duplicate value
#1
set1.intersection_update(set2)
print(set1)
#2
z=set1.intersection(set2)
print(z)

#not duplicate
#1
set1.symmetric_difference_update(set2)
print(set1)
#2
u=set1.symmetric_difference(set2)
print(u)


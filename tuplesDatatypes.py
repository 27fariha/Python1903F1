#store every type of data
#values cannot b change
#represent with ()

#1st Method
fruits=("apple","watermelon","kiwi","cherry")
print(fruits)

#2nd method use with Constructor
fruits1=tuple(("apple","watermelon","kiwi","cherry"))
print(fruits1)

#access
#index start with 0
print(fruits[2])
print(fruits[1:3]) #between 
print(fruits[:3])
print(fruits[2:])


#check values
if "kiwiiii" not in fruits:
    print("Yes")
else:
    print("No")

#add values 
#step 1: first change tuple into list
#step 2: add desirable value into list
#step 3: after this change list to tuple 
y=list(fruits)
y.append("orange")
fruits=tuple(y)
print(fruits)

#access through index 
for i in range(len(fruits)): #range(5) -. 0 to 4
    print(fruits[i])

#join 2 tuple
finalList=fruits+fruits1
print(finalList)


#multiply tuples
z=fruits1*5
print(z)

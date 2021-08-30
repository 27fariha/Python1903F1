#store every type of data
#values cannot b change
#represent with ()

#1st Method
fruits=("apple","watermelon","kiwi","cherry")
print(fruits)

#2nd method use with Constructor
a=tuple((1,2,3,4,5,6,7,8))
fruits1=tuple(("apple","watermelon","kiwi","cherry"))
print(fruits1)

#access
#index start with 0
print(fruits[2]) #kiwi
print(fruits[1:3]) #between  - water.....
print(fruits[:3])  #start with zero index ...
print(fruits[2:])  # kiwi,cherry


#check values
#a=kiwiiiiii
# if (a != kiwi)
if "kiwii" not in fruits:
    print("Yes")
else:
    print("No")



#add values 
#step 1: first change/convert tuple into list
#step 2: add desirable value into list
#step 3: after this change/convert list to tuple 
#ex-1
e=list(fruits)
e.append("abc")
fruits=tuple(e)
print(fruits)

#join 2 tuple
finalList=fruits+fruits1
print(finalList)

#multiply tuples
z=fruits1*3
print(z)



#access through index 
for i in range(len(fruits)): #range(5) -. 0 to 4
    print(fruits[i])
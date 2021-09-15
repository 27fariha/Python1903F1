#syntax : [expression(variable) for item in list]

#example 1 
fruits=["Apple","Banana","Watermelon","Kiwi","Cherry"]
for x in fruits:
    print(x)

# with compre
new_List=[x for x in fruits]
print(new_List)

#Example -2 
#simple
letter=['A','B','C','D','E','F']
letter.append("abc")
for x in 'Human':
    letter.append(x)
print(letter)

#with compre
new_letter=[ a for a in 'HUMAN']
print(new_letter)

#even 
for x in range(21):
    if x%2 == 0:
        print(x)

#with compre
even=[ x for x in range(51) if x%2==0]  # 4/2 =0== 0 -yes
print(even)

#nested compre
list1=[y for y in range(51) if y%2==0 if y%5==0]
print(list1)

#uppercase
a=[x.upper() for x in fruits]
print(a)

#square number 2*2 , a*a
d=[i*i for i in range(10)]
print(d)

#if else
abc=[ x if x!="Banana" else "orange"  for x in fruits  ]
print(abc)

sentence="this is python language and it is used in ai" #string

for i in sentence:
    print(i)

vowel=[i for i in sentence if i in 'aeiou']
print(vowel)

matrix=[ [0,0,0] , [1,1,1], [2,2,2]  ]
flat_matrix=[col for row in matrix for col in row]
print(flat_matrix)
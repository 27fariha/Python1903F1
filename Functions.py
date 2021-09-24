#public myfunc(int a , string b){}

#def -> create function 

#basic function 
def show():
    print("This is some text")

#calling a function
show()

a=10
#parameterized function
def showname(name):
    print("You Entered :",name)

#calling a parameter function 
showname("Haris")
showname("Naeem")

#function with 2 parameter 
def fullname(fname,lname):
     print("Your FullName is :",fname,lname)
     print("Your FullName is :",fname+" "+lname)
     print("Your FullName is :",fname+lname)
     print("Your FirstName is %s and your LastName is : %s" % (fname,lname))

#calling
fullname("Hammad","Ahmed")

#assign value with parameter
def fullname1(lname,fname):
     print("Your FullName is :",fname,lname)

fullname1(fname="Hammad",lname="Ahmed")

#without arbitary argument
def showvalues1(one,two,subj1,subj2,subj3,subj4):
    print("First value is ",one)
    print("Second value is ",two)
    print("Third value is ",subj1,subj2,subj3,subj4)


showvalues1("Abc","1903F1","PHP","JAVA","Python","C#")


#arbitary argument with function
def showvalues(one,two,*multiple):
    print("First value is ",one)
    print("Second value is ",two)
    print("Third value is ",list(multiple))

showvalues("Abc","1903F1","PHP","JAVA","Python","C#","ASP.Net","C++")


#Keyword argument
def myfunc(a2,a1,a3):
    print("a1 :",a1)
    print("a2 :",a2)
    print("a3 :",a3)

#issue without keyword
myfunc("One","Two","Three")
#issue resolved with keyowrd
myfunc(a1="One",a2="Two",a3="Three")

#multiple arbitary argument with **
def testfunc(a1,a2,a3):
    print("a1 :",a1)
    print("a2 :",a2)
    print("a3 :",a3)

#calling 
dict1={"a2":987,"a3":"abc"}
testfunc(123,**dict1)


#using *arg , **kwarg
def studentinfo(name,batch,*subjects,**info):
    print("Student Name is :",name)
    print("Student Batch is :",batch)
    print("Students Subjects are:",list(subjects))
    print("Student info :",dict(info))

studentinfo("Ayesha","1903F1","PHP","Java","C#","Python",height=167,weight=50)


#passing a list in function
def print_list(f): # ["a","b","c"]
    for x in f:
        print(x)

fruits=["A","B","C","D","E","F"]
print_list(fruits)

#simple printing
for i in fruits:
    print(i)

#function with return keyword
def number_finder(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"    

#1st method
res=number_finder(0)
print(res)
#2nd method
print("Result is ",number_finder(3))


#[4,3,5] = 12
#sum = sum+something
def sum_list(number_list):
    sum = 0
    for i in number_list:
        sum+=i  # sum = sum + i => sum=0+5 =5 => sum = 5+7=12 => sum = 12+4=16
    return sum

res1=sum_list([5,9,7,87,95])
print(res1)
#try except -> 
#try except finally

# connection open 
# try { command }
# except { error identify}
# finally {close connection }

#try , except
x=1234
try:
    print(x)
except:
    print("No value")

#try, except ,else
# try{ open conn,command} 
# except{ error identify}
# else{ close conn}
try:
    a=235
    print(a)
except:
    print("Error")
else:
    print("nothing")

#try , except ,finally

f=open("demo.txt")
try:
    f.write("\nBasic text from sample file2")
except:
    print("Error in creating a file")
finally:
    print("Finally block")
    f.close()

#raise
x=1
if x<0:
    raise Exception("Not Allowed")

#typeError
x=123
if not type(x)is int:
    raise TypeError("Only Int values are allowed")
  
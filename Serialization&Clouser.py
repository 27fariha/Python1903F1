# process of converting structured data or object that recover it's original state 
# pickle - library for serialization data
# dump(), dumps() -> pass objects 
# load()-> read pickle object from file 
# loads()-> read pickle object from memory


#serialization 
import pickle
#perform with file system
book ={}
book['title'] = 'Python Programming'
book['page_link']='https://www.python.org/'
book['id']='1234'
book['tag']=('Python','Coding','Programming','AI')
book['Published']=True

with open('book.pickle','wb') as file:
    pickle.dump(book,file)

with open('book.pickle','rb') as file:
    output=pickle.load(file)
print(output)
if book == output:
    print("They are same object")
else:
    print("Output not same")

#perform as memory
save_in_memory=pickle.dumps(book)
print(save_in_memory)

book2=pickle.loads(save_in_memory)
if book2 == book:
    print("Equal")
else:
    print("Diffrent")

#clouser -nested function
#example -1
def show(msgs):
    def print_msg():
        print(msgs)
    print_msg()

show("Hello World")

#example 2
def show1(msgs):
    def print_msg():
        print(msgs)
        return print_msg
    print_msg()
show1("Hi")

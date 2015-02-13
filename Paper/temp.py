class Test:
    myInt = 0
    myString = "Hello world"
    myList = []
    myDict = {}
    def __init__(self):
        pass

    def manage(self):
    	#Do stuff with all self varaibles 
    	pass

myInt = 0
myString = "Hello World"
myList = []
myDict = {}

def manage(interger, string, listVar, dictVar):
	#Do stuff with provided variables (Mirroring the class)
	pass

####
#Show use of code
####

MyTest = Test()
MyTest.manage()

#Or without OOP

manage(myInt, myString, myList, myDict) #Much longer, ugly

"""
you have just spent how ever many cycles initiating the four variables that only make up one object here:
myInt = 0
myString = "Hello World"
myList = []
myDict = {}
//
Where the scalability of an object model and encapsulation of the 
object model are much easier to instantiate for the computer.

MyTest = Test() < Creates all variables quickly because the computer has optimized the allocation routines for that object and it's memory model
##
class Test:
    myInt = 0
    myString = "Hello world"
    myList = []
    myDict = {}
// Can all be packed very tightly in the memory model because the computer knows all the information you are asking for at runtime.
whereas 

myInt = 0
myString = "Hello World"
myList = []
myDict = {}

each take up separate areas on the heap and have padding around 
the variables in the model so that they may be expanded so 
their memory model can not be packed as tightly as the class model
which also can make for slower lookup times and retrieval times.

One of the main things about OOP is that the object knows where 
it's stack frames lie in the memory and can retrieve them quickly 
and then the stack frame relating to the object can easily access
all needed information because when the program was written into the 
stack frames the object model was built into the code in ASM

Another point is scalability. To scale the class it is just another 
class initiation call which returns the class object and gives you access
to properties and methods 
where to scale the procedural method although uses the same functions
requires the memory allocation sequence again of instantiating the (in this case)
four variables separately.

NewTest = Test()

VS

NewInt = 0
NewString = "Hello World"
NewList = []
NewDict = {}

And then you have to manage the new names as well where the object model 
abstracts the same information into accessible properties via the dot operator
NewTest.myInt

<you told me to do homework>
"""
def addme():
 print (x+y)
 print ("finished!")
 
def subme():
 print (x-y)
 print ("finished!")
 
def timesme():
 print (x*y)
 print ("finished!")
 
def divideme():
 print (x/y)
 print ("finished!")
 
x=float(input("choose a number: "))
y=float(input("choose another number: "))
z=input("what do you want to do with these? ")
 
if z==("divide"):
 divideme()
elif z==("add"):
 addme()
elif z==("multiply"):
 timesme()
elif z==("subtract"):
 subme()
else:
 print("error, try again.")

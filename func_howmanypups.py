def pupmax():
    print ("ok, that's a bunch of pups")
    print ("dude, you're gona be a dog lady...")
def pupmin():
    print ("surely you could use more pups")
    print ("aim higher!")
def pupmid():
    print("ok, that's a good number.")
    
x=int(input("how many puppies would you like?"))
if x<=2:
    pupmin()
elif x==3:
    pupmid()
elif x>=4:
    pupmax()

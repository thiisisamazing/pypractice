#for some reason, I found this concept really hard to grasp!
def ponies(x,y):
    return x+y
def poniestwice(func,x,y):
    return func(func(x,y),func(x,y))
a=3
b=4
print ("you're gonna get",(poniestwice(ponies,a,b)),"ponies!")

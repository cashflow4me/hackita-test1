__author__ = 'shmunik'

#print "hello world"

def f_helloworld():
    return "Hello World"

def f_helloyou(name):
    return "Hello " + name

def f_99bottles(bottles):
    for i in range(bottles,0,-1):
        #print i
        print (str(i) + " bottles of beer on the wall, " + str(i) + " bottles of beer.\n Take one down, pass it around, " + str(i-1) +" bottles of beer on the wall...")

def f_99beers(bottles):
    if bottles>0 :
        f_99beers(bottles-1)
        break
    print(bottles)

print(f_helloworld())
print(f_helloyou("Alex"))
f_99bottles(3)



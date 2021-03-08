# All about Conditions and branching

i = 2
print(i>6)

age = 20
if age>19:
    print("He is not a teenager.")
elif age<=12:
    print("He is a kid.")
else:
    print("he is a teenager.")

albumYear = 2011
if albumYear<2014 or albumYear !=2011:
    print("Hello")
else:
    print("Wow")

albumYear2 = 2010
if albumYear2<2014 and albumYear2 !=2010:
    print("Hello")
else:
    print("Wow")


# All about Loops
squares = ["red", "green", "yellow", "purple", "blue"]

for i in range(0,4):
    print(squares[i])
print()

for i,square in enumerate(squares):
    print(i,square)

print()
NewSquares = []
i = 0
while(squares[i] != 'blue'):
    NewSquares.append(squares[i])
    i = i+1

print(NewSquares)

for i,x in enumerate(['A','B','C']):
    print(i,2*x)


#All about Function

string = [10,4,5,3,56,84,23]
print(string)
print(len(string))
print(sum(string))
print(sorted(string))
print(string.sort())
print(string)


def add1(a):
    a = a+1
    return a

c = add1(2)
c = add1(10)

print(c)

def Mult(a,b):
    c = a*b
    return c

print(Mult(2,'Michael jackson '))

def NoWork():
    pass

print(NoWork())

def printStuff(stuff):
    for i,s in enumerate(stuff):
        print("Album",i,"Rating : ",s)

printStuff([45,34,34,43])

a=1

def do(x):
    return(x+a)

print(do(1))

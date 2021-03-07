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

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

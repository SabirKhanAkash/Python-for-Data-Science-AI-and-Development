Tuple1 = (4,10,1.2)

print(Tuple1[0])
print(Tuple1+ ("Hard Work" , 10))
print(Tuple1[0:3])
print(len(Tuple1))


SortedTuple = sorted(Tuple1)
print(SortedTuple)

NT = (1,2, ("pop","rock",3),(3,4))
print(NT[2])
print(NT[2][2])
print(NT.index((3,4)))

List = [1,2, ["pop","rock",3],[3,4]]
print(List[2:3])
List.extend([2,6])
List.append([6,4])

print(List + [1,2])

del(List[3])
print(List)
s = "kd,js,hf,kj"

print(s.split(','))
help(List)
print(List)
Ba = List[:]

print(Ba)

# All about Dictionary

Dict = {"key1":1, "Key2":2}

print(Dict["Key2"])

print('Key1' in Dict)
print(Dict.keys())


# All about Sets
List1 = ["1", "hello", "23f", "hello"]

Set1 = {"1", "hello", "23f", "hello"}
print(Set1)

w = set(List1)
print(w)

Set1.add("NSYNC")
print(Set1)

Set1.remove("NSYNC")
print(Set1)

adf = "1" in Set1
print(adf)

Set2 = {"2", "fhg", "hello"}

uni = Set1 & Set2

print(uni)

print(Set1.issubset(Set2))

album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])

album_set_3 = album_set1.union(album_set2)
print(album_set_3)



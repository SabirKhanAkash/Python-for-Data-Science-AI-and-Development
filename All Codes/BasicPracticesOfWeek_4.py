#All about Files

File1 = open("Doraemon.txt","w")

print(File1)

with open("Doraemon.txt","r") as File1:
    fileStuff = File1.read()
    print(fileStuff)

    fileStuff = File1.readlines(16)
    print(fileStuff)

File1.closed
print(fileStuff)

Lines = ["Hello\n", "My name is Akash\n", "I am a boy\n"]
File1 = open("Hello.txt","w")

with open("Hello.txt","w") as File1:
    fileStuff = File1.write("This is Akash here. Hello\n")
    for line in Lines:
        File1.write(line)

with open("Doraemon.txt","r") as readfile:
    with open("Hello.txt","w") as writefile:
        for line in readfile:
            writefile.write(line)

#All about Pandas

import pandas as pd

csv_path = 'credit_data.csv'
df = pd.read_csv(csv_path)
print(df.head())


#All about Numpy

import numpy as np

# a = ["0",1,"two",2,3,"three"]
a = np.array(["0",1,"two",2,3,"three"])

print(type(a))
print(a.dtype)

a[0] = 100
print(a)
print(a[3:5])

u = [1,0]
v = [0,1]

z = []

for n,m in zip(u,v):
    z.append(n+m)

print(z)

u = np.array([1,0])
v = np.array([0,1])

z = u+v
print(z)

y = np.array([1,2])
z = 2*y
print(z)

m = np.array([2,1])
n = np.array([2,4])

z = np.dot(m,n)
print(z)

u = np.array([1,2,3,4])
z = u+1
print(z)
x = u.max()
print(x)

x = np.linspace(0,2*np.pi, 100)
y = np.sin(x)
print(y)

z = np.linspace(0,2*np.pi,100)
print(z)
import matplotlib.pyplot as plt
# %matplotlib inline

plt.plot(x,y)
plt.show()

A = [[11,12,13], [21,22,23],[31,32,33]]

a = np.array(A)
print(a)
print(a.ndim)
print(a.shape)
print(a.size)
a.sort()

print(a[0:2,2])

a=np.array([-1,1])
b=np.array([1,1])
print(np.dot(a,b))

X=np.array([[1,0,1],[2,2,2]])
out=X[0:2,2]
print(out)

X=np.array([[1,0],[0,1]])
Y=np.array([[2,2],[2,2]])
Z=np.dot(X,Y)

print(Z)

X=np.array([[1,0,1],[2,2,2]])
out=X[0,1:3]
print(out)



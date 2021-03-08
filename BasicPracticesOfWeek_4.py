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

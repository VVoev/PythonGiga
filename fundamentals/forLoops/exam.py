myfile = open("../workingwithFiles/files/sample.txt")
content = myfile.read()
myfile.close()
content = content.splitlines()
for i in content:
    print(len(i))

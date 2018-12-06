myfile = open('files/sample.txt')
fruits = myfile.read()
myfile.close()
print(fruits)


towns = ['Sofia', 'New York', 'San Francisko']
myfile = open('files/write.txt', 'a')

for town in towns:
    myfile.write(town+'\n')

myfile.close()

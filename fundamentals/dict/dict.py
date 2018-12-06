# person97 = {"name": "Jack", "surname": "Smith", "age": "29"}
# person97.pop("name")
# # 'Jack'

# person97
# {'surname': 'Smith', 'age': '29'}

keys = ["a", "b", "c"]
values = [1, 2, 3]

mydict = dict(zip(keys, values))
print(mydict)


def stringLen(any):
    return len(any)


print(stringLen('xuqmi'))


def convertToFarenheit(celsius):
    return celsius * 9/5 + 32


print(convertToFarenheit(40))

a = ['a', 'b', 'c']
b = [1, 2, 3]

for i, j in zip(a, b):
    print('{A} and {B}'.format(A=i, B=j))

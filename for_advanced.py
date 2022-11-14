for (*a, b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]: # gwiazdka oznacza pozostałe !! :)
    print('...')
    #print(a)
    #print(b)
    #print(c)


for all in [(1, 2, 3, 4), (5, 6, 7, 8)]:
    a, b, c = all[0], all[1:3], all[3]
    print(a)
    print(b)
    print(c)

#enumerate zwraca indeks i wartość - Zwraca krotkę
S = 'mielonka'
for (offset, item) in enumerate(S):
    print(item, 'występuje na pozycji przesunięcia', offset)


L1 = [1,2,3,4]
L2 = [5,6,7,8]
list(zip(L1, L2))
for (x, y) in zip(L1, L2):
    print(x, y, '--', x+y)

S1 = 'abc'
S2 = 'xyz123'
x = list(zip(S1, S2))
y = dict(zip(S1, S2))
print(x)
print(y,"_______________dict")


keys = ['mielonka', 'jajka', 'tost']
vals = [1, 3, 5]
list(zip(keys, vals))
items = {}
for (k, v) in zip(keys, vals): items[k] = v
print(items)

S = 'mielonka'
for (offset, item) in enumerate(S):
    print(item, 'występuje na pozycji przesunięcia', offset)

L = [1, 2, 3]
I = iter(L)
while True:
    try:
        X = next(I)
    except StopIteration:
        break
print(X ** 2, end=' ')


D = {'a':1, 'b':2, 'c':3}
for key in D.keys():
    print(key, D[key])

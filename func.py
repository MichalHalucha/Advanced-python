def func(a, b=4, c=5):
    print(a, b, c)
func(1,2) #1,2,5


def func(a, b, c=5):
    print(a, b, c)
func(1,c=3,b=2) # 1 przekazywane przez pozycję, c i b przez nazwę, kolejnośc nie ma znaczenia


def func(a, *pargs):
    print(a, pargs)
func(1,2,3,4)  #a tylko jest wynikiem a reszta zwracana jako krotka

def func(a, **kargs):
    print(a, kargs)
func(a=1, c=3, b=2,d=3) #pierwszy normalnie a reszta to klucz>slowo

def func(a, b, c=3, d=4): print(a, b, c, d)
func(a=1,b=2,c=3,d=4)


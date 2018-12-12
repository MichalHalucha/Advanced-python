lista = [1, 2, 3, 4, 5]

class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        #Tworzenie nowych obiektów bez modyfikacji operandów
        return self.x + other.x, self.y + other.y

    def __mul__(self, other):
        return self.x * other.x, self.y * other.y

    #rept definiujemy po to żeby wyświetlając widzieć wartości w postaci Vector(dana1,dana2)
    #Reprezentacja tekstowa
    def __repr__(self):
        return 'Vector(%r,%r)' % (self.x,self.y)

    #Łatwy sposób sprawdzenia czy wektor nie jest 0.0
    def __bool__(self):
        return bool(self.x or self.y)


def iteration(lista,object):
    try:
        print(next(object))
        print(x.__next__())
    except:
        print("List doesn't exist or index problem")

def czytelnosc():
    symbols = '()*#@$@'
    codes = []
    #for i in symbols:
    #    codes.append(ord(i))
    #    symbol.append(i)

    #Reprezentacje listowe
    codes = [i for i in symbols]
    filters = [ord(i) for i in symbols if ord(i) > 10]
    #Wyrażenie listowe zbudowane z funkcji map/filter
    #wynik = lambda x: x*2 -> print(wynik(2)) -> 4
    #Wyrażenia listowe są szybsze
    fm = list(filter(lambda c:c > 10,map(ord,symbols)))
    print(codes)
    print(filters)
    print(fm)

def koszulki():
    colors = ['Black','White']
    sizes = ['S','M','L']
    tshirts = [(color,size) for color in colors for size in sizes]
    print(tshirts)


if __name__ == '__main__':


    x = iter(lista)
    iteration(lista,x)


    v1 = Vector(1,3)
    v2 = Vector(2,1)
    print(v1.y)
    V = v1 + v2
    print(V)
    print(v1*v2)
    print(v1)
    print(bool(v1))
    czytelnosc()
    koszulki()

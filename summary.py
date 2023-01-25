import array
import numpy

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.x + other.x, self.y + other.y

    def __mul__(self, other):
        return self.x * other.x, self.y * other.y

    # def __repr__(self) define how to print object
    def __repr__(self):
        return 'Vector(%r,%r)' % (self.x, self.y)

    # Check if vector is not 0.0
    def __bool__(self):
        return bool(self.x or self.y)


class MyNewcar:
    is_engine_on = False
    is_light_on = False
    make = None
    model = None

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return (f'{self.make} {self.model} with engine'
                f'{" on " if self.is_engine_on else "off"}'
                f'and lights {" on " if self.is_light_on else "off"}')

    def run_car(self):
        self.is_engine_on = True

    def turn_lights(self):
        self.is_light_on = True

    def turn_off_car(self):
        if self.is_engine_on:
            print("Dont turn off your car while you are driving")
            return


def car_class():
    Elantra = MyNewcar('Hyundai', "Elantra")
    print(Elantra)
    print(Elantra.is_light_on)
    Elantra.run_car()
    print(Elantra.is_engine_on)
    print(Elantra.__repr__())
    Elantra.turn_lights()
    print(Elantra.__repr__())
    Elantra.turn_off_car()


def vector_operations():
    vector_one = Vector(3, 2)
    vector_two = Vector(2, 1)
    print(vector_one + vector_two)
    print(vector_one.x + 5)
    print(vector_two.y * 10)
    print(vector_one)
    print(bool(vector_one))


def iteration(lista, object):
    try:
        print(next(object))
        print(x.__next__())
        print(list_of_numbers.index(x.__next__() + 1))
        print(x.__next__())
        print(next(object))
    except:
        print("List doesn't exist or index problem")


def while_iteration():
    L = [1, 2, 3]
    I = iter(L)
    while True:
        try:
            X = next(I)
            print(X)
        except StopIteration:
            break
    print(X + 10, end=' ')


def iteration_operations(x):
    iteration(list_of_numbers, x)
    while_iteration()


def my_numpy():
    a = numpy.arange(12)
    print(a)
    # matrix view
    a.shape = 3, 4
    print(a)
    # print row
    print(a[2])
    print(a[1])
    # matrix x = 1, y = 2
    print(a[2, 1])
    # all numbers from index 1
    print(a[:, 1])


def tshirts():
    colors = ['Black', 'White']
    sizes = ['S', 'M', 'L']
    count = [2, 5, 6]
    tshirts = [(color, size) for color in colors for size in sizes]
    tshirts2 = [(size, color, how_many) for color in colors for size in sizes for how_many in count]
    print(tshirts)
    print(tshirts2)


def gener():
    colors = ["black", "white"]
    sizes = ["S", "M", "L"]
    for tshirt in ((c, s) for c in colors for s in sizes):
        print(tshirt)


def get_arguments_between_index():
    for all in [(1, 2, 3, 4), (5, 6, 7, 8)]:
        a, b, c = all[0], all[1:3], all[3]
        # print(a)
        print(b)
        # print(c)


def some_advanced_loops():
    tshirts()
    # gener() short version of tshirts()
    gener()
    get_arguments_between_index()


def for_with_enumerate():
    list_a = [1, 2, 3, 2, 5]
    for position, list_object in enumerate(list_a):
        if list_object == 2:
            print('I have found number 2 on position: ', position)
    # enumerate zwraca indeks i wartość - Zwraca krotkę
    S = 'mielonka'
    for (offset, item) in enumerate(S):
        print(item, 'występuje na pozycji przesunięcia', offset)


def unpack_touple():
    # city,year,pop,chg,area=("Tokyo",2003,32450,0.66,8014)
    traveler_ids = [('USA', '321424'), ('Bra', 132819034)]
    for passport in sorted(traveler_ids):
        print('%s/%s' % passport)
    # unpacking
    t = (20, 8)
    first, second = divmod(*t)
    print(divmod(t[0], t[1]))
    print(first, second)


def countdown(n):
    if n == 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n - 1)


def zip_items():
    L1 = [1, 2, 3, 4]
    L2 = [5, 6, 7, 8]
    S1 = 'abc'
    S2 = 'xyz123'
    keys = ['mielonka', 'jajka', 'tost']
    vals = [1, 3, 5]

    for (x, y) in zip(L1, L2):
        print(x, y, '--', x + y)
    x = list(zip(S1, S2))
    y = dict(zip(S1, S2))
    z = list(zip(L1, L2))
    print(x)
    print(y)
    print(z)

    items = {}
    for (k, v) in zip(keys, vals):
        items[k] = v
    print(items)


def readable_simple_loop_map():
    symbols = '()*#@$@'
    #codes = str to list of strings
    codes = [i for i in symbols]
    filters = [i for i in symbols if ord(i) > 40]
    fm = list(filter(lambda c: c > 40, map(ord, symbols)))
    print(codes)
    print(filters)
    print(fm)


def min1(*args):
   res = args[0]
   print(res)
   for arg in args[1:]:
      if arg < res:
         res = arg
   return res


def min2(first, *rest):
    print(first)
    print(rest)
    for arg in rest:
        if arg < first:
            first = arg
            return first


def min3(*args):
    print(args)
    tmp = list(args)
    tmp.sort()
    print(tmp)
    return tmp[0]


def funkcja(*args):
    print("Ilosc zmiennych: ", len(args))
    for arg in args:
        print(arg)


def minmax(test, *args):
    res = args[0]
    for arg in args[1:]:
        if test(arg, res):
            res = arg
    return res


def lessthan(x, y): return x < y


def grtrthan(x, y): return x > y


def args():
    print(min1(3, 4, 6, 2, 2, 8, 9))
    print(min2('bb', 'aa', 'cc', 'ad'))
    print(min3([2, 2], [1, 1], [3, 3]))
    print(minmax(lessthan, 4, 2, 1, 5, 6, 3))
    print(minmax(grtrthan, 4, 2, 1, 5, 6, 3))
    print(funkcja(1, 2, "abc", [1, 2, 3]))

def kwargs(**kwargs):
    print("Ilosc zmiennych: ", len(kwargs))
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))


def dictionary():
    D = {'a': 1, 'b': 2, 'c': 3}
    for key in D.keys():
        print(key, D[key])


def too_many_elements():
    a,b,*rest = range(5)
    print(a,b,rest)
    a,*rest,c,d = range(5)
    print(c, d)
    print(a,*rest,c,d)

    for (a, *b, c) in [(5, 6, 7, 8)]: # *means rest of numbers
        print('...')
        print(a)
        print(b)
        print(c)


def func_a(a, b=4, c=5):
    print(a, b, c)


def func_b(a, b, c=5):
    print(a, b, c)


def func_c(a, *pargs):
    print(a, pargs)


def func_d(a, **kargs):
    print(a, kargs)


def func_e(a, b, c=3, d=4): print(a, b, c, d)


def passing_arguments():
    func_a(1)  # 1,2,5
    func_b(1, c=10, b=2) #passing through position
    func_c(1, 2, 3, 4)  # first one is a result, rest are a touple
    func_d(a=1, c=3, b=2, d=3)  # first one result > rest key > value. ** returns dict
    func_e(a=1, b=2, c=3, d=4)


if __name__ == '__main__':
    #class
    vector_operations()
    car_class()
    #iterations
    x = iter(list_of_numbers)
    iteration_operations(x)
    #numpy
    my_numpy()
    some_advanced_loops()
    for_with_enumerate()
    unpack_touple()
    countdown(5)
    zip_items()
    readable_simple_loop_map()
    args()
    dictionary()
    kwargs(jeden=1, dwa= "abc",trzy= [1, 2, 3])
    too_many_elements()
    passing_arguments()



    # print(wastetime())
    # print(roll())
    # wakeup()


#
# def startstop(func):
#     def wrapper():
#         print("Starting...")
#         func()
#         print("Finished!")
#     return wrapper
#
# #@exectime  - roll = exectime(startstop(roll))
# @startstop   #----roll = startstop(roll) łączy roll i startstop
# def roll():
#     print("Rolling on the floor laughing XD")
#
# import time
# def measuretime(func):
#     def wrapper():
#         starttime = time.perf_counter()
#         func()
#         endtime = time.perf_counter()
#         print(f"Time needed: {endtime - starttime} seconds")
#     return wrapper
#
# @measuretime
# def wastetime():
#     sum([i**2 for i in range(1000000)])
#
# #----------spowalnianie
# def sleep(func):
#     def wrapper():
#         time.sleep(2)
#         return func()
#     return wrapper
# @sleep
# def wakeup():
#     print("Get up! Your break is over.")
#
#
# if __name__ == '__main__':

#     gener()

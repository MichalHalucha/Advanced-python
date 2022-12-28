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

def greet(name):
    return f"Hello, {name}!"
def simon(func):
    return func("Simon")
print(simon(greet))
print(greet("Simon"))

def startstop(func):
    def wrapper():
        print("Starting...")
        func()
        print("Finished!")
    return wrapper

#@exectime  - roll = exectime(startstop(roll))
@startstop   #----roll = startstop(roll) łączy roll i startstop
def roll():
    print("Rolling on the floor laughing XD")

print(roll())


import time
def measuretime(func):
    def wrapper():
        starttime = time.perf_counter()
        func()
        endtime = time.perf_counter()
        print(f"Time needed: {endtime - starttime} seconds")
    return wrapper

@measuretime
def wastetime():
    sum([i**2 for i in range(1000000)])

print(wastetime())


#----------spowalnianie
def sleep(func):
    def wrapper():
        time.sleep(2)
        return func()
    return wrapper
@sleep
def wakeup():
    print("Get up! Your break is over.")
wakeup()


Elantra = MyNewcar('Hyundai',"Elantra")
print(Elantra)
print(Elantra.is_light_on)
Elantra.run_car()
print(Elantra.is_engine_on)
print(Elantra.__repr__())
Elantra.turn_lights()
print(Elantra.__repr__())
Elantra.turn_off_car()


def funkcja(*args):
    print("Ilosc zmiennych: ", len(args))
    for arg in args:
        print(arg)
print(funkcja(1, 2, "abc", [1, 2, 3]))


def funkcja(**kwargs):
    print("Ilosc zmiennych: ", len(kwargs))
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))
print(funkcja(jeden=1, dwa=2, trzy="abc", cztery=[1, 2, 3]))


def countdown(n):
  if n == 0:
    print('Blastoff!')
  else:
    print(n)
    countdown(n - 1)
countdown(5)


lista_a = [ 1, 2, 3, 4, 5]
for pozycja, list_object in enumerate(lista_a):
    if list_object == 2:
        print('Znalazłem dwójkę na pozycji', pozycja)

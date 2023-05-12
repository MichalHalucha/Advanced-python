#REPEATER
def repeat(num):
    def my_decorator(func):
        def wrapper(*args):
            for i in range(num):
                func(*args)
        return wrapper
    return my_decorator
@repeat(num=2)
def say_hello(name):
    print(f"Hello {name}!")
    
say_hello("world")


#TIME MEASUREMENT 
import time
def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Czas wykonania funkcji {func.__name__}: {execution_time} sekund")
        return result
    return wrapper
@measure_time
def my_function():
    # kod funkcji
    pass
    
my_function()
   
#EVENT LOGER
def log_event(func):
    def wrapper(*args, **kwargs):
        print(f"Wywołanie funkcji {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Zakończono funkcję {func.__name__}")
        return result
    return wrapper
@log_event
def my_function():
    # kod funkcji
    pass
    
my_function()

#LIMIT WYWOŁAŃ FUNKCJI
import functools
def limit_calls(max_calls):
    def decorator(func):
        remaining_calls = max_calls

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal remaining_calls
            if remaining_calls > 0:
                remaining_calls -= 1
                return func(*args, **kwargs)
            else:
                raise ValueError(f"Przekroczono limit wywołań funkcji {func.__name__}")
        return wrapper
    return decorator
@limit_calls(3)
def my_function():
    print("Wywołanie funkcji")

my_function()
my_function()
my_function()
my_function()  # zgłoszenie błędu, przekroczono limit wywołań


def validate_input(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int):
                raise ValueError("Argumenty muszą być liczbami całkowitymi")
        for kwarg, arg in kwargs.items():
            if not isinstance(arg, str):
                raise ValueError("Argumenty nazwane muszą być łańcuchami znaków")
        return func(*args, **kwargs)
    return wrapper
@validate_input
def my_function(num1, num2, name):
    print(f"Suma {name}: {num1 + num2}")
my_function(5, 10, name="wynik")  # Poprawne wywołanie
my_function(5, 1, name="wynik")  # Błąd walidacji, drugi argument nie jest liczbą całkowitą
# my_function("test", "test", name="wynik")



def check_condition(condition):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if condition:
                return func(*args, **kwargs)
            else:
                raise ValueError("Warunek nie został spełniony")
        return wrapper
    return decorator
@check_condition(2 + 2 == 4)
def my_function():
    print("Warunek został spełniony")
my_function()  # Funkcja zostanie wykonana
@check_condition(2 + 2 == 5)
def another_function():
    print("Warunek został spełniony")

another_function()  # Błąd wartości, warunek nie został spełniony



def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Wystąpił wyjątek: {str(e)}")
            # Dodatkowe działania w przypadku wyjątku
    return wrapper
@handle_exceptions
def divide(a, b):
    return a / b
divide(5, 0)  # Wywołanie funkcji z błędem dzielenia przez zero



import functools
def repeat(n_times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(n_times):
                result = func(*args, **kwargs)
                results.append(result)
            return results
        return wrapper
    return decorator

@repeat(3)
def generate_random_number():
    import random
    return random.randint(1, 100)
print(generate_random_number())  # Wykonanie funkcji trzykrotnie i zwrócenie wyników

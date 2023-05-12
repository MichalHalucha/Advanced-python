Wzorzec Obserwator:
Wzorzec Obserwator umożliwia powiadamianie wielu obiektów (obserwatorów) o zmianach w stanie innego obiektu (obserwowanego). Obserwatorzy są dynamicznie zarejestrowani do obserwowanego obiektu i otrzymują powiadomienia o aktualizacjach.
# Klasa podmiotu
class Subject:
    def __init__(self):
        self.observers = []
        self.state = None

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state
        self.notify_observers()

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update()

# Interfejs obserwatora
class Observer:
    def update(self):
        pass

# Implementacja obserwatora
class ConcreteObserver(Observer):
    def __init__(self, subject):
        self.subject = subject
        self.subject.attach(self)

    def update(self):
        print("Stan podmiotu zmieniony:", self.subject.get_state())

# Przykładowe użycie wzorca obserwator
if __name__ == "__main__":
    subject = Subject()
    observer1 = ConcreteObserver(subject)
    observer2 = ConcreteObserver(subject)

    subject.set_state(1) # Wywołanie metody spowoduje powiadomienie obu obserwatorów
    subject.set_state(2) # Wywołanie metody spowoduje powiadomienie obu obserwatorów

    subject.detach(observer2) # Usunięcie jednego z obserwatorów
    subject.set_state(3) # Wywołanie metody spowoduje powiadomienie tylko jednego obserwatora
    

Wzorzec Dekorator:
Wzorzec Dekorator pozwala na dynamiczne dodawanie nowych funkcjonalności do istniejących obiektów poprzez opakowywanie ich w dodatkowe obiekty (dekoratory). Pozwala to na elastyczne rozszerzanie funkcjonalności bez modyfikacji oryginalnego kodu.


# Komponent bazowy
class Pizza:
    def get_description(self):
        pass

    def get_cost(self):
        pass

# Konkretny komponent
class Margherita(Pizza):
    def get_description(self):
        return "Margherita"

    def get_cost(self):
        return 5.0

# Dekorator bazowy
class PizzaDecorator(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza

    def get_description(self):
        return self.pizza.get_description()

    def get_cost(self):
        return self.pizza.get_cost()

# Konkretny dekorator
class CheeseDecorator(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)

    def get_description(self):
        return self.pizza.get_description() + ", Ser"

    def get_cost(self):
        return self.pizza.get_cost() + 1.0

# Przykładowe użycie wzorca dekorator
if __name__ == "__main__":
    pizza = Margherita()
    print(pizza.get_description())  # Margherita
    print(pizza.get_cost())  # 5.0

    pizza_with_cheese = CheeseDecorator(pizza)
    print(pizza_with_cheese.get_description())  # Margherita, Ser
    print(pizza_with_cheese.get_cost())  # 6.0
    
Wzorzec Fasady:
Wzorzec Fasady dostarcza uproszczony interfejs do złożonego podsystemu. Ukrywa szczegóły implementacyjne i umożliwia łatwiejsze korzystanie z podsystemu poprzez udostępnienie jednego punktu dostępu.

# Podsystem A
class SubsystemA:
    def operation_a1(self):
        print("Podsystem A - operacja A1")

    def operation_a2(self):
        print("Podsystem A - operacja A2")

# Podsystem B
class SubsystemB:
    def operation_b1(self):
        print("Podsystem B - operacja B1")

    def operation_b2(self):
        print("Podsystem B - operacja B2")

# Fasada
class Facade:
    def __init__(self):
        self.subsystem_a = SubsystemA()
        self.subsystem_b = SubsystemB()

    def operation(self):
        self.subsystem_a.operation_a1()
        self.subsystem_a.operation_a2()
        self.subsystem_b.operation_b1()
        self.subsystem_b.operation_b2()

# Przykładowe użycie wzorca fasady
if __name__ == "__main__":
    facade = Facade()
    facade.operation()

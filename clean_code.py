list_of_names = ["Wroclaw", "Krakow", "Warszawa", "Poznan"]
list_of_reservation_numbers = [638659, 766683, 1765000, 540365]

#city_dict = {list_of_names[i]: list_of_reservation_numbers[i] for i in range(len(list_of_names))}

city_dict = dict(zip(list_of_names, list_of_reservation_numbers))

print(city_dict)


def get_resident_number(name):
    """
    Gets residents number for name
    """
    try:
        return city_dict[name]
    except KeyError:
        return "Incorrect city"


print(get_resident_number("Wroaw"))

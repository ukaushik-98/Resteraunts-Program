from collections import namedtuple
rest = namedtuple('rest', 'name cuisine phone dish price')
#########################################################
def rest_main():
    rest_list = []
    rest_handle(rest_list)

def rest_handle(c: list) -> list:
    R=rest
    while True:
        n = input(menu)
        if n == '1':
            R = rest_info()
            rest_add(c, R)
        elif n == '9':
            print('Thank you, Have a nice day!')
            return
        elif n == '4':
            print(c)
        else:
            rest_error()

def rest_error():
    print('Input is invalid')

def rest_info() -> rest:
    return rest(
        input('Name: '),
        input('Cuisine: '),
        input('Phone: '),
        input('Dish: '),
        input('Price: '))

def rest_add(a: list, r) -> list:
    a.append(r)
    
menu = """
 1:  Add a new restaurant to the collection
 2:  Remove a restaurant from the collection
 3:  Search the collection for selected restaurants
 4:  Print all the restaurants
 9:  Quit
"""
rest_main()

            

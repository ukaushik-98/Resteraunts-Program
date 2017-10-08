from collections import namedtuple
rest = namedtuple('rest', 'name cuisine phone dish price')
##########################################################

def rest_main():
    rest_list = []
    rest_face(rest_list)

def rest_face(c: list) -> list:
    while True:
        n = input(menu)
        R = rest_info()
        if n == '1':
            rest_add(c, R)
            print(c)
        elif n == '2':
            rest_remove(c, s)
            print(c)
        elif n == '9':
            print('Thank you, have a nice day!')
            return
        else:
            invalid_response()
    
def rest_info() -> rest:
    return rest(
        input('Name: '),
        input('Cuisine: '),
        input('Phone: '),
        input('Dish: '),
        input('Price: '))

def rest_add(b: list, r) -> list:
    b.append(r)

def rest_remove(d: list, s: str) -> list:
    d.remove(s)
             
def invalid_response():
    print('Input not recognized')
    
#########################################################
menu = """
 1:  Add a new restaurant to the collection
 2:  Remove a restaurant from the collection
 3:  Search the collection for selected restaurants
 4:  Print all the restaurants
 9:  Quit
"""
rest_main()

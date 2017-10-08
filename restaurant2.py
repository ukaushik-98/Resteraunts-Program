from collections import namedtuple
rest = namedtuple('rest', 'name cuisine phone dish price')

##############################
def rest_face():
    new_list = []
    rest_handle(new_list)

def rest_list() -> list:
    return []
    
#interactive function#
def rest_handle(c:list) -> list:
    n = input(menu)
    if n == '9':
        print('Thank you, Have a nice day!')
        return c
    elif n == '1':
        Rst=rest
        rest_add(c, Rst)
    
#function takes in all info#
def rest_info()-> rest:
    return rest(
        input('Name: '),
        input('Cuisine: '),
        input('Phone: '),
        input('Dish: '),
        float(input('Price: ')))

#function adds info to a list#
def rest_add(c: list, R) -> list:
    rest_info()
    c.append(R)
    return c
#################################
        
menu = """
1 = add a new restaurant
2 = remove a restaurant
3 = search collection for restaurant
4 = print all restaurants
9 = quit
"""

rest_face()






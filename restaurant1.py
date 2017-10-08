#################################
def Rest_face(menu1):
    n = input(menu1)
    if n == 'q':
        Rest_end()
    elif n == 'p':
        Rest_info()

#Result of input p#
def Rest_end():
    print('End')

#Result of input q#
from collections import namedtuple
Rest = namedtuple('Rest', 'name cuisine phone dish price')

def Rest_info() -> Rest:
    return Rest(
        input("Name's: "),
        input('Cuisine: '),
        input('Phone: '),
        input('Dish: '),
        float(input('Price: ')))
#################################
menu = '''
p = add restaraunt to collection
q = quit
'''

Rest_face(menu)


    
    

'''
Created on 3 Apr 2021

@author: Legacy
'''


fruitBasket = {'mango':40, 'oranges':89, 'pear':34}

print (fruitBasket['mango'])
print (fruitBasket.items())

fruitBasket['grapes'] = 56
fruitBasket.update({'pawpaw':32})

print (fruitBasket.items())

fruitBasket.pop('pear')

print (fruitBasket.items())


squared_value = lambda x: x*2

print (squared_value(10))

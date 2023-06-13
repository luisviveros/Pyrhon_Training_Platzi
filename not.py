print(not True)
print(not False)

# or
print('NOT AND')
print('True or True =>', not(True or True))
print('True or False =>', not(True or False))
print('False or True =>', not(False or True))
print('False or False =>', not(False or False))

stock = input('Ingrese el numero de stock => ')
stock = int(stock)

print (not(stock >= 100 and stock <= 1000))
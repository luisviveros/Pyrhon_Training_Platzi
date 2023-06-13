#Las listas te permiten almacenar varios tipos de datos

numbers = [1, 2, 3, 4]
print (numbers)
print(type(numbers))

tasks = ['make a dishes', 'play videogames']
print(tasks)

types = [1,True, 'Hola']
print(types)

#Te da lo que hay en la lista en esa posición
print(numbers[0])
print(tasks[0])
text = 'Hola'
text[0] = 'W'

#cambiar lo que hay dentro de una lista
tasks[0]= 'watch platzi courses'
print(tasks)

tasks[0] = 'do the dishses'
print(tasks)
text = "Ella sabe Python"
print(text[0])
print(text[1])

#metodo para saber cual es el ultimo caracter del texto
size = len(text)
print('size =>', size)
print(text[size-1])
print(text[-1])

#slicing (Obtiene el texto que tu le indicas en el rango)
# Es decid del 0 al 3
print(text[10:1])
print(text[0:10])
#Para obviar el cero y sabe que empieza desde cero  es syntaxis solamente
print(text[:10])

print(text[5:-1])
print(text[5:])
print(text[:])

#Para que de saltos
print(text[10:16:1])
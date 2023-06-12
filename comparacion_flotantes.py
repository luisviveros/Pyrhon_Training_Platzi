x = 3.3
y = 1.1 + 2.2

print(y)
print(x) 
print(x ==y)

#Cambiar el formato del decimal para que te imprima solo dos decimales
y_str = format(y,".2g")
print(y_str)


print('*'*10)

print(y,x)

tolerance = 0.00001
print(abs(x - y)< tolerance)
#Proyecto del training (PIEDRA PAPEL O TIJERA)

user_option = input ('piedra, papel o tijera => ')
computer_option = 'papel'

if user_option == computer_option:
    print ('Empate!')
elif user_option == 'piedra':
    if computer_option == 'tijera':
        print ('Piedra gana a tijera')
        print ('user gano!')
    else:
        print ('Papel gana a piedra')
        print ('computer gano!')
elif user_option == 'papel':
    if computer_option == 'piedra':
        print ('Papel gana a piedra')
        print ('user gano!')
    else:
        print ('Tijera gana a papel')
        print ('computer gano!')
elif user_option == 'tijera':
    if computer_option == 'papel':
        print ('tijera gana a papel')
        print ( 'user gano!')
    else:
        print('piedra gana a tijera')
        print('computer gano!')

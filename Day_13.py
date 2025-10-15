import os
os.system('cls' if os.name == 'nt' else 'clear')



while True:


    os.system('cls' if os.name == 'nt' else 'clear')


    decimal_number = input('Enter a whole number (or type exit to quit): ')



    
    if decimal_number.lower() == 'exit':
        break

    if not decimal_number.isdigit():
        print('Please enter a valid whole number.')

    else:
        decimal_number = int(decimal_number)


        binary_number = ' '
        if decimal_number == 0:
            binary_number = '0'
        else:
            while decimal_number > 0:
                remainder = decimal_number % 2
                decimal_number = decimal_number // 2
                binary_number = str(remainder) + binary_number



        print('The binary representation is:', binary_number)

    input('\nPress Enter to convert another number...')




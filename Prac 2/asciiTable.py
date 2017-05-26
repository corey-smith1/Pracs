if input('Enter "A" for Character to ASCII or "B" for ASCII to Character') == 'A'.upper():
    character = input('Enter a character')
    print('The ASCII code for "{}" is: {}'.format(character, str(ord(character))))
else:
    character = int(input('Enter a number between 33 and 127'))
    while 33 >= character >= 127:
        character = int(input('Enter a number between 33 and 127'))
    else:
        print('The ASCII code for "{}" is: {}'.format(character, str(chr(character))))
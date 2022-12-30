pet = 'fish'

if pet == 'fish':
    print('I am a fish')
elif pet == 'dog':
    print('I am a dog')
elif pet == 'cat':
    print('I am a cat')
else:
    print('I am not a pet')


speaks_english = True
knows_python = False

if speaks_english and knows_python:
    print("Congratulations")
if not knows_python and not speaks_english:
    print("you must need to know python and learn english")
if not speaks_english:
    print("you must need to speak english")
if not knows_python:
    print("you need to learn python")
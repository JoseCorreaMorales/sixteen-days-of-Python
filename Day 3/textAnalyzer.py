""" text = input('enter your text....')
print('now enter three letters, wherever  you want')
fLetter = input('whats the frist letter?')
sLetter = input('whats the second letter?')
tLetter = input('whats the third letter?') """

text = "holaaa como estasccbba"
baseText = text.lower()

fLetter = 'a'
sLetter = 'b'
tLetter = 'c'

""" how many times appear each lettter? """
flc = 0
slc = 0
tlc = 0 
for i in range(baseText.__len__()):
    if baseText[i] == fLetter:
        flc = flc + 1
    if baseText[i] == sLetter:
         slc = slc + 1
    if baseText[i] == tLetter:
         tlc = tlc + 1

""" how many words the text have? """
textList = baseText.split()

""" whats the frist and last letter? """
initialLetter = baseText[0]
LastLetter = baseText[-1]

""" iverse order """
listInverse = text.split()

inverse = listInverse[::-1]

""" is the Python word inside the text? """
isPython = "Python" in baseText

print(f"Frist letter appears {flc} times, the second one {slc} times, and thrid one {tlc} times\n The text have {textList.__len__()} words \n Frist letter is {initialLetter}\n Last letter is {LastLetter}\n Invserse text: {inverse}\n is {isPython} that Python is on the text")

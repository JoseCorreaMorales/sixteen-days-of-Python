names = ['Maria', 'Mariad', 'Steven', 'John', 'Patrick']
ages = [34, 32, 1, 32, 32,999]
countries = ['Mexico', 'Canada', 'France', 'Germany', 'United States']

#we take the length of the shortest list in general
full_info = list(zip(names, ages, countries))
print(full_info)


for name, age, country in full_info:
    print(f'{name} is {age} old and lives in {country}')

espanol = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
portuges = ['un', 'dois', 'três', 'quatro', 'cinco']
ingles =  ['one', 'two', 'three', 'four', 'five']

mi_zip = list(zip(espanol, portuges, ingles))

i = 1
for esp, port, ing in mi_zip:
    print(f"""{i}. {esp} / {port} / {ing}""")
    i+=1
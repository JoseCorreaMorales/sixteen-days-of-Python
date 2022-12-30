serie = 'N-02'

match serie:
    case 'N-02':
        print('N-02')

    case 'N-03':
        print('N-03')

    case 'N-04':
        print('N-04')

    case _: # just like an else or default statement
        print('no matching item')



""" mathing patterns """
person = {'name': 'Jose',
            'age': 21,
            'occupation': 'Python student'}

movie = {
        'title': 'Matrix',
        'data': {'protagonist': 'Keanu reeves', 'director': 'Lana y Lilly Wachowski'}
}


data = [person, movie, 'book']

for item in data:
   
   match item:
    case {'name': name, 'age': age, 'occupation': occupation}:
        print('its a person', name, age, occupation)

    case {'title': title, 'data': {'protagonist': protagonist, 'director': director}}:
        print('its a movie', title, protagonist, director)
    
    case _:
        print('its a book')


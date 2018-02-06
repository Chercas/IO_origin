import shelve

with shelve.open('bike') as bike:
    bike['make'] = 'Honda'
    bike['color'] = 'red'
    bike['model'] = '250 Dream'
    bike['engine_size'] = 250

    print(bike['make'])
    print(bike['color'])
    
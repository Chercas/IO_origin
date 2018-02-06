import pickle
#pickle.loads(b"cos\nsystem\n(S'rm Shelve_test'\ntR.")

import shelve


with shelve.open('ShelveTest') as fruit:
    fruit['orange'] = 'a sweet, orange, citrus fruit'
    fruit['apple'] = 'good for making cider'
    fruit['lemon'] = 'a sour, yellow fruit'
    fruit['grape'] = 'a small, sweet fruit growing in bunches'
    fruit['lime'] = 'good with tequila'

    print(fruit['lemon'])
    print(fruit['grape'])

#print(fruit)

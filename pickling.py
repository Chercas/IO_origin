import pickle

imelda = ('More Mayhem',
          'Imelda May',
          '2011',
          ((1, 'Pulling the Rug'),
           (2, 'Psycho')))

print('---'*30)
even = list(range(0, 10, 2))
print(even)
odd = list(range(1, 10, 2))
print(odd)
print('---'*30)

with open('imelda.pickle', 'wb') as pickle_file:
    pickle.dump(imelda, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)
    pickle.dump(even, pickle_file, protocol=0)
    pickle.dump(odd, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)
    pickle.dump(2998302, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)

with open('imelda.pickle', 'rb') as pickle_file:
    imelda2 = pickle.load(pickle_file)
    even_list = pickle.load(pickle_file)
    x = pickle.load(pickle_file)
    odd_list = pickle.load(pickle_file)

print('---'*30)
print(imelda2)

album, artist, year, song = imelda2
print('---'*30)
print(album)
print(artist)
print(year)
for track in song:
    number, song_name = track
    print('Track num. ' + str(number) + ' named: ' + song_name)

print('---'*30)
print('X', x)
print('Even', even_list)
print('Odd', odd_list)

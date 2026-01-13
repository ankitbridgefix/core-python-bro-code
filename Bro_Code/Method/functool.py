import functools

lettar = ['H','E','L','L','O']
l = [1,2,3.4]
word = lambda x,y :x+y

word = functools.reduce(word,lettar)
print(word)
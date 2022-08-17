import random
print('A number between 1 and 10')
print random.randint(0,10)

#random.random() * 100
random.choice(['red','black','green'])

myList = [2, 109,False, 10, "Lorena",482,"Vanessa"]
random.choice(myList)

for i in range(3):
   print random.randrange(0,101,5)

from random import shuffle
x=[[i] for i in range(10)]
shuffle(x)



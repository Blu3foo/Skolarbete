import random
import sys
import os
import time

'''
count = 0
x = 0
y = 100
r = random.randrange(x,y)
while x == 0:
    r = random.randrange(x,y)
    count = count + 1
    print(r)
    if r == 20:
        break
print('Loopen kördes',count,'gånger.')
largest = None
print('Before', largest)
for itevar in [ 3, 41, 12, 9, 74, 15]:
    if largest is None or itevar > largest :
        largest = itevar
    print('loop', itevar, largest, ',', end = " ")
print('Largest', largest, ',', end = " ")

while (random.randrange(0,100) != 15):
    print(end = " ") 

print('-----------------------')
print('Exponentielll beräkning')
print('-----------------------')
for x in range(10,-1,-1):
    print(x,'^',x, '=', x**x) 

def exponentialCount():
    print('-----------------------')
    print('Exponentielll beräkning')
    print('-----------------------')
    for x in range(10,-1,-1):
        print(x,'^',x, '=', x**x)

exponentialCount()



for r in range(0, 4):
    print()
    print('-----------')
    print('|', end="")
    for k in range(0, 4):
        print(r**4, end="|")
print('\n-----------')


r = 0
k = 1
while r <= 3 :
    print()
    r += 1
    k = k == 0
    while k <=3:
       k += 1
       print('*', end="")


x = 10
y = 20
z = x
x = y
y = z
print('x var 10 men är nu',"\n",x)
print('y var 20 men är nu',"\n",y)

x = 10
y = 20
x,y = y,x
print('x är',x)
print('y är',y)


print('Mata in ditt namn: ')
print('Hej', sys.stdin.readline())


fruit = 'Banan'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1

print(fruit[:])


jeff = ['yellow', 'green', 'blue', 'svart', 'vit', 'orange']


bilar = ['Volvo', 'Toyota', 'Skoda', 'Volkswagen', 'Range', 'Nissan']



print(len(jeff))
print(len(bilar))

jeffsBilar = [jeff, bilar]
print(jeffsBilar)

print(jeffsBilar[1][1], jeffsBilar[0][2])

bilar.append('Jaguar')
print(bilar)

bilar.sort()
print(bilar)

bilar.reverse()
print(bilar)

bilar.remove('Jaguar')
print(bilar)

bilar.remove(bilar[1])
print(bilar)

bilar.append('Toyota')
print(bilar)

print(bilar)

print(bilar[2:5])

print(bilar[:4])

print(bilar[2:])

print(bilar[5:])

print(len(bilar))



jeffsCars = jeff + bilar

print(jeffsCars)

inp = input('Välj en färg: ').lower()
for color in jeff:
    rätt = inp, ('finns ej i listan')
    if color == inp:
        rätt = (inp, ('finns i listan'))
        break
print(rätt)

myHome = (1, 2, 3, 4)

myCars = ('BMW', 'Volvo', 'Volkswagen', 'Toyota')

myCars = list(myCars)
print(myCars)

myHome = list(myHome)
print(myHome)


ifrunning = True
while ifrunning:
    inp = int(input('Vad vill du räkna?\n 1. Addition \n 2. Multiplikation\n 3. Exponentiel \n 4. Avsluta\n Val: '))
    if inp == 1:
        inp2 = int(input('Välj första talet: '))
        inp3 = int(input('Välj andra talet: '))
        print(inp2, '+', inp3, '=', inp2 + inp3)
        inp4 = input('Vill du testa igen? (j/n)')
        if inp4 == 'j':
            continue
        elif inp4 == 'n':
            print('Då var vi klara')
            break
        else:
            print('Var du rolig nu eller?')
    elif inp == 2:
        inp2 = int(input('Välj första talet: '))
        inp3 = int(input('Välj andra talet: '))
        print(inp2, '*', inp3, '=', inp2 * inp3)
        inp4 = input('Vill du testa igen? (j/n)')
        if inp4 == 'j':
            continue
        elif inp4 == 'n':
            print('Då var vi klara')
            break
        else:
            print('Var du rolig nu eller?')
    elif inp == 3:
        inp2 = int(input('Välj tal: '))
        print(inp2, '^', inp2, '=', inp2 ** inp2)
        inp4 = input('Vill du testa igen? (j/n)')
        if inp4 == 'j':
            continue
        elif inp4 == 'n':
            print('Då var vi klara')
            break
        else:
            print('Var du rolig nu eller?')
    elif inp == 4:
        print('Då var vi klara')
        break


ifrunning = True
while ifrunning:
    try:
        inp = int(input('Vad vill du räkna?\n 1. Addition \n 2. Multiplikation\n 3. Exponentiel \n 4. Avsluta\n Val: '))
    except:
        print('Vad har vi sagt om att dricka innan lunch..? Välj ett tal istället')
        continue

    if inp == 4:
        print('Ok, då var vi klara...')
        ifrunning = False
        break
    inp2 = int(input('Välj första talet: '))
    inp3 = int(input('Välj andra talet: '))
    if inp == 1:
        print(inp2, '+', inp3, '=', inp2 + inp3)

    elif inp == 2:
        print(inp2, '*', inp3, '=', inp2 * inp3)

    elif inp == 3:
        print(inp2, '^', inp2, '=', inp2**inp2)

    inp4 = ()
    while inp4 != 'j' and inp4 != 'n':
        inp4 = input('Vill du fortsätta? (j/n)')
        if inp4 == 'n':
            print('Ok, då var vi klara...')
            break
        elif inp4 == 'j':
            pass
        else:
            print('Var du rolig nu eller? prova igen...')
    if inp4 == 'n':
        break
        
        
person = {'Namn': 'Emil',
          'Ålder': '26',
          'Yrke': 'Student',
          'Ort': 'Tyresö',
          'Civilstånd': 'I förhållande'}
print(person.keys())
print(person.values())
print(person)
print(person['Namn'])
print(person.get('Ost'))
print(person.get('Emil'))
person['Namn'] = 'John'
print(person)


x = "Nackademin \"i Solna."
print(x)

y = Det här är massa text.
Flera rader text.
Kul med så mycket text."
print(y)

print(y + x)

num = 10123982718371287189471984389432984
print(num)
print(type(num))

var = 1.98197483463275647564985614895613475634178561478562178561278
print(var)
print(type(var))

c = "10"
print(c)
print(type(c))
print(type(int(c)))

z = [input('Skriv ett värde \n> ')for i in range(3)]
print(z)


fl = [1, 2, 3]
fl = []
print(fl)

x = [i**i for i in range(10)]
print(x)
for i in range(len(x)):
    print(x[i])
    
ult_list = [[i for i in range(5)], [i for i in range(10)]]
print(ult_list)


lis1 =[1,2,3]
lis2 =['röd', 'blå', 'gul']
lis3 =[4,5,6]
allalis = [lis1, lis2, lis3]
print(allalis)
print(allalis[0], allalis[1], allalis[2])
print(allalis[0][1], allalis[1][1], allalis[2][1])


for r in range(5):
    print()
    for k in range(5):
        print(str(r)+':'+str(k), "", end="")

y = [[i for i in range(3)]for i in range(3)]
print(y)

x = [[i, i, i]for i in range(3)]
print(x)


lista = [20, 'solna', 30.43, 0.42, 'Nackademin', 345]
for i in range(0, 6):
    print(lista[i])

lista2 = [[12, 30.43], ['Stockholm', 345]]
skrivlis = lista2[0] + lista2[1]
for i in skrivlis:
    print(i)
print()

for e in lista2:
    for i in e:
        print(i, end=" ")

x = 4
y = 20
if (x <= y) and y < 30 or x < 5:
    print('Stämmer')
else:
    print('Stämmer inte')

while x == 10 and y == 20 or y < 30:
    print('JA!')
    break

x = 3
y = 4

while (x == 2) or x < 5 and y < 5:
    if y == 4:
        print('YAAAAAS! Du hitta den magiska siffran!')
        break
    else:
        print('Fel siffra.')
        break

for i in range(11):
    time.sleep(0.5)
    if i == 3:
        print('Du har nått 3! Bara 7 kvar!')
        continue
    elif i == 9:
        print('Bara 1 kvar!!! snart framme!')
        continue
    print(i)

x = 1000
y = 40
c = ((x-y)/100)
print(c)

print(x*(y/100))

beviljat = 0
kolla = True
while kolla:
    age = input('Hej!\nVar god ange ålder: ')
    try:
        age = int(age)
        if age <= 17:
            print('Du måste vara minst 18 år gammal för att ta ett lån hos oss.')
            continue
        elif age >= 18:
            pass
    except:
        print('Var god ange siffror')
        continue
    while age >= 18:
            kalk = int(input('Hur mycket vill du låna?\n>>> '))
            if (kalk >= 1000) and kalk <= 1498:
                kalkmr = (kalk * (3/100))
                print('lån:', kalk, 'ränta:', kalkmr, 'kr', 'totalt', kalk+kalkmr, 'kr')
                time.sleep(0.5)
                beviljat = 1
                kolla = False
                break
            elif (kalk >= 434) and kalk <= 720:
                kalkmr = (kalk * (6.3/100))
                print('lån:', kalk, 'ränta:', kalkmr, 'kr', 'totalt', kalk+kalkmr, 'kr')
                time.sleep(0.5)
                beviljat = 1
                kolla = False
                break
            elif (kalk >= 721) and kalk <= 999:
                print('Vi godkänner endast i mellan 434kr-720kr, samt 1000kr-1498kr\nSjukt specifikt, jag vet...')
            else:
                print('Vi godkänner endast lån mellan 434 och 1498kr')
while beviljat == 1:
    inp = input('Vill du ta detta lån?').lower()
    while inp:
        if inp == 'ja' or inp == 'j':
            print('Behandlar')
            for i in range(random.randint(3, 10)):
                print(" ", end="-")
                time.sleep(0.5)
                continue
            print('\nGrattis!')
            time.sleep(0.5)
            print('Ditt lån kommer att finnan tillgängligt om 1-3 bankdagar')
            time.sleep(2)
            exit()
        elif inp == 'nej' or inp == 'n':
            inp2 = input('Vill du ta ett annat lån?')
            if inp2 == 'ja' or inp2 == 'j':
                kolla = True
                break
            else:
                print('VI VILLE ÄNDÅ INTE HA DINA PENGAR!')
                time.sleep(0.5)
                exit()


age = input('Ange ålder: ')
try:
    age = int(age)
    if age >= 2:
        print('Du får ha kalas!')
    elif age >= 16:
        print('Är inte du lika gammal för att ha kalas?')
    elif age >= 100:
        print('IT\'S NOT SAFE!')
    else:
        print('Nae. Här blir det inget kalas.')
except:
    age = str(age)
    print('Var god ange siffror...')


x = 10
z = 20
c = 30
if (x == 10) or z == 10 or c == 40:
    print('Hej')
    

x = 'N'
z = 'ost'
s = 13
d = 0.14000
g = 0.14000
a = 'computer'
print(2*'\n', '%c%s' % (x, z))
print("%c är min favorit och %s med siffran %d på %.5f och %r och %s" % ('x', z, s, d, g, sorted(a)))
print(a.upper())


person = {'namn': 'Emil', 'age': 26}

mening = 'Mitt namn är {} och jag är {} år gammal'.format(person['namn'],person['age'])
print(mening)

mening = 'Mitt namn är {0} och jag är {1} år gammal'.format(person['namn'],person['age'])
print(mening)

tag = 'h1'
text = 'This is a headline'

mening = '<{0}>{1}</{0}>'.format(tag, text)
print(mening)

person = {'namn': 'Emil', 'age': 26}

mening = 'Mitt namn är {0[namn]} och jag är {1[age]} år gammal'.format(person, person)
print(mening)

class person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = person('Emil','26')

mening = 'Mitt namn är {0.name} och jag är {0.age} år gammal'.format(p1)
print(mening)


mening = 'Mitt namn är {name} och jag är {age} år gammal'.format(name='Emil', age='26')
print(mening)


person = {'name': 'Emil', 'age': 26}
mening = 'Mitt namn är {name} och jag är {age} år gammal'.format(**person)
print(mening)


for i in range(1, 11):
    mening = 'Värdet är {}'.format(i)
    print(mening)


pi = 3.14159265
mening = 'Pi är lika med {:.2f}'.format(pi)
print(mening)


sentence = '1 MB is equal to {:,} bytes'.format(1000**2)
print(sentence)


mening = 'Mitt namn är {name} och är {age} gammal.'.format(name='Emil', age='26')
print(mening)
'''


class Car():
    wheels = 4
    car_count = 0

    def __init__(self, model, price):
        self.model = model
        self.price = price
        self.equipment = []

        Car.car_count += 1

    def present_car(self):
        print('Model: {m}, Price: {p}'.format(m=self.model, p=self.price))

    @staticmethod
    def calculate_price_reduction(aPrice):
        return int(aPrice * 0.66)

    def reduce_price(self):
        self.price = self.calculate_price_reduction(self.price)
        return 'Priset för {c} är nu {p}'.format(c=self.model, p=self.price)

    def add_equipment(self, new_equipment):
        self.equipment.append(new_equipment)

    def print_equipment(self):
        for eq in self.equipment:
            print('* ' + eq)

    def get_model(self):
        return self.model

    def get_price(self):
        return self.price

    def set_model(self, model):
        self.model = model

    def set_price(self, price):
        self.price = price

    def __add__(self, other):
        return self.price + other.get_price()

    def __iadd__(self, other):
        self.price += other.get_price()
        return self


bmw = Car('BMW', 100000)
volvo = Car('Volvo', 150000)

bmw += volvo
print(bmw.get_price())


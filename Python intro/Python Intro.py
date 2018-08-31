import random
import sys
import os

'''
x = 30
if x == 30:
    print('Du har 30!')

x = 20
if x != 30:
    print('Du har inte 30!')

x = 20
if x < 30:
    print('Du har mindre än 30!')

x = 40
if x > 30:
    print('Du har mer än 30!')

x = 25
if x <= 30:
    print('Du har mindre än eller 30!')

x = 35
if x >= 30:
    print('Du har mer eller 30!')

x = 30
y = 30
if x == 30 and y == 20:
    print('Du har 30 och 20!')
else:
    print('Du har inte 30 och 20!')

x = 45
y = 30
if x == 50 or y == 30:
    print('Du har åtminstone en rätt!')

name = 'Emil'
lastName = 'Jacobsson'
age = 26
if age == 26 and name == 'Emil' and lastName == 'Jacobsson':
    print('Du är', age, 'år gammal och heter', name, lastName)
elif age != 26 and name == 'Emil' and lastName == 'Jacobsson':
    print('Du heter',name,lastName,'men är inte 26 år gammal')
elif age == 26 and name != 'Emil' and lastName == 'Jacobsson':
    print('Du är', age,'och heter', lastName, 'men inte Emil i förnamn')
elif age == 26 and name == 'Emil' and lastName != 'Jacobsson':
    print('Du är', age,'år gammal och heter', name, 'men inte Jacobsson i efternamn')
else:´
    print('Vem är du?')

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
'''

print('Mata in ditt namn: ')
print('Hej', sys.stdin.readline())

# Lektion 1

# Övning 1

a = 1
b = 2
c = a+b

print(c) # 3

# Övning 2

a = 5
b = a # b tar värdet 5
a = 7 # a byter till värde 7
c = a + b

print(c) # 12

# Övning 3

a = 7 * 3 + 1
'''
prioriterings regeln ger 7 * 3 = 21 + 1 = 22
'''

print (a) # 22

# Övning 4

a = 20 / 4 * 2
'''
För att undvika missförstånd kan man ange paranteser för att
 klargöra vilken ordning man vill beräkna talen
 '''

print(a) # 10.0
print(5+2, 5-2, 5*2, 5/2, 5%2, 5**2, 5//2, 1 + 2 - 3 * 2, ((1 + 2 - 3) * 2))

# Övning 5

a = 9
b = 2
c = a/b # Här delar vi variablerna med varandra

print(c) # 4.5

# Övning 6

a = 2
b = 3
c = a/b

print(c) # 0.6666666666

# Övning 7

a = 'Hej'
b = 'Erik'
c = a + b

print(c) #HejErik

# Övning 8

a = 0
a = a + 1 # a får värde 1
a = a - 2 # subtrahera 2 från 1 till -1
print(a) # -1

# Övning 9

a = 0
# a++ : a blir här 1
# a++ : a blir här 2
# a-- : a blir här 1
# a = a + a : 1 + 1
# a = 2

# Övning 10

a = 1
b = a       # Värdet på b är nu 1
a = a + b   # a blir: 1(a)+1(b), a är nu 2
c = a + b   # c = 2(a) + 1(b)
print(c)

# Övning 11

a = "Emil"
b = "Jacobsson"
c = a
a = b
b = c
print(a,b)

a,b = b,a
print(a,b)
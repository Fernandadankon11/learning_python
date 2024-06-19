arret = -1
nbre_salaire = 0
total_salaire = 0

while True:
    salaire = int(input("entrez les salaires un par un. Tapez -1 pour arrêter  "))
    if salaire == arret:
        break
    nbre_salaire += 1
    total_salaire += salaire

moyenne = total_salaire / nbre_salaire

if moyenne > 0:
    print("le salaire moyen est : ", moyenne)
else: 
    print("le salaire est négatif ou nul")


"""""

test = 18
nbre_plis = int(input("Combien de plis sont-ils nécessaires pour se rendre sur la Lune ? : "))

while nbre_plis != test:
        print("mauvaise réponse")
        nbre_plis = int(input("Combien de plis sont-ils nécessaires pour se rendre sur la Lune ? : "))
print("Bravo") 


import turtle
for i in range(4):
    turtle.forward(100)
    turtle.left(90)
turtle.done()


import math

first_letter = input("veuillez entrer la première lettre de votre figure géométrique")
arrete = float(input("veuillez entrer la longueur de l'arrête de votre figure géométrique"))

if first_letter == "T":
    volume = (math.sqrt(2) / 12) * (arrete ** 3)
    print("le volume de votre tétraèdre est : ", volume)
elif first_letter == "C":
    volume = arrete ** 3
    print("le volume de votre Cube est : ", volume)
elif first_letter == "O":
    volume = (math.sqrt(2) / 2) * (arrete ** 3)
    print("le volume de votre Octaèdre est : ", volume)
elif first_letter == "D":
    volume = (( 15 + (7 * math.sqrt(5))) / 4) * (arrete ** 3)
    print("le volume de votre Dodécaèdre est : ", volume)
elif first_letter == "I":
    volume = (( 5 * (3 + math.sqrt(5))) / 12) * (arrete ** 3)
    print("le volume de votre Dodécaèdre est : ", volume)
else: print("Polyèdre non connu")



le casino 

import random 

pari_type =  int(input("Entrez un numéro pour votre type pari"))
mise = 10

if pari_type == 1: 
    print("Vous avez choisi de parier sur le numéro sortant   ")
    choix1 = int(input("Choisissez un nombre entre 0 et 12 "))
    tirage = random.randint(0,12)    
    print("Tirage : ", tirage)  
    print("Votre choix :", choix1)
    if choix1 == tirage :
        print("vous avez gagné ", mise * 12, "euros")
    else: print("vous avez perdu")

elif pari_type == 2:
    print("Vous avez choisi de parier sur la parité du numéro gagnant")
    choix2 = int(input("Choisissez 13 pour pair ou 14 pour impair"))
    tirage = random.randint(0,12) 
    print("Tirage : ", tirage)  
    print("Votre choix :", choix2)
    if choix2 == 13 and tirage % 2 == 0 : 
        print("vous avez gagné ", mise * 2, " euros")
    elif choix2 == 14 and tirage % 2 != 0:
        print("Vous avez perdu")
    else : print("veuillez faire un bon choix la prochaine fois")

elif pari_type == 3:
    print("Vous avez choisi de parier sur la couleur du numéro gagnant")
    rouges = {1, 3, 5, 7, 9, 12}
    noirs = {2, 4, 6, 8, 10, 11}
    tirage = random.randint(0,12)   
    
    choix3 = int(input("Choisissez 15 pour la couleur rouge ou 16 pour la couleur noire  : "))
    print("Tirage : ", tirage)  
    print("Votre choix :", choix3)
    if choix3 == 15 and tirage in rouges:
        print("Bravo ! Vous avez gagné :", mise * 2, " euros")
    elif choix3 == 16 and tirage in noirs :
        print("Bravo ! Vous avez gagné :", mise * 2, " euros")
    else:
        print("Vous avez perdu")    
else:
    print("Vous n'avez pas choisi un bon numéro. Veuillez choisir un nombre entre 1, 2 et 3.") 


le casino


a =  int(input())
b = int(input())

if (a % b == 0) or (b % a == 0) : print("l'un est diviseur")
else: print("False")

a =  int(input())

if a % 2 == 0: print("True")
else: print("False")


a = int(input())
b = int(input())
c = int(input())

if c == 1 : print(a + b)
elif c == 2 : print(a - b)
elif c == 3 : print (a * b)
elif c == 4 : print (a ** 2 + a * b)
else: print("Erreur")

temperature = int(input("Température maximale"))

if temperature > 0 and temperature <=10: 
    print("il va faire frais")

elif temperature < 0 : print("il va faire froid")




a = int(input())
b = int(input())
c = int(input())

if a == b:
    print(a)
elif a == c:
    print(a)
elif b == c:
    print(b)

import random 

r = random.randint(0,5)

x = int(input("Devinez le nombre"))

if r == x : print("gagné")
else: print("perdu")

import math 

a = float(input("Entrez la valeur de a"))
b = float(input("Entrez la valeur de b"))
c = float(input("Entrez la valeur de c"))

delta = b ** 2 - (4 * a * c)

if delta > 0 :
    x1 = (-b - math.sqrt(delta)) / (2 * a)
    x2 = (-b + math.sqrt(delta)) / (2 * a)
    print("L'équation admet deux solutions réelles : x1 = ", x1, " et x2 = ", x2)

elif delta == 0 :
    x = -b / (2 * a)
    print("La solution de l'équation est x = ", x)

else:
    print("L'équation n'a pas de racine réelle")


import math 
r = float(input())
vol = (4/3) * math.pi * r ** 3
print(vol)

print("Hello Word")
print("Aujourd'hui")
print("C'est \"Dommage\"")
print("Hum  \\o/")

x = 36
produit = int(36*36)
div_entiere = 36 // 5
expo = 15 ** 15
pi = 3.14159
mon_texte = "Bonjour"

nombre1 = float(input())
nombre2 = float(input())
res = (nombre1 + nombre2)/2
print(res)

a = float(input())
b = float(input())
c = float(input())
d = (b * c) / a

print(d)

# Crée une fenêtre pour le dessin
window = turtle.Screen()
window.bgcolor("white")

# Crée une tortue
tortue = turtle.Turtle()
tortue.shape("turtle")
tortue.color("blue")

# Dessine un carré
for _ in range(4):
    tortue.forward(100)  # Avance de 100 unités
    tortue.right(90)     # Tourne à droite de 90 degrés

# Ferme la fenêtre en cliquant dessus
window.exitonclick()

import turtle

window = turtle.Screen()
window.bgcolor("white")

# Crée une tortue
tortue = turtle.Turtle()
tortue.shape("turtle")

for _ in range(3):
    tortue.forward(100)
    tortue.right(120)

window.exitonclick()

x = int(input())
y = int(input())
z = float(input())
t = float(input())

print("\n",x - y)
print("\n",x + z)
print("\n", x + z)
print("\n", z + t)
print("\n", x * z)
print("\n", x / 2)
print("\n", x / (y + 1))
print("\n", ((x + z) * z) / 4 * y)
print("\n", x ** (-1/2))
"""""






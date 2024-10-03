# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 10:45:57 2024

@author: USER
"""

"""
Écrivez une classe Python nommée Point3D définie par x, y et z. 
Définissez une méthode qui renvoie (x, y, z). 
Cela indique à Python de représenter cet objet dans le format suivant : (x, y, z). 
Créez ensuite une variable nommée my_point contenant une nouvelle instance de Point3D avec x=1, y=2 et z=3 et imprimez-la.

Écrivez une classe Python nommée Rectangle construite par une longueur et une largeur. 
Définissez deux méthodes, area et circumstance, qui calculeront l'aire et le périmètre du rectangle. 
Créez ensuite une variable nommée my_rectangle contenant une nouvelle instance de Rectangle avec width=3 et length=4 
et calculez à la fois area et circumstance (l'aire devrait être 3*4=12 et le périmètre 2*(3+4)=14).
                                            
Écrivez une classe Python nommée Circle construite par son centre O et son rayon r. 
Définissez deux méthodes, area et circumference, qui calculeront l'aire et le périmètre du cercle, 
et une méthode Inside() qui vous permettra de tester si un point A(x, y) appartient au cercle C(O, r) ou non.
Supposons que nous souhaitons modéliser un compte bancaire avec prise en charge des opérations de dépôt 
et de retrait. Créons une classe Python nommée Bank définie par son solde. Définissons deux méthodes, 
deposit et withdraw, pour calculer le nouveau montant de chaque opération.

"""

print()
print("EXERCICE 1")
print()
class Point3D:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        
        
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    
my_point = Point3D(1, 2, 3)
print(my_point)

print()
print("EXERCICE 2")
print()

class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

    def circumference(self):
        return 2 * (self.width + self.length)

# Créer une instance de Rectangle
my_rectangle = Rectangle(width=3, length=4)

# Calculer l'aire et le périmètre
rectangle_area = my_rectangle.area()
rectangle_circumference = my_rectangle.circumference()

# Afficher les résultats
print(f"Aire: {rectangle_area}")  # Aire: 12
print(f"Périmètre: {rectangle_circumference}")  # Périmètre: 14

print()
print("EXERCICE 3")
print()

import math

class Circle:
    def __init__(self, centre, rayon):
        self.centre = centre  # center est un tuple (x, y)
        self.rayon = rayon

    def area(self):
        return math.pi * self.rayon ** 2

    def circumference(self):
        return 2 * math.pi * self.rayon

    def inside(self, point):
        # point est un tuple (x, y)
        distance_carre = (point[0] + self.centre[0]) ** 2 + (point[1] + self.centre[1]) ** 2
        return distance_carre <= self.rayon ** 2

# Créer une instance de Circle
my_circle = Circle(centre=(0, 0), rayon=5)

# Calculer l'aire et la circonférence
circle_area = my_circle.area()
circle_circumference = my_circle.circumference()

# Vérifier si le point A(3, 4) est à l'intérieur du cercle
point_A = (3, 4)
is_inside = my_circle.inside(point_A)

# Afficher les résultats
print(f"Aire: {circle_area:.1f}")  # Aire du cercle
print(f"Circumférence: {circle_circumference:.1f}")  # Circonférence du cercle
print(f"Le point A{point_A} est à l'intérieur du cercle : {is_inside}")  # Vérification du point


print()
print("EXERCICE 4")
print()


class Bank:
    def __init__(self, solde_initial=0):
        self.balance = solde_initial

    def deposit(self, montant):
        if montant > 0:
            self.balance += montant
            print(f"Dépôt de {montant} fr. Nouveau solde: {self.balance} fr")
        else:
            print("Le montant du dépôt doit être positif.")

    def withdraw(self, montant):
        if montant > 0:
            if montant <= self.balance:
                self.balance -= montant
                print(f"Retrait de {montant} fr. Nouveau solde: {self.balance} fr")
            else:
                print("Fonds insuffisants pour effectuer ce retrait.")
        else:
            print("Le montant du retrait doit être positif.")

# Exemple d'utilisation de la classe Bank
mon_compte = Bank(solde_initial=100000)  # Création d'un compte avec un solde initial de 100

# Dépôts et retraits
mon_compte.deposit(50000)   # Dépôt de 50
mon_compte.withdraw(30000)  # Retrait de 30
mon_compte.withdraw(150000) # Tentative de retrait de 150, fonds insuffisants
mon_compte.deposit(-20000)  # Tentative de dépôt d'un montant négatif

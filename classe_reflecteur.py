#----------------------------------------------------
# Classe Reflecteur
# réalisée le 18/01/2022
# par Jean-Christophe BONNEFOY
# Python : Version 3.10
#----------------------------------------------------
# -*- coding: utf-8 -*-

# ---------------------------------
# -- CONSTANTES DES REFLECTEURS
# ---------------------------------
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Description des deux réflecteurs (Codage historique)
REFLECTEURS = [{"id" : "UKW-B", "lettres" : "YRUHQSLDPXNGOKMIEBFZCWVJAT" },
          {"id" : "UKW-C", "lettres" : "RDOBJNTKVEHMLFCWZAXGYIPSUQ" }]

class Reflecteur:
    def __init__(self, num_reflecteur):
        self.id = ""
        self.Set_reflecteur(num_reflecteur)
    
    def Set_reflecteur(self, numero) :
        """
            Sélection d'un reflecteur (numero de 1 à 2) 
            Affecte simplement les attributs :
                - reflecteur à une liste des indices des lettres du rotor choisi
                - id à l'Id du reflecteur choisi
            
            Exemple : Set_reflecteur(2) mettra :
                - reflecteur à renvoie [17, 3, 14, 1, 9, 13, 19, 10, 21, 4, 7, 12, 11, 5, 2, 22, 25, 0, 23, 6, 24, 8, 15, 18, 20, 16]
                - id à "UKW-C"
        """
        self.reflecteur = REFLECTEURS[numero -1]["lettres"]
        self.id = REFLECTEURS[numero - 1]["id"]

    def Get_num_reflecteur(self):
        """
            Retourne le numéro du réflecteur affecté :
                - 1 si UKW-B
                - 2 si UKW-C
        """
        if self.id == "UKW-B":
            val = 1
        elif self.id == "UKW-C":
            val = 2
        return val
        
                   
    def passage_dans_reflecteur(self, valeur):
        """
        Fonction retournant la nouvelle valeur après passage dans le reflecteur
        Paramètres :
            'valeur' est un entier correspondant à la lettre en entrée du reflecteur
        Résultat :
            Renvoie un tuple composé de la lettre codée et la 'valeur' modifiée par le reflecteur
        
        Exemple : l'appel à la fonction passage_dans_reflecteur(1) sur le rotor [17, 3, 14, 1, 9, 13, 19, 10, 21, 4, 7, 12, 11, 5, 2, 22, 25, 0, 23, 6, 24, 8, 15, 18, 20, 16] 
                  renvoie 'D', 3
        
        """
        lettre_codee = self.reflecteur[valeur]
        nouvelle_valeur = ALPHABET.index(lettre_codee)
        return lettre_codee, nouvelle_valeur
    
    
if __name__ == "__main__":
    mon_reflecteur = Reflecteur(2)    
    print(mon_reflecteur.reflecteur)
    print(mon_reflecteur.id)
    print(mon_reflecteur.passage_dans_reflecteur(1))

    
    
    

#----------------------------------------------------
# Classe Rotor
# réalisée le 18/01/2022
# par Jean-Christophe BONNEFOY
# Python : Version 3.10
#----------------------------------------------------

# -*- coding: utf-8 -*-

# ----------------------------
# -- CONSTANTES DES ROTORS
# ----------------------------
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Description des cinq rotors de la machine (Codage historique)
ROTORS = [{"id" : "I", "lettres" : "EKMFLGDQVZNTOWYHXUSPAIBRCJ", "encoche" : "Q" },
          {"id" : "II", "lettres" : "AJDKSIRUXBLHWTMCQGZNPYFVOE", "encoche" : "E" },
          {"id" : "III", "lettres" : "BDFHJLCPRTXVZNYEIWGAKMUSQO", "encoche" : "V" },
          {"id" : "IV", "lettres" : "ESOVPZJAYQUIRHXLNFTGKDCMWB", "encoche" : "J" },
          {"id" : "V", "lettres" : "VZBRGITYUPSDNHLXAWMJQOFECK", "encoche" : "Z" }]

class Rotor:
    def __init__(self, num_rotor):
        self.id = 0
        self.rotor = []
        self.encoche = ""

        self.Set_rotor(num_rotor)
        self.poscur = 0
    
    def Set_rotor(self, numero) :
        """
            Sélection d'un rotor (numero de 1 à 5) 
            Affecte simplement les attributs :
                - rotor à une liste des indices des lettres du rotor choisi
                - id à l'Id du rotor choisi
                - encoche à l'indice de la lettre de l'encoche du rotor choisi
            
            Exemple : Set_rotor(3) mettra :
                - rotor à [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]
                - id à "III"
                - encoche à 21
        """
        self.id = ROTORS[numero - 1]["id"]
        self.rotor = ROTORS[numero - 1]['lettres']
        self.encoche = ALPHABET.index(ROTORS[numero - 1]['encoche'])
        
    def Get_num_rotor(self) :
        """
            Retourne le numéro du rotor :
                - 1 pour I
                - ...
                - 5 pour V
        """
        if self.id == "I":
            val = 1
        elif self.id == "II":
            val = 2
        elif self.id == "III":
            val = 3
        elif self.id == "IV":
            val = 4
        else:
            val = 5
        return val

        
    def decalage_un_rang(self):
        """
        Décalage à gauche d'un cran la position du rotor
        Effet :
            La liste rotor est modifiée : le premier élément devenant le deuxieme, etc... et le dernier élément devenant le premier.
    
        Exemple : l'appel à la fonction decalage_un_rang sur le rotor [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]
                  change la liste rotor en la suivante [3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14, 1]
        
        """
        self.rotor = self.rotor[1:] + self.rotor[0]

    def pos_init_rotor(self, config_letter):
        """
        Réalise l'initialisation du rotor par décalage de 'pos' crans
        Paramètres :
            'pos' est un entier
        Effet :
            décale le rotor à gauche de 'pos' crans
            
        Exemple : l'appel à la fonction pos_init_rotor(3) sur le rotor [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]
                  change la liste rotor en la suivante [7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 14, 1, 3, 5]
        
        """
        print(config_letter)
        pos = self.rotor.index(config_letter)
        print(pos)
        # Effectuer le décalage
        self.rotor = self.rotor[pos:] + self.rotor[:pos]
        print(self.rotor)
        
    def passage_dans_rotor(self, valeur):
        """
        Fonction retournant la nouvelle valeur après passage dans le rotor
        Paramètres :
            'valeur' est un entier correspondant à la lettre en entrée du rotor
        Résultat :
            Renvoie un tuple formé de la lettre codée et de la 'valeur' modifiée par le rotor
        
        Exemple : l'appel à la fonction passage_dans_rotor(3) sur le rotor [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14] 
                  renvoie 'H', 7
        
        """
        lettre_codee = self.rotor[valeur]
        nouvelle_valeur = ALPHABET.index(lettre_codee)
        
        self.poscur = (self.poscur + 1) % 26

        return lettre_codee, nouvelle_valeur


        
    def passage_inverse_dans_rotor(self, valeur):
        """
        Fonction retournant la nouvelle 'valeur' après le passage dans un rotor dans le sens du retour (inverse)
        Paramètres :
            'valeur' est un entier correspondant à la lettre en entrée du rotor
        Résultat :
            Renvoie un tuple formé de la lettre codée et de l'indice de 'valeur' du rotor
            
        Exemple : l'appel à la fonction passage_inverse_dans_rotor(11) sur le rotor [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]
                  renvoie 'L', 5
        
        """ 
        lettre_entree = ALPHABET[valeur]
        nouvelle_valeur = self.rotor.index(lettre_entree)
        return lettre_entree, nouvelle_valeur
    
    
    
if __name__ == "__main__":
    mon_rotor = Rotor(3)    
    print(mon_rotor.rotor)
    print(mon_rotor.id)
    print(mon_rotor.encoche)
    print(mon_rotor.passage_dans_rotor(3)) # chiffrage de la lettre D
    print(mon_rotor.passage_inverse_dans_rotor(11)) # chiffrage inverse de la lettre V
        
    

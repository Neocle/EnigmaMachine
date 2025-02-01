#----------------------------------------------------
# Classe Enigma
# réalisée le 18/01/2022
# par Jean-Christophe BONNEFOY
# Python : Version 3.10
#----------------------------------------------------
# -*- coding: utf-8 -*-
import classe_rotor as rtr
import classe_reflecteur as rfl

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Enigma:
   
    def __init__(self, rotor_g, rotor_c, rotor_d, refl):
        self.cablage_lettres = []           
        self.SetRotors(rotor_g, rotor_c, rotor_d)
        self.SetReflecteur(refl)

    def SetRotors(self,num_g,num_c,num_d):
        self.rotor_g = rtr.Rotor(num_g)
        self.rotor_c = rtr.Rotor(num_c)
        self.rotor_d = rtr.Rotor(num_d)

    def GetNumRotorGauche(self):
        return self.rotor_g.Get_num_rotor()
    
    def GetNumRotorCentre(self):
        return self.rotor_c.Get_num_rotor()
    
    def GetNumRotorDroite(self):
        return self.rotor_d.Get_num_rotor()

    def SetReflecteur(self,num_refl):
        self.reflecteur = rfl.Reflecteur(num_refl)

    def GetNumReflecteur(self):
        return self.reflecteur.Get_num_reflecteur()
    
    def Set_Configuration_depart(self, configrotor_g, configrotor_c, configrotor_d):
        """
        Configuration de la position initial des 3 rotors
        Paramètres :
            configrotor_g : lettre sur le rotor de gauche
            configrotor_c : lettre sur le rotor du centre
            configrotor_d : lettre sur le rotor de droite
        Résultat :
            decale d'autant de positions necessaires chaque rotor
        """
        print((configrotor_g), (configrotor_c), (configrotor_d))
        self.rotor_g.pos_init_rotor(configrotor_g)
        self.rotor_c.pos_init_rotor(configrotor_c)
        self.rotor_d.pos_init_rotor(configrotor_d)


    def GetLettreInitRotorGauche(self):
        return ALPHABET[self.rotor_g.poscur]

    def GetLettreInitRotorCentre(self):
        return ALPHABET[self.rotor_c.poscur]
    
    def GetLettreInitRotorDroite(self):
        return ALPHABET[self.rotor_d.poscur]

    def Set_cablage_depart(self, cables):
        """
        Configuration du branchement du câblage par l'utilisateur : 6 câbles relient les 6 paires de lettres
        Paramètres :
            Entrée au clavier d'une chaine de 12 caractères en MAJUSCULE
        Résultat :
            Affecte l'attribut cablage_lettre avec un tableau contenant les valeurs numériques correspondant aux caractères de la chaine entrée
            
            exemple : si cable = la chaine 'AHBICJDKELFM' (cela veut dire que l'on a relié par un cable les
                      touches A à H, B à I, etc..
                      l'attribut cablage_lettres est affecté par la liste [0, 7, 1, 8, 2, 9, 3, 10, 4, 11, 5, 12]
        """
        cablage_num = []
        cablage_num = [ALPHABET.index(c) for c in cables]
        
        self.cablage_lettres = cablage_num

    def Get_cablage_depart(self):
        cablage_l = []
        cablage_l = [ALPHABET[c] for c in self.cablage_lettres]
        return "".join(cablage_l)
        
        
    def val_apres_cablage_depart(self, valeur):
        """
        Fonction de codage/décodage des lettres câblées
        Paramètres :
            'valeur' est un entier correspondant à la lettre cablée ou non
        Résultat :
            Renvoie un tuple composé de lettre  et de la nouvelle valeur (inchangée si elle n'est pas dans la liste du câblage)
                                        
        Exemple : si cablage_lettres = [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], l'appel à la fonction val_apres_cablage_depart(0) 
                  change 'valeur' en 1 puisque la lettre 'A' est cablée avec 'B'.
                  tandis que l'appel à la fonction val_apres_cablage_depart(2, [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
                  ne change pas 'valeur' et reste donc à 2 puisque la lettre 'C' n'est pas cablée.
        """
        nouv = valeur
        if nouv in self.cablage_lettres:
            n = self.cablage_lettres.index(valeur)
            if n % 2 == 0:
                nouv = self.cablage_lettres[n + 1]
            else:
                nouv = self.cablage_lettres[n - 1]
        return ALPHABET[nouv], nouv
    
    
    def lettre_en_nombre(self, lettre):
        if isinstance(lettre, str) and len(lettre) == 1:
            return ALPHABET.index(lettre)
        raise ValueError(f"Valeur incorrecte pour lettre_en_nombre: {lettre}")

    def nombre_en_lettre(self, nombre):
        return ALPHABET[nombre % 26]

    def rotation_des_rotors(self):
        """ Fait tourner les rotors en fonction de la lettre entrée. """

        self.rotor_d.decalage_un_rang()

        if self.rotor_d.poscur == self.rotor_d.encoche:
            self.rotor_c.decalage_un_rang()

        if self.rotor_c.poscur == self.rotor_c.encoche:
            self.rotor_g.decalage_un_rang()


    def passage_par_rotor(self, rotor, valeur):
        return rotor.passage_dans_rotor(valeur)

    def passage_inverse_par_rotor(self, rotor, valeur):
        return rotor.passage_inverse_dans_rotor(valeur)

    def Decodagelettre(self, lettre):
        if not isinstance(lettre, str) or len(lettre) != 1:
            raise ValueError(f"Lettre invalide reçue : {lettre}")

        print(f"\n--- Décryptage de '{lettre}' ---")
        v = self.lettre_en_nombre(lettre)
        print(f"Clavier : {lettre} -> {v}")

        self.rotation_des_rotors()
        v = self.passage_par_rotor(self.rotor_d, v)
        print(f"Rotor droit : {v}")

        v = self.passage_par_rotor(self.rotor_c, v[1])
        print(f"Rotor centre : {v}")

        v = self.passage_par_rotor(self.rotor_g, v[1])
        print(f"Rotor gauche : {v}")

        v = self.reflecteur.passage_dans_reflecteur(v[1])
        print(f"Réflecteur : {v}")

        v = self.passage_inverse_par_rotor(self.rotor_g, v[1])
        print(f"Rotor gauche inverse : {v}")

        v = self.passage_inverse_par_rotor(self.rotor_c, v[1])
        print(f"Rotor centre inverse : {v}")

        v = self.passage_inverse_par_rotor(self.rotor_d, v[1])
        print(f"Rotor droit inverse : {v}")

        lettre_decode = self.nombre_en_lettre(v[1])
        print(f"Sortie : {lettre_decode}")

        return lettre_decode
    


if __name__ == "__main__":
    print("\nMachine ENIGNMA M3")
    
    M3 = Enigma(5,3,1,2)
    M3.Set_Configuration_depart("J", "C", "B")
    M3.Set_cablage_depart("FT")
    
    ## Le message à décoder
    message = input("\nEntrez le message à décoder : ").upper()
    ch = ""
    for l in message:
        if l == " ":
            pass
        else:
            ch += M3.Decodagelettre(l)
    #on affiche par paquet de 5
    new_ch = ""
    for i in range(0, len(ch)):
        if (i%5 == 0) and (i != 0):
            new_ch += " "
            
        new_ch += ch[i]
    print(new_ch)

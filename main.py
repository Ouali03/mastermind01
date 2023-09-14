import random
print("Bienvenue dans le jeu mastermind !")
nbr_de_partie = 0
score=0


while True :  #cette boucle while c'est pour demander a l'utilisateur est ce que il veut joue ou rejouer  
    go = input("vueillez ecrire start pour rejouer une autre partie : ") 
    if str(go) == "start": # si l'utilasateur ecrit start le jeu va ce lancer 
        nbr_de_partie += 1  
    
    
        LC = []
        nbr_couleurs = int(input("veuillez donner le  nombre de couleur de la liste : " ))
        nbr_c = int(nbr_couleurs) 
        nbr_elem_code = int(input("veuillez donner le nombre d'element de code secret : "))
        nbr_e_c = int(nbr_elem_code)
        tent = input("veuillez donner le nombre maximal de tentatives : ")
        
        
        print("les couleurs possibles : Rouge : R / Bleu : B / Vert : V /Jaune : J / Noir : N / Orange : O / Gris : G")
        for i in range (0,nbr_c):
            couleur = str(input("donner la couleur "+ str(i) + " : "))# Demandez à l'utilisateur de saisir (nbr_e_c) couleurs
            LC.append(couleur) 
        
        
        code_c = "".join(random.choice(LC) for _ in range(nbr_e_c)) #générer le code couleur secret
        print(code_c)
        
        
        def evaluer_proposition(code, LC):
            bien_places = 0
            couleurs_correctes = 0
            
            for i in range(len(code)):
                if LC[i] == code[i]:
                    bien_places += 1
                
                    
                if LC[i] in code:
                    couleurs_correctes += 1

            return bien_places, couleurs_correctes
        
        
        
        while True:
            score+=1
            if score <= int(tent) :
                code = input("donner le code couleur : ")
                if len(code) != nbr_e_c :
                    print("Veuillez entrer une proposition valide de "+str(nbr_e_c)+" couleurs")
                    continue
                
                bien_places, couleurs_correctes = evaluer_proposition(code, LC)
                

                if bien_places == nbr_e_c:
                    print("Bravo ! Vous avez trouvé le code en {score} tentatives.")
                    break
                else:
                    print("Correct : {bien_places}")
                    print("Partiel : {couleurs_correctes}")
                    
                    
                    
                    
                    
                
                
    else :#si l'utilisateur n'ecrit rien ou n'import quoi, dans ce cas on quitte le jeu  
         print("à bientot")
         break
     
    
    
    
    

with open (".le_score.txt",'w') as fi: # ouvrire un fichier et sommer les score de toutes les parties
        fi.write(str(score) )
        fi.close()
with open (".Nombre_de_parties.txt", "w") as f:   #ouvrir un fichier et ecrire le nbr des parties  
        f.write(str(nbr_de_partie) )        
        f.close()





    
with open (".Nombre_de_parties.txt", "r") as f: # lire le fichier f
    contenu = f.read()   
    print("le nbr de partie joue : "+ contenu)
    f.close()
    
with open(".le_score.txt",'r') as fi: #lire le fichier fi
    contenu_2 = fi.read()
    print("le score dans chaque partie : " + contenu_2 )
    fi.close()

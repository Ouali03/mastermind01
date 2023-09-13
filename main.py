import random



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



score=-1
debut = True
while debut:
    score+=1
    if score <= int(tent) :
        code = input("donner le code couleur  sous la forme des  couleurs : ")
        if str(code) == code_c:
            print("Correct : "+ str(code) )
            break
        else :
            print("Partiel : "+ str(code))
    else :
        print("vous avez depasser nbr d'essais autorise")
        break
        
print("nombre de tentatives : "+ str(score))


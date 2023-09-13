import random
print("Les couleurs possible : Rouge, Vert, Bleu, Jaune, Mauve, Noir")

LC = ["R", "V", "B", "J", "M", "N"]
code_c = "".join(random.choice(LC) for _ in range(4))

print(code_c)
score=0
debut = True
while debut:
    score+=1
    if score <=12 :
        code = input("donner le code couleur  sous la forme des quatre couleurs : ")
        if str(code) == code_c:
            print("Correct : "+ str(code) )
            break
        else :
            print("Partiel : "+ str(code))
    else :
        print("vous avez depasser nbr d'essais autorise")
        break
        
print("nombre de tentatives : "+ str(score))


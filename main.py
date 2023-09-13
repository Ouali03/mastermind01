
print("Les couleurs possible : Rouge, Vert, Bleu, Jaune, Mauve, Noir")
print("VBRM")
LC= ["R" , "V" , "B" , "J" , "M" , "N"]
score=0
debut = True
while debut:
    score+=1
    if score <=12 :
        code = input("donner le code couleur  sous la forme des quatre couleurs : ")
        if str(code) == LC[1]+LC[2]+LC[0]+LC[4]:
            print("Correct : "+ str(code) )
            break
        else :
            print("Partiel : "+ str(code))
    else :
        print("vous avez depasser nbr d'essais autorise")
        break
        
print("nombre de tentatives : "+ str(score))
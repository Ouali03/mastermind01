def evaluer_proposition(code, LC):
    bien_places = 0
    couleurs_correctes = 0
    
    for i in range(len(code)):
        if LC[i] == code[i]:
            bien_places += 1
        
            
        if LC[i] in code:
            couleurs_correctes += 1

    return bien_places, couleurs_correctes




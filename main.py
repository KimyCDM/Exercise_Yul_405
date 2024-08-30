import random
exercise=-1
while exercise != 0:
    exercise = int(input('Quel exercise voulez-vous voir?(0 pour fermer):'))
    if exercise == 1:
        nom = input('Quel est votre nom:?')
        print('Bonjour', nom, '.Comment allez-vous?')
    elif exercise == 2:
        nombre1 = int(input('Quel est votre 1er chiffre?:'))
        nombre2 = int(input('Quel est votre 2eme chiffre?:'))
        print('Votre somme est', nombre1 + nombre2, )
    elif exercise == 3:
        nombre1 = int(input('Quel est votre 1er chiffre?:'))
        nombre2 = int(input('Quel est votre 2eme chiffre?:'))
        if nombre1 == 0 or nombre2 == 0:
            print('La reponse est indefini')
        else:
            print('La reponse est', nombre1 / nombre2, )
    elif exercise == 4:
        npair = 0
        nimpair = 0
        for i in range(1, 10):
            if i % 2 == 0:
                print(i, 'est pair')
                npair = npair + 1
            else:
                print(i, 'est impair')
                nimpair = nimpair + 1
        print('Il y a', npair, 'pairs et', nimpair, 'impairs')
    elif exercise == 5:
        def exercise4(ndebut, nfin):
            npair = 0
            nimpair = 0
            for i in range(ndebut, nfin):
                if i % 2 == 0:
                    print(i, 'est pair')
                    npair = npair + 1
                else:
                    print(i, 'est impair')
                    nimpair = nimpair + 1
            print('Il y a', npair, 'pairs et', nimpair, 'impairs')


        ndebut = int(input('Quel est votre debut?:'))
        nfin = int(input('Quel est votre fin?')) + 1
        exercise4(ndebut, nfin)
    elif exercise == 6:
        d6 = random.randint(1, 6)
        print('Le résultat de votre lancer =', d6, )
    elif exercise == 7:
        score = 0
        nlancer = int(input('Combien de des vous-voulez lancer ?'))
        nlancerv = nlancer
        while nlancer > 0:
            d6 = random.randint(1, 6)
            nlancer = nlancer - 1
            score = score + d6
        print('Vous avez lancer',nlancerv,'de de(s) pour avoir',score,)
    elif exercise == 8:
        d6 = 0
        nlancer = 0
        score = int(input('Quel est votre score voulu?'))
        if score > 0 and score >7:
            while score != d6:
                d6 = random.randint(1, 6)
                nlancer = nlancer + 1
            print('Vous avez lancé', nlancer, 'dé(s) à six faces et obtenu le score de', score, )
        else:
            print('Le score doit etre de 1 a 6')













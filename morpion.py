from random import randint

a =' '
b =' '
c =' '
d =' '
e =' '
f =' '
g =' '
h =' '
i =' '



#J1 = X
#5 fois J1 et 4fois J2

print("Choisir ou mettre la croix :") 
print("Mettre un nombre entre 1 et 9. 1 correspond à la case en Haut à gauche")
print("9 correspond à la case en bas à droite.")

while:
    J1_1 = int(input())

    if J1_1 == 1:
        a = 'X'
    if J1_1 == 2:
        b = 'X'
    if J1_1 == 3:
        c = 'X'
    if J1_1 == 4:
        d = 'X'
    if J1_1 == 5:
        e = 'X'
    if J1_1 == 6:
        f = 'X'
    if J1_1 == 7:
        g = 'X'
    if J1_1 == 8:
        h = 'X'
    if J1_1 == 9:
        i = 'X'

    tab1 = [ a , b , c ]
    tab2 = [ d , e , f ]
    tab3 = [ g , h , i ]

    print(tab1)
    print(tab2)
    print(tab3)

    J2_1 = int(input())

    if J2_1 != J1_1 :
        if J2_1 == 1:
            a = 'O'
        if J2_1 == 2:
            b = 'O'
        if J2_1 == 3:
            c = 'O'
        if J2_1 == 4:
            d = 'O'
        if J2_1 == 5:
            e = 'O'
        if J2_1 == 6:
            f = 'O'
        if J2_1 == 7:
            g = 'O'
        if J2_1 == 8:
            h = 'O'
        if J2_1 == 9:
            i = 'O'
    else:
        print("C'est déjà choisi !")
        while J2_1 == J1_1 :
            J2_1 = int(input())
        if J2_1 != J1_1 :
            if J2_1 == 1:
                a = 'O'
            if J2_1 == 2:
                b = 'O'
            if J2_1 == 3:
                c = 'O'
            if J2_1 == 4:
                d = 'O'
            if J2_1 == 5:
                e = 'O'
            if J2_1 == 6:
                f = 'O'
            if J2_1 == 7:
                g = 'O'
            if J2_1 == 8:
                h = 'O'
            if J2_1 == 9:
                i = 'O'

    tab1 = [ a , b , c ]
    tab2 = [ d , e , f ]
    tab3 = [ g , h , i ]

    print(tab1)
    print(tab2)
    print(tab3)
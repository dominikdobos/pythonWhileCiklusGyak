def feladat1():
    letszam = int(input("Létszám: "))
    i = 0
    sikeres = 0
    serult = 0
    osszido = 0
    while i < letszam:
        ido = int(input("Szint idő másodpercben: "))
        if ido < 0:
            print("Hibás!")
            i -= 1
        else:
            if ido != 0:
                sikeres += 1
                osszido += ido
            else:
                serult += 1
        i += 1
    atlag = osszido / sikeres
    print("Sérülés nélkül beértek száma:", sikeres)
    print("Az adott szintet teljesítette a szereplők", "{:.2f}".format(sikeres/letszam), "% -a" )
    print("Átlag sikeres teljesítmény:", atlag)


def feladat2():
    letszam = int(input("Létszám: "))
    i = 0
    sikeres = 0
    serult = 0
    osszido = 0
    elozo = 0
    monoton = True
    while i < letszam:
        ido = int(input("Szint idő másodpercben: "))
        if ido > elozo:
            print("Ez az érték nagyobb, mint az előző")
        else:
            print("Ez az érték kisebb, mint az előző")
            monoton = False
        elozo = ido
        if ido < 0:
            print("Hibás!")
            i -= 1
        else:
            if ido != 0:
                sikeres += 1
                osszido += ido
            else:
                serult += 1
        i += 1
    if osszido == 0 and sikeres == 0:
        atlag = 0
    else:
        atlag = osszido / sikeres
    print("Sérülés nélkül beértek száma:", sikeres)
    print("Az adott szintet teljesítette a szereplők", "{:.2f}".format(sikeres / letszam), "% -a")
    print("Átlag sikeres teljesítmény:", "{:.2f}".format(atlag))
    if monoton:
        print("Szigorúan monoton!")
    else:
        print("Nem szigorúan monoton!")
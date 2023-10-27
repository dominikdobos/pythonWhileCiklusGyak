def feladat1():
    i = 1
    while i < 150:
        if i % 2 == 0:
            print(i, end=";")
        i += 1
    print(150)


def feladat2():
    i = 0
    db = 0
    while i < 10:
        szam = int(input("Kérek egy számot: "))
        if szam % 3 == 0:
            db += 1
        i += 1
    print("3-mal osztható számok száma:", db)


def feladat3():
    i = int(input("Kérek egy számot: "))
    while i % 10 != 0:
        i = int(input("Kérek egy számot: "))


def feladat4():  # Addig kérjünk be számokat, amíg nem kapunk kétjegyű és páros számot!*
    i = int(input("Kérek egy számot: "))
    while not((i > 9 and i < 100 or i < -9 and i > -100) and i % 2 == 0):
        i = int(input("Kérek egy számot: "))


def feladat5():  # Addig kérjünk be számokat, amíg pozitív páratlan számot nem kapunk.*
    i = int(input("Kérek egy számot: "))
    while i <= 0 or i % 2 == 0:
        i = int(input("Kérek egy számot: "))


def feladat6():  # Addig kérjünk be számokat, amíg 3-mal osztható vagy négyzetszám nem lesz.*
    i = int(input("Kérek egy számot: ")).__abs__()
    while not((i % 3 == 0) or (i ** 0.5) % 1 == 0):
        i = int(input("Kérek egy számot: ")).__abs__()
    print("Siker")


def feladat7():  # Kérj be valós 3 számot, amíg szerkeszthető háromszög oldalait nem kapjuk!
    a = float(input("Kérek egy valós számot: "))
    b = float(input("Kérek egy valós számot: "))
    c = float(input("Kérek egy valós számot: "))
    while not((a > b + c) or (b > a + c) or (c > a + b)):
        print("Nem szerkeszthető!")
        a = float(input("Kérek egy valós számot: "))
        b = float(input("Kérek egy valós számot: "))
        c = float(input("Kérek egy valós számot: "))
    print("Szerkeszthető")


def feladat8():  # Addig kérjünk be szöveget, amíg legalább 3 karakterest nem írnak be. Majd írjuk ki a szót csupa nagy betűvel!*
    i = input("Kérek egy szöveget: ")
    if not(len(i) >= 3):
        i = input("Kérek egy szöveget: ")
    print(i.upper())


def feladat9():  # Addig kérjünk be szöveget, amíg csupa kis betűs és 4 karakteres szót nem adnak meg!*
    i = input("Kérek egy szöveget: ")
    while not(i.islower() and len(i) == 4):
        i = input("Kérek egy szöveget: ")


def feladat10():  # Kérj a felhasználótól bizonyos számú egész számot (0-tól eltérő értékeket), és írasd ki az átlagukat 2 tizedes jegy pontossággal (a felhasználó úgy jelzi, hogy többet nem kíván beírni, hogy azt írja: 0)!
    i = int(input("Kérek egy számot (Ha 0 akkor nem kell több): "))
    db = 0
    osszeg = i
    atlag = 0
    while not(i == 0):
        i = int(input("Kérek egy számot (Ha 0 akkor nem kell több): "))
        db += 1
        osszeg += i
    atlag = osszeg / db
    print("A számok átlaga:", "{:.2f}".format(atlag))


def feladat11():  # A fenti feladatot írd meg úgy, hogy csak pozitív számot fogadjon el (ha negatív, addig kérjen új számot, ameddig pozitív nem lesz), illetve ha 0-t ír, akkor legyen vége a bemeneteknek!
    i = int(input("Kérek egy számot (Ha 0 akkor nem kell több): "))
    db = 0
    osszeg = 0
    atlag = 0
    while not(i == 0):
        while not(i > 0):
            i = int(input("Kérek egy POZITÍV számot (Ha 0 akkor nem kell több): "))
        db += 1
        osszeg += i
        i = int(input("Kérek egy számot (Ha 0 akkor nem kell több): "))
    atlag = osszeg / db
    print("NYERTÉL VALAMIT!!", "{:.2f}".format(atlag))


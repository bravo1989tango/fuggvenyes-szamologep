# FUNKCIÓK

plusz = "+"
minusz = "-"
osztas = "/"
szorzas = "*"

                # A tervben bármilyen változókat lehet használni nem kell ugyanaz
                #nem kell paramétert megadni a függvény utáni zárójelbe ha függvényen belül adjuk meg

def osszeadasmuv(num1, num2):
    osszeg = num1 + num2
    print("Az összeadás eredménye: ")
    return osszeg

def kivonasmuv(num1,num2):
    osszeg = num1 - num2
    print("A kivonás eredménye: ")
    return osszeg

def szorzasmuv(num1,num2):
    osszeg = num1 * num2
    print("A szorzás eredménye: ")
    return osszeg

def osztasmuv(num1,num2):
    osszeg = num1/num2
    print("Az osztás eredménye: ")
    return osszeg

def teszt1():
    while True:
        try:
            num1 = int(input("Kérem az első számot: "))
            return num1
        except ValueError:
            print("Számokat kérek!")

def teszt2():
    while True:
        try:
            num2 = int(input("Kérem a második számot: "))
            return num2
        except ValueError:
            print("Számokat kérek!")
while True:
    szam1 = teszt1()
    szam2 = teszt2()
    muvelet = input("Kérem a műveletet: ")
    if muvelet == plusz:
        print(osszeadasmuv(szam1,szam2))
        break
    elif muvelet == minusz:
        print(kivonasmuv(szam1,szam2))
        break
    elif muvelet == osztas:
        print(osztasmuv(szam1,szam2))
        break
    elif muvelet == szorzas:
        print(szorzasmuv(szam1,szam2))
        break
    else:
        print("Érvénytelen operátor!")
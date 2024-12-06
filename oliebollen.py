import math
import time
import os

def winkel():
    # start tekst
    print("-------- ACTIE --------")
    print("ELKE 10 OLIEBOLLEN KOSTEN €10.00 INPLAATS VAN €11.50\n")
    print("BOVEN €50.00 7.5% KORTING\n")

    while True:
        try:
            oliebollen = int(input("Hoeveel oliebollen (van €1,15) wilt u bestellen? "))
            if oliebollen < 0:
                print("Aantal mag niet negatief")
            else:
                break
        except ValueError:
            print("Voer een geldig nummer in")

    while True:
        try:
            appelflappen = int(input("Hoeveel appelflappen (van €1,60) wilt u bestellen? "))
            if appelflappen < 0:
                print("Aantal mag niet negatief zijn")
            else:
                break
        except ValueError:
            print("Voer een geldig nummer in")

    # prijzen
    oliebollenPrijs = 1.15
    appelflappenPrijs = 1.60
    zakprijs = 10.00

    # percentages
    kortingPrecentage = 7.5
    btwPrecentage = 9

    aantalZakken = oliebollen // 10
    loseoliebollen = oliebollen % 10

    # totaal berekeningen
    totaalOliebollen = (aantalZakken * zakprijs) + (loseoliebollen * oliebollenPrijs)
    totaalAppelflappen = appelflappen * appelflappenPrijs

    subtotaal = totaalOliebollen + totaalAppelflappen

    korting = 0
    if subtotaal > 50:
        korting = round(subtotaal * (kortingPrecentage / 100), 2)

    totaal = subtotaal - korting

    # btw berekenen
    prijsZonderBTW = totaal / 1.09
    btw = totaal - prijsZonderBTW

    # wachtijd berekenen
    tijdPerGroep = 75
    tijdPerZak = 15
    tijdOlieballen = ((oliebollen + 14) // 15) * (tijdPerGroep + tijdPerZak)

    tijdPerInpakAppel = 20
    tijdAppelflappen = ((appelflappen + 2) // 3) * tijdPerInpakAppel

    totaleTijd = tijdOlieballen + tijdAppelflappen

    wachtTijdMinuten = math.ceil(totaleTijd / 60)

    # bon print
    print("\n---------- [UW BESTELLING] ----------")
    if aantalZakken > 0:
        print(f"Oliebol (zak): {aantalZakken:>2} x €{zakprijs:<5.2f} = €{aantalZakken * zakprijs:>7.2f}")
    if loseoliebollen > 0:
        print(f"Oliebol (los): {loseoliebollen:>2} x €{oliebollenPrijs:<5.2f} = €{loseoliebollen * oliebollenPrijs:>7.2f}")
    if appelflappen > 0:
        print(f"Appelflap:     {appelflappen:>2} x €{appelflappenPrijs:<5.2f} = €{totaalAppelflappen:>7.2f}")
    if korting > 0:
        print("------------------------------------+")
        print(f"Subtotaal:                   €{subtotaal:7.2f}")
        print(f"Korting (7.5%):             -€{korting:7.2f}")
    print("------------------------------------+")
    print(f"Totaal:                      €{totaal:7.2f}")
    print(f"BTW ({btwPrecentage}%):                    €{btw:7.2f}")
    print(f"Wachtijd: {wachtTijdMinuten} minuuten")

    time.sleep(5)

    herhalen = input("Nog een bestelling invoeren? (j) of (n)\n")
    if herhalen.lower() == 'j':
        os.system('clear' if os.name == 'posix' else 'cls')
        winkel()

if __name__ == "__main__":
    winkel()
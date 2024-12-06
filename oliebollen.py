print("-------- ACTIE --------")
print("ELKE 10 OLIEBOLLEN KOSTEN €10.00 INPLAATS VAN €11.50\n")

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

oliebollenPrijs = 1.15
appelflappenPrijs = 1.60
zakprijs = 10.00

aantalZakken = oliebollen // 10
loseoliebollen = oliebollen - (aantalZakken * 10)

totaalOliebollen = (aantalZakken * 10 * 1) + (loseoliebollen * oliebollenPrijs)
totaalAppelflappen = appelflappen * appelflappenPrijs

totaal = totaalOliebollen + totaalAppelflappen

print("-------- [UW BESTELLING] --------")
if oliebollen > 0:
    print(f"Oliebol (zak): {aantalZakken:>2} x €{zakprijs:<5.2f} = €{aantalZakken * 10 * 1:>7.2f}")
    if loseoliebollen > 0:
        print(f"Oliebol (los): {loseoliebollen:>2} x €{oliebollenPrijs:<5.2f} = €{loseoliebollen * oliebollenPrijs:>7.2f}")
if appelflappen > 0:
    print(f"Appelflap:     {appelflappen:>2} x €{appelflappenPrijs:<5.2f} = €{totaalAppelflappen:>7.2f}")
print("---------------------------------+")
print(f"Totaal:                     {totaal:5.2f}")
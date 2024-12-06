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

totaalOliebollen = oliebollen * oliebollenPrijs
totaalAppelflappen = appelflappen * appelflappenPrijs

totaal = totaalOliebollen + totaalAppelflappen

print("------ [UW BESTELLING] ------")
if oliebollen > 0:
    print(f"Oliebol: {oliebollen:>2} x €{oliebollenPrijs:<4.2f} = €{totaalOliebollen:>5.2f}")
if appelflappen > 0:
    print(f"Appelflap:{appelflappen:>2} x €{appelflappenPrijs:<4.2f} = €{totaalAppelflappen:>5.2f}")
print("-----------------------------+")
print(f"Totaal:                 {totaal:5.2f}")
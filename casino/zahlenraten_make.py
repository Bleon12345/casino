import random

while True:
    while True:
        try:
            bet_money = float(input("wie viel geld willst du setzen? ->"))
            break
        except:
            print("Bitte wähle eine Zahl")

    print("""    1. Aus 10 Zahlen  (Multiplikator: 2)
    2. Aus 25 Zahlen (Multiplikator: 3)
    3. Aus 50 Zahlen (Multiplikator: 4)
    4. Aus 100 Zahlen (Multiplikator: 5)
    """)

    while True:
        meine_range = input("Wähle aus 1,2,3,4 ->")
        if meine_range in str([1,2,3,4]):
            break
        else:
            print("bitte wähe eine der angegebenen zahlen")


    if meine_range == "1":
        die_range = 10
    elif meine_range == "2":
        die_range = 25
    elif meine_range == "3":
        die_range = 50
    elif meine_range == "4":
        die_range = 100


    random_zahl = random.randint(0, die_range)
    meine_geratene_zahl = input(f"Errate die Zahl von 0 bis {die_range} ->")
    if meine_geratene_zahl == random_zahl:
        print("Du hast richtig geraten!")
        print("Hier ist dein gewonnenes Geld: " + bet_money*(meine_range+1))
    else:
        print("Danke für dein Geld. Verkauf dein Haus Frau und Kinder oder geh raus!")
        entscheidung = input("Willst du dein Haus Frau und Kinder verkaufen um weiter zu spielen? j/n ->")
        if entscheidung == "j" or "J":
            print("Hier ist dein Geld für das Haus Frau und Kinder")
        elif entscheidung == "n" or "N":
            break
print("niggas")

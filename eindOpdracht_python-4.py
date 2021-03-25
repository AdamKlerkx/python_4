import os           #hier heb ik ale variabele neergezet
woordenlijst = {}
DELETE = 'd'
KIES_LIJST = 'k'
MAX_WOORDLENGTE = 40
NIEUWE_LIJST = 'n'
OPSLAAN = 'w'
OVERHOREN = 'o'
SCHEIDER = '='
SCHERMBREEDTE = 80
SCHERMHOOGTE = 40
STANDAARD_LIJST = 'EN-NED'
STOPPEN = 'q'
TOEVOEGEN = 't'
GEKOZEBESTAND = "test_bestand.txt"
CONTROLS_VERANDEREN = 'c'
KIJKEN = "l"
DELIMiTER = ";"
fouten = 0
nieuwe_bestand = ""
naar_wat_input = ""
verander_input = ""


def clear_screen():         #clear schreen
    os.system('cls' if os.name == 'nt' else 'clear')

def compile(woord1,woord2): #hier compile ik twee worden in een formaat die in het document gaat zodat het later nog gelzen kan worden
    compile = woord1 + SCHEIDER + woord2 + DELIMiTER
    return compile

def file_explore(): #met dit stukje pragtige code (waar ik erg trots op ben) kan ik uit het documend waar je nu in zit alle .txt bestanden filteren en de .txt er af haalen zodat het voor de user te lezen is
    file = os.listdir()
    lijste = ""
    # print(file)
    # clear_screen()
    for word in file:
        if ".txt" in word:
            word = word.replace(".txt", "")
            lijste += word + ", "
            # print(word)
        else:
            pass
    print(lijste)

def overhoren(bestandsnaam): #hier me overhoor ik de woorden lijst aan de user
    with open(bestandsnaam) as f:
        bestandsdata = f.read().split(DELIMiTER)
        for item in bestandsdata:
            if not item == '':
                woord1, woord2 = item.split(SCHEIDER)
                print_header()
                print(woord1)
                if (input("wat is het vertalde woord: ")) == woord2:
                    print("goedzo")
                else:
                    print("sorry fout")

def woordenlijst_make(bestandsnaam):    #hiermee zet ik de inhoud van het bestand in een dictionary
    with open(bestandsnaam) as f:
        bestandsdata = f.read().split(DELIMiTER)
        for item in bestandsdata:
            if not item == '':
                woord1, woord2 = item.split(SCHEIDER)
                # print(woord1)
                # print(woord2)
                woordenlijst[woord1] = woord2
    return woordenlijst


def print_lijn(tekst="", uitlijn="<"):  #hier mee kan ik een mjooie regel maken
    print(("| {:" + uitlijn + str(SCHERMBREEDTE - 2) + "} |").format(tekst))

def print_menu():  #hiermee print ik het menu en return ik de input van de user
    print_header()
    print_lijn(KIES_LIJST + " - Kies een nieuwe lijst")
    print_lijn(OVERHOREN + " - Overhoor de geselekteerde lijst")
    print_lijn(TOEVOEGEN + " - Voeg een woord toe aan de huidige lijst")
    print_lijn(DELETE + " - Verweideren")
    print_lijn(KIJKEN + " - om je lijst te zien")
    print_lijn(NIEUWE_LIJST + " - Maak een woordenlijst aan")
    print_lijn(CONTROLS_VERANDEREN + " - om de controls te veranderen")
    print_lijn(STOPPEN + " - quit het programma")
    print_header()
    Input = input("hier kan je het invullen: ")
    return Input

def print_header(): #hier mee print ik de header om boven en onder het menu te zeten
    print("+" + "-" * (SCHERMBREEDTE) + "+")

def woord_toevoegen(gekozenbestand):    #hier mee voeg ik een woord toe aan het gekozen document
    toegevoegt1 = input("wat is het eerste woord: ")
    toegevoegt2 = input("wat is het tweede woord: ")
    f = open(gekozenbestand, 'a')
    # f.write(toegevoegt1 + SCHEIDER + toegevoegt2 + DELIMiTER)
    f.write(compile(toegevoegt1,toegevoegt2))
    woordenlijst = woordenlijst_make(gekozenbestand)
    return woordenlijst

def woord_weghalen(gekozenbestand): #met dit mooie stukje code haal ik een woord weg uit het gekozen bestand
    print("zo ziet het bestand er nu uit: " + str(woordenlijst_make(gekozenbestand)))
    woorden = str(woordenlijst_make(gekozenbestand))
    nieuwe_lijst = ""
    welke_key = input("welke key wil je weg halen: ")
    if welke_key in woorden:
        for key, value in woordenlijst_make(gekozenbestand).items():
            if welke_key == key:
                pass
            else:
                # nieuwe_lijst += key + SCHEIDER + value + DELIMiTER
                nieuwe_lijst += compile(key,value)
        print(nieuwe_lijst)
        f = open(gekozenbestand, "w")
        f.write(nieuwe_lijst)
        f.close()
    else:
        print("sorry dit is geen key")

def controls_veranden():    #hier mee print ik het menu overniew maar deze keer zonder de headers, ook vraag ik wat de user wild veranderen en naar wat. dat stuur ik dan weer terug
    print("hoi")
    print("welke control wil je veranden kies tussen deze: ")
    print_lijn(KIES_LIJST + " - Kies een nieuwe lijst")
    print_lijn(OVERHOREN + " - Overhoor de geselekteerde lijst")
    print_lijn(TOEVOEGEN + " - Voeg een woord toe aan de huidige lijst")
    print_lijn(DELETE + " - Verweideren")
    print_lijn(KIJKEN + " - om je lijst te zien")
    print_lijn(NIEUWE_LIJST + " - Maak een woordenlijst aan")
    print_lijn(CONTROLS_VERANDEREN + " - om de controls te veranderen")
    print_lijn(STOPPEN + " - quit het programma")
    verander_input = input("type hier de leter die je wild veranderen: ")
    naar_wat_input = input("naar wat wil je " + verander_input + " veranderen? ")
    return verander_input, naar_wat_input

def nieuwe_lijst(): #hiermee maak ik een nieuwe lijst aan
    naarwat = input("hoe wil je het bestand noemen, het moet een naam zijn van een bestand die nog niet bestaat: ")
    hoe_veel = input("hoe veel woorden wil je toevoegen? ")
    f = open(naarwat + ".txt", "w")
    for i in range(int(hoe_veel)):
        inhoud = input("wat is het word dat getest word: ")
        inhoud2 = input("wat is de vertaling daarvan: ")
        # compilen = inhoud + SCHEIDER + inhoud2 + DELIMiTER
        compilen = compile(inhoud,inhoud2)
        f.write(compilen)
    f.close()

def kies_lijst(): #hier kies ik de nieuwe lijst
    while True:
        file_explore()
        nieuwe_bestand = input("kies je bestands naam tussen deze bestanden: ")
        nieuwe_bestand = (nieuwe_bestand) + ".txt"
        if input("is " + nieuwe_bestand + " het bestand die jij hebt gekoze? ") == "ja":
            GEKOZEBESTAND = nieuwe_bestand
            print(GEKOZEBESTAND)
            break
        else:
            pass

def main(): #hier gebeurd alles
    global STOPPEN
    global CONTROLS_VERANDEREN
    global OVERHOREN
    global KIES_LIJST
    global TOEVOEGEN
    global DELETE
    global KIJKEN
    clear_screen()
    GEKOZEBESTAND = "test_bestand.txt"
    while (geprint := print_menu()) != STOPPEN: #een while loop die stopt als geprint "p" is
        if geprint == CONTROLS_VERANDEREN:  #hiermee verander ik de controls
            verander_input, naar_wat_input = controls_veranden()
            if verander_input == STOPPEN:
                STOPPEN = str(naar_wat_input)
            if verander_input == CONTROLS_VERANDEREN:
                CONTROLS_VERANDEREN = str(naar_wat_input)
            if verander_input == OVERHOREN:
                OVERHOREN = str(naar_wat_input)
            if verander_input == KIES_LIJST:
                KIES_LIJST = str(naar_wat_input)
            if verander_input == TOEVOEGEN:
                TOEVOEGEN = str(naar_wat_input)
            if verander_input == DELETE:
                DELETE = str(naar_wat_input)
            if verander_input == KIJKEN:
                KIJKEN = str(naar_wat_input)
            else:
                print("sorry deze leter staat niet in de lijst")
        elif geprint == OVERHOREN:  #hiermee overhoor ik
            overhoren(GEKOZEBESTAND)
        elif geprint == KIES_LIJST: #hiermee kies ik een lijst
            kies_lijst()
        elif geprint == TOEVOEGEN:  #hiermee voeg ik een word toe aan het bestand
            woord_toevoegen(GEKOZEBESTAND)
            print("dus you woorden lijst ziet er nu zo uit: " + str(woordenlijst))
        elif geprint == DELETE: #hiermee verwijder ik een woord uit de lijst
            woord_weghalen(GEKOZEBESTAND)
        elif geprint == KIJKEN: #hiermee kan de user kijken wat er in de lijst staat
            print("zo ziet jou geseleckteerde bestand er uit: " + str(woordenlijst_make(GEKOZEBESTAND)))
        elif geprint == NIEUWE_LIJST: #hiermee maak ik een nieuwe lijst
            nieuwe_lijst()
        else:   #als de input van de user in geen een van deze if's past dan komt hij bij dit berigt uit
            print("sorry dit is geen comand")



main()


'''
todo

    fouten regelen in overhoooren
'''



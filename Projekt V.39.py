import time


# Hej då funktion för implementering
def goodbye():
    print('Thank you for using LimeWare Spyware!')
    time.sleep(1)
    print('Please tell you friends!')
    time.sleep(1)
    print('But only if they are spies!')
    time.sleep(0.5)


users = {}

# Välkomst text
print(input('Welcome To LimeWare Spyware!\nThe worlds most ineffective encryption service!\nPress enter to continue'))
# Menu
running = True
while running:
    try:
        # Menyval för att logga in, skapa användare eller stänga programmet
        menuChoice = int(input('Log in or create new user\n[1] Log in\n[2] Create new user\n[3] Quit\n>>> '))
        if menuChoice == 1:
            attempt = True
            count = 0
            while attempt:
                if count <= 2:
                    login = input('Enter Username\n>>> ')
                    password = input('Enter Password\n>>> ')
                    count += 1

                    if (login not in users or not users[login] == password) and count <= 2:
                        attempts = str(count)
                        print('Wrong username or password\nPlease try again\nAttempt: ' + attempts, 'of 3')

                    elif (login in users and users[login] == password) and count < 2:
                            print('Login successful!')
                            createMessage = True
                            while createMessage:
                                # Ange om det ska encrypt eller decrypt
                                checkMode = True
                                while checkMode:
                                    try:
                                        enorde = int(input('What would you like to do?\n[1] Encrypt\n[2] Decrypt\n\n>>> '))
                                        if enorde == 1:
                                            mode = 1
                                        elif enorde == 2:
                                            mode = 2
                                        else:
                                            print('Invalid input. Please enter 1 or 2')
                                            continue

                                        # Texten som man vill ha encrypted eller decrypted
                                        message = str(input('What is your message?\n>>> '))

                                        # val av nyckel
                                        key = int(input('Choose encryption/decryption key(Remember Your key)\n>>> '))
                                        strkey = str(key)

                                        # Alla symboler som går att  använda sig av
                                        SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

                                        # Lagra medelandet
                                        translated = ''

                                        for symbol in message:
                                            if symbol in SYMBOLS:
                                                symbolIndex = SYMBOLS.find(symbol)

                                                # Här sker själva encrytpion eller decryption
                                                if mode == 1:
                                                    # Hur många steg den går ner i karaktärer i SYMBOLS
                                                    translatedIndex = symbolIndex + key
                                                elif mode == 2:
                                                    # Hur många steg den går bak i karaktärer i SYMBOLS
                                                    translatedIndex = symbolIndex - key

                                                if translatedIndex >= len(SYMBOLS):
                                                    translatedIndex = translatedIndex - len(SYMBOLS)
                                                elif translatedIndex < 0:
                                                    translatedIndex = translatedIndex + len(SYMBOLS)

                                                translated = translated + SYMBOLS[translatedIndex]

                                            else:
                                                # Om man använder andra tecken än de tillåtna
                                                print('Please use the allowed symbols\nabcdefghijklmnopqrstuvwxyz1234567890 !?.')

                                        print('Your message is:\n' + translated)
                                        print()
                                        print()
                                        try:
                                            # Variabel för att få antingen y eller n på checksave
                                            checkSave = True
                                            while checkSave:
                                                savemessage = str(input('Would you like to save your message to a file?[Y]/[N]\n>>> ').lower())
                                                if savemessage == 'y':
                                                    nameFile = input('Name your file\n>>> ')  # Namnge din fil
                                                    with open(nameFile + '.txt', 'w') as f:
                                                        # Skriver ner key och meddelande till fil
                                                        f.write('Key: ' + strkey + '\nMessage: ' + message)
                                                        f.close()
                                                        break
                                                elif savemessage == 'n':
                                                    break
                                                else:
                                                    print('Invalid input')
                                        except:
                                            print('Please enter Y or N')
                                            continue

                                        # börja om eller stäng ner programmet
                                        check = int(input('[1] Continue\n[2] Quit\n>>> '))
                                        if check == 1:
                                            continue
                                        elif check == 2:  # Stäng ner programmet
                                            goodbye()
                                            checkMode = False
                                            createMessage = False
                                            running = False
                                            attempt = False
                                    except:
                                        print('Invalid iput. Please enter 1 or 2')

                    elif count == 3:
                        # Stäng program om inlogg tar förmånga försök
                        print('Attempt: 3 of 3')
                        print('Too many attempts\n Program shutting down')
                        time.sleep(0.5)
                        attempt = False
                        running = False

        elif menuChoice == 2:
            createUser = input('Create username\n>>> ')  # Skapa ett användarnamn

            if createUser in users:
                print('Username already exists!')  # Ifall användarnamnet redan är angett

            else:
                createPass = input('Create password\n>>> ')
                users[createUser] = createPass  # Spara användanamnet till users och lösenordet till användarnamnet
                print('Success!\nUser created')
                continue
        # Avsluta programmet
        elif menuChoice == 3:
            goodbye()
            running = False
        else:
            print('Choice is out of range, please try again')  # Fånga upp om siffran är ej är 1-3
            continue
    except:
        print('Invalid input')  # Fånga upp om input ej är en siffra
        continue

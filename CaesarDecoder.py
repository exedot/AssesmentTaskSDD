def start():
    white = str("\u001b[37m")
    yellow = str("\u001b[33;1m")

    # The maketrans() method returns a translation table that maps each character in the first(intab) string into the character at the same position in the last(outtab) string.
    rot13 = str.maketrans('NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm', 'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz')

    print("          _____                    _____                    _____                    _____                    _____                    _____                    _____                _____    \n"      
    "         /\    \                  /\    \                  /\    \                  /\    \                  /\    \                  /\    \                  /\    \              |\    \         \n"
    "        /::\    \                /::\    \                /::\    \                /::\    \                /::\    \                /::\    \                /::\    \             |:\____\        \n"
    "       /::::\    \              /::::\    \              /::::\    \              /::::\    \              /::::\    \              /::::\    \              /::::\    \            |::|   |        \n"
    "      /::::::\    \            /::::::\    \            /::::::\    \            /::::::\    \            /::::::\    \            /::::::\    \            /::::::\    \           |::|   |        \n"
    "     /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \          |::|   |        \n"
    "    /:::/  \:::\    \        /:::/__\:::\    \        /:::/__\:::\    \        /:::/__\:::\    \        /:::/__\:::\    \        /:::/__\:::\    \        /:::/__\:::\    \         |::|   |        \n"
    "   /:::/    \:::\    \      /::::\   \:::\    \      /::::\   \:::\    \       \:::\   \:::\    \      /::::\   \:::\    \      /::::\   \:::\    \      /::::\   \:::\    \        |::|   |        \n"
    "  /:::/    / \:::\    \    /::::::\   \:::\    \    /::::::\   \:::\    \    ___\:::\   \:::\    \    /::::::\   \:::\    \    /::::::\   \:::\    \    /::::::\   \:::\    \       |::|___|______  \n"
    " /:::/    /   \:::\    \  /:::/\:::\   \:::\    \  /:::/\:::\   \:::\    \  /\   \:::\   \:::\    \  /:::/\:::\   \:::\    \  /:::/\:::\   \:::\____\  /:::/\:::\   \:::\____\      /::::::::\    \ \n"
    "/:::/____/     \:::\____\/:::/  \:::\   \:::\____\/:::/__\:::\   \:::\____\/::\   \:::\   \:::\____\/:::/  \:::\   \:::\____\/:::/  \:::\   \:::|    |/:::/  \:::\   \:::|    |    /::::::::::\____\ \n"
    "\:::\    \      \::/    /\::/    \:::\  /:::/    /\:::\   \:::\   \::/    /\:::\   \:::\   \::/    /\::/    \:::\  /:::/    /\::/   |::::\  /:::|____|\::/    \:::\  /:::|____|   /:::/~~~~/~~      \n"
    " \:::\    \      \/____/  \/____/ \:::\/:::/    /  \:::\   \:::\   \/____/  \:::\   \:::\   \/____/  \/____/ \:::\/:::/    /  \/____|:::::\/:::/    /  \/_____/\:::\/:::/    /   /:::/    /         \n"
    "  \:::\    \                       \::::::/    /    \:::\   \:::\    \       \:::\   \:::\    \               \::::::/    /         |:::::::::/    /            \::::::/    /   /:::/    /          \n"
    "   \:::\    \                       \::::/    /      \:::\   \:::\____\       \:::\   \:::\____\               \::::/    /          |::|\::::/    /              \::::/    /   /:::/    /           \n"
    "    \:::\    \                      /:::/    /        \:::\   \::/    /        \:::\  /:::/    /               /:::/    /           |::| \::/____/                \::/____/    \::/    /            \n"
    "     \:::\    \                    /:::/    /          \:::\   \/____/          \:::\/:::/    /               /:::/    /            |::|  ~|                       ~~           \/____/             \n"
    "      \:::\    \                  /:::/    /            \:::\    \               \::::::/    /               /:::/    /             |::|   |                                                        \n"
    "       \:::\____\                /:::/    /              \:::\____\               \::::/    /               /:::/    /              \::|   |                                                        \n"
    "        \::/    /                \::/    /                \::/    /                \::/    /                \::/    /                \:|   |                                                        \n"
    "         \/____/                  \/____/                  \/____/                  \/____/                  \/____/                  \|___|                                                        \n"
    "                                                                                                                                                                                                    ")
    # User's input is provided before decoding begins
    print("Welcome to the decryption program, provided for your convenience")
    inp = input("Encrypted text goes here:\n")
    # Input is then translated using our pre-established rot13 variable
    print(yellow + inp.translate(rot13) + white)
    print("The above text has been decoded. Thank you for using Stop 'N' Drop, America's favourite suicide booth since 2008.")

    save = int(input("Do you wish to store as a .txt file? (Press 1 for yes):\n"))
    if save == 1:
        with open('CAESAR_decoded.txt', 'w') as f:
            f.write(inp.translate(rot13))
            print("File stored in program directory.\n")
    else:
        print("As you wish.\n")
    
    yn = int(input(white + "Revert program? 1 = Yes, 2 = No: "))
    if yn == 1 : start()
    elif yn == 2 : print(yellow + "Shutting down..." + white), exit()
    else : print("Invalid selection, " + yellow + "shutting down..." + white), exit()
start()
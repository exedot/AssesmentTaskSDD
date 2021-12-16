def start():
    white = str("\u001b[37m")
    yellow = str("\u001b[33;1m")
    red = str("\u001b[31;1m")
    # The maketrans() method returns a translation table that maps each character in the first(intab) string into the character at the same position in the last(outtab) string.
    rot13 = str.maketrans('ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz','NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm')
    print(red + "          _____                    _____                    _____                    _____                    _____                    _____                    _____                _____    \n"      
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
    "                                                                                                                                                                                                    " + white)
    # User's input is provided before encoding begins
    print("Hail unto Caesar. Lowly Plebeian, What is to be encodified?")
    inp = input("Typus in sententia ut encoded:\n")
    # Input is then translated using our pre-established rot13 variable
    print(yellow + inp.translate(rot13) + white)
    print("The above text has been encoded. Above can be decoded through the provided program")

    save = str(input("Do you wish to store as a .txt file? (y/n):\n"))
    if save == "y":
        with open('CAESAR.txt', 'w') as f:
            f.write(inp.translate(rot13))
            print("File stored in root program directory.\n")
    else:
        print("As you wish.\n")
    # Attempts reversion
    yn = int(input(white + "Revert program? 1 Yes, 2 No: "))
    if yn == 1 : start() # If user selects option 1 the program reverts to start function
    elif yn == 2 : print(yellow + "Shutting down..." + white), exit() # If option 2 was selected, the program terminates
    else : print("Invalid selection, " + yellow + "shutting down..." + white), exit() # If otherwise program is terminated
start()
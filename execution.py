from script import *

# welcome message
print("\nHello, this is a Instagram Bot by petit/petitoff. He can post comments, give likes or send DMs.\n")

# first questions
print("Choice option")
print("Comments and likes: 1")
print("DM: 2")
print("Quit: 99")

print("If you need help, please enter: help")


# running script.py
def start_script():

    login = input("\nLogin: ")
    password = input("Password: ")

    print("\nThe browser will open, however, after loading in the console, "
          "messages will still appear, so come back here.")
    sleep(2)

    ScriptSelenium().main_script(login, password, user_input)


try:
    while True:
        user_input = verify_input_int("set")

        if user_input == 1:
            # pierwsza opcja
            # dodanie like oraz komentarzy
            start_script()
            break

        elif user_input == 2:
            # druga opcja
            start_script()
            break

        elif user_input.lower() == "help":
            print("If you want to add comments and/or like, type 1.")
        elif user_input == 99:
            break
        else:
            print("Error")
except KeyboardInterrupt:
    print("Exiting...")
except AttributeError:
    print("Exiting...")
except selenium.common.exceptions.NoSuchWindowException:
    print("Exiting...")

# ScriptSelenium().script()

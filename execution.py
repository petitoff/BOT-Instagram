from script import *

print("Hello, this is a Instagram Bot by xDragon. He can post comments, give likes or send DMs.\n")

print("Comments and likes: 1")
print("DM: 2")

print("\nIf you need help, please enter: help\n")

while True:
    user_input = input(": ")
    if user_input == "1":
        while True:
            while True:
                try:
                    how_many = int(input("how many: "))
                    break
                except ValueError:
                    print("Enter a number greater than 0")
                    pass

            if how_many > 0:
                while True:
                    commant_message = input("Message in the comments: ")
                    break
                    if commant_message == "":
                        print("It cannot be empty")
                        pass
                    else:
                        break
                break
            else:
                print("Enter a number greater than 0")
                pass

        login = input("Login: ")
        password = input("Password: ")

        ScriptSelenium().main_script(login, password, how_many, commant_message)
        break
    elif user_input == "2":
        print(2)
        break
    elif user_input == "help":
        print("help")
        break
    else:
        print("Error")
        pass

# ScriptSelenium().script()

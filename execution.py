from script import *

print("Hello, this is a Instagram Bot by xDragon. He can post comments, give likes or send DMs.\n")

print("Comments and likes: 1")
print("DM: 2")

print("\nIf you need help, please enter: help\n")

while True:
    user_input = input("-:")
    if user_input == 1:
        print(1)
        break
    elif user_input == 2:
        print(2)
        break
    elif user_input == "help":
        print("help")
        break
    else:
        print("Error")
        pass

# ScriptSelenium().script()

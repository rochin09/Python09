known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Georgie", "Harry"]

while True:
    print("Hi! My name is Travis")
    name = input("What's your name?:").strip().capitalize()

    if name in known_users:
        print("Hello {}!".format(name))
        remove = input("Would you like to be removed from the system (yes/no)?:").lower()
        
        if remove == "yes":
                print("You have been removed from the system")
                known_users.remove(name)
        elif remove == "no":
                print("No problem, I didn't want you to leave anyway!")
            
    else:
        print("Hmmm I don't think I have met you yet {}".format(name))
        add_me = input("Would you like to be added to the system (yes/no)?:").strip().lower()
        if add_me == "yes":
            print("I will update the previous list and then add you to the system")
            print(known_users)
            known_users.append(name)
            print(known_users)
            print("As you can see, you have been added to the system, now I recognize you")
        elif add_me == "no":
               print("No worries, see you around")
        

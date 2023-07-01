import time
"""Will need to adjust/modify numbers/code for the json dict and such. I just did them
   this way to give a basic idea of what I was thinking, feel free to 
   adjust/change anything. I am also open to any advice or thoughts. """

#Sample dictionary to fool with, might have to modify for actual json dict
sampleroid = {"AsteroidA": {"Speed": 30000, "Distance": 484851, "Size": 6},
              "AsteroidB": {"Speed": 8452654, "Distance": 481518496161518, "Size": 1}}

#function to print all asteroids in dict
def print_info():
    for asteroid_name in sampleroid:
        print(asteroid_name)

#function that gets info of a choosen astoerid and runs checks on its data
def get_info():
    print_info()
    secure_info = False
    while not secure_info:
        info_choice = input("Which asteroid do you need info on?\n")
        if not info_choice.isdigit():
            secure_info = True

            if info_choice in sampleroid:
                speed = sampleroid[info_choice]["Speed"]
                distance = sampleroid[info_choice]["Distance"]
                size = sampleroid[info_choice]["Size"]
                print("***" + info_choice + "***")
                print("Speed:", speed, "MPH")
                print("Distance:", distance, "Miles")
                print("Size:", size, "Miles long\n")

                #Calculates how long it would take for asteroid to collide with earth
                collision = distance / speed
                print(info_choice + " will be here in ", round(collision, 2), " days\n")
                if collision > 75:
                    print("This little guy will be fine, will continue to monitor in case collision zone is unsafe.\n")
                elif 50 <= collision <= 75 and 3 < size < 5:
                    print("Will continue monitoring, trajectory could change. If still set on eartch: Initiate defense protocol.\n")
                elif collision < 20 and size > 4:
                    print("***DEFENSE PROTOCOL ENGAGED***")

                    secure_decision = False
                    while not secure_decision:
                        try:
                            decision = int(input("[1] Fire Missle\n"
                                                 "[2] Launch catastrophic nuke\n"))
                            if isinstance(decision, int):
                                secure_decision = True
                                if decision == 1:
                                    print("The asteroid " + info_choice + " has been broken into smaller pieces and seems to have safer to no more impact dangers.\n")
                                    sampleroid.pop(info_choice)
                                    # Countdown timer
                                    countdown_time = 5  # Adjust the countdown time as desired
                                    print("Countdown initiated...")
                                    while countdown_time > 0:
                                        print("Countdown:", countdown_time)
                                        time.sleep(1)
                                        countdown_time -= 1
                                    print("***COLLISION MADE, DANGER EVERTED***\n")
                                if decision == 2:
                                    print("The asteroid " + info_choice + " has been DECIAMTED and threat no longer persists.\n")
                                    sampleroid.pop(info_choice)
                                    # Countdown timer
                                    countdown_time = 5  # Adjust the countdown time as desired
                                    print("Countdown initiated...")
                                    while countdown_time > 0:
                                        print("Countdown:", countdown_time)
                                        time.sleep(1)
                                        countdown_time -= 1
                                    print("***COLLISION MADE, DANGER EVERTED***\n")
                        except ValueError:
                            print("Invalid input. Try again...\n")
        elif info_choice.isdigit():
            print("Invalid input. Try again...\n")

#Function to destroy a choosen asteroid that could be suspicious
def destroy():
    target_destroyed = False
    print("***Asteroid eradication INITIATED***")

    while not target_destroyed:
        print_info()
        target = input("Choose target: ")

        if target.isdigit():
            print("Invalid target! Please enter a valid asteroid name.\n")
            continue

        if target in sampleroid:
            print("Missiles heading towards:", target)
            print("Impact Countdown initiated...")

            countdown_time = 5  # Adjust the countdown time as desired

            while countdown_time > 0:
                print("Countdown:", countdown_time)
                time.sleep(1)
                countdown_time -= 1

            print(target, "destroyed!")
            sampleroid.pop(target)
            print("New list of asteroids:")
            print_info()

            target_destroyed = True
        else:
            print("Invalid target! The specified asteroid does not exist.\n")


#Simple menu to choose different interactions with dict
def menu():
    print("Hey there what would you like to do.\n"
          "[1] All current known Asteroid.\n"
          "[2] Obtain info about the asteroid.\n"
          "[3] Launch missle at known asteroids to clear spacefield.\n")

selection = 0
while selection != 3:
    menu()
    selection = int(input("Please make a selection.\n"))
    if selection == 1:
        print_info()
    elif selection == 2:
        get_info()
    elif selection == 3:
        destroy()
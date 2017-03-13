from sys import exit

def living_room():
    print "There is somebody passed out on the couch.  What do you do?"
    print "1. Poke him"
    print "2. Scream at him"
    print "3. Touch his bum"
    choice = raw_input("> ")

    if choice == "1":
        print "He woke up and slaps the shit out of you.  Go back to bed and start over"

    elif choice == "2":
        print "He doesn't hear you."

    elif choice == "3":
        print "He likes that.  You and he make love and run away to Antartica together."

    else:
        dead("I don't think you understand how this game works.")

def kitchen():
    print "You enter the kitchen.  What do you do first?"
    print "1. COFFEE"
    print "2. Make breakfast"
    print "3. Go back to bed"

    choice = raw_input("> ")

    if choice == "1":
        print "Good choice.  You win"

    elif choice == "2":
        print "You choke on scrambled eggs and die.  Not ideal."

    elif choice == "3":
        print "Not a bad choice.  You live to fight another day."

    else:
        dead("I don't think you understand the game.")

def start():
    print "You wake up.  Should you go to the kitchen or the living room first?"
    choice = raw_input("> ")

    if choice == "kitchen":
        kitchen()

    elif choice == "living room":
        living_room()

    else:
        dead("I don't think you understand.")

def dead(reason):
    print reason, "Game over."
    exit(0)

start()

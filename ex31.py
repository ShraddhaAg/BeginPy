print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == '1':
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at th bear."

    bear = raw_input("> ")

    if bear == '1':
        print "The bear eats your face off. Good job!"
    elif bear == '2':
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

elif door == '2':
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries.\n2. yellow jacket clothespins.\n3. Understanding revolvers ylling melodies."

    insanity = raw_input("> ")

    if insanity == '1' or insanity == "2":
        print "Your body survives powered by a mind of jello. good job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"

else:
    print "You stumble around and discover a key to the dungeon. Do you want to enter the dungeon?"

    dungeon = raw_input('> ')

    if dungeon == 'yes' or dungeon == 'YES' or dungeon == 'Yes':
        print "You face a dragon. What do you do?\n1. Try to befriend the dragon.\n2.Fight the dragon!"
        dragon = raw_input('> ')

        if dragon == '1' or dragon == '2':
            print "The dragon roats you into a marshmello. Good job!"
        else:
            print "That's probably better! The dragon lets you go in. Congratualtions you discovered a treasure!"
    else:
        print "You are a lazy ass. A vulture comes and eats your eyes out. Good job!"


def get_guests():
    guests = []
    while True:
        name = raw_input("Who's coming: ")
        if name == "":
            break
        guests.append(name)
    return guests

def say(what, guests):
    for x in guests:
        # print "Hi, {0}".format(x)
        print what + ", " + x

def inflate_balloons():
    print "The balloons are inflated"

def start_music():
    print "I want it that way is playing"

def cheer(number_of_times):
    for j in range(number_of_times):
        print 'woop de doo!'


def party():
    guests = get_guests()
    say("hello",guests)
    inflate_balloons()
    start_music()
    cheer(8)
    say("goodbye"guests)

party()

import controller

# -----------------------------------------------------
# NEW CONTROLLER
# -----------------------------------------------------

def newController():
    control = controller.newController()
    return control

# -----------------------------------------------------
# LOAD DATA
# -----------------------------------------------------

def loadData():
    players = controller.loadData(control)
    return players

def menu():
    print('1- Load Data')
    print('2- Search ovnis sightings by date')
    print('3- Show sightings by city')
    print('4- Search sightings with more duration than a number')
    print('5- Search ovnis sightings in date interval')
    print('6- Search ovnis sightings in a distance radio')
    print('7- Search ovnis sightings with a state')
    print('8- Search the shortest and largest, ovnis sightings in a country')
    print('9- Show ovnis sightingd by way')
    print('10- Search ovnis sightings with more duration in a country')
    print('11- Search ovnis sightsings by comments')

while True:
    menu()
    inputs = int(input('Select an option to continue\n'))
    if inputs == 1:
        control = newController()
        print("Loading information from files ....\n")
        players = loadData()
        print("Data was charged succesfully")

    elif inputs == 2:
        date = input('Enter date: ')
        ovnis_date = controller.requirement2(control, date)
        print(ovnis_date)

    elif inputs == 3:
        city = input('Enter the city: ')
        ovnis_city = controller.requirement3(control, city)
        print(ovnis_city)

    elif inputs == 4:
        duration = float(input('Enter duration: '))
        ovnis_duration = controller.requirement4(control, duration)
        print(ovnis_duration)

    elif inputs == 5:
        initial_date = input('Enter init date: ')
        final_date = input('Enter fianl date: ')
        ovnis_period_time = controller.requirement5(control, initial_date, final_date)
        print(ovnis_period_time)

    elif inputs == 7:
        state = input('Enter state: ')
        ovnis_state = controller.requirement7(control, state)
        print(ovnis_state)

    elif inputs == 8:
        country = input('Enter country: ')
        dic = controller.requirement8(control, country)
        print(dic)

    elif inputs == 9:
        input('Press enter to start')
        shapes = controller.requirement9(control)
        print(shapes)

    elif inputs == 10:
        pass

    elif inputs == 11:
        word  = input('Enter the word: ')
        ovnis_word = controller.requirement11(control, word)
        print(ovnis_word)
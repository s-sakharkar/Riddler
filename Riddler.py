from tkinter import *
from tkinter.scrolledtext import ScrolledText

# import time
# from tkinter import messagebox

root = Tk()
root.attributes('-topmost', 1)
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
# setting tkinter window size
root.geometry("%dx%d" % (width, height))
root.title("Riddler")

descLabel = Label(root, text="Room Description", font="Arial")
descLabel.place(x=100, y=100)
desc_output = ScrolledText(root, font=('Arial', 18), borderwidth=2, height=20, width=30, wrap=WORD)
desc_output.place(x=10, y=150)
cmdLabel = Label(root, text="Command Help", font="Arial")
cmdLabel.place(x=1100, y=120)
cmd_help_output = ScrolledText(root, font=('Arial', 18), borderwidth=2, height=20, width=30, wrap=WORD)
cmd_help_output.place(x=930, y=150)

answer_sewer = False
answer_lab = False
answer_cafe = False
answer_grass = False
answer_prison = False
answer_hall = False

startgame = False

roomDescDict = {
    '0o21': 'You are now in the sewer trapdoor. It is dark, wet, and hard to move around in. The metal makes '
            'a clanging noise as you slowly through. In the sewer, 3 signs display messages. '
            'Find which sign is false. \n1) The control panel is adjacent to the hallway. \n2) The prison cell is adjacent to the cafeteria. \n3) The '
            'grassy field is adjacent to the cafeteria. Input first, second, or third to select an answer',
    '113': 'You are now in the science lab. This room is well lit, with a table and an antique computer on top. On the wall is a large '
           'periodic table. 20 boxes with Post-Its line the sides of the room. A message on a chalkboard is: \"The answer lies IN THE TABLE\"'
           'To read through the 20 Post-Its, type a number from 1-20. To input your answer, simply type your word.'
           'To the east lies the cafeteria.',
    '123': 'you are now in the cafEteria. four small wooden tables are placed iN each corner of The room. empty plates '
           'and utensils lie on top of the plate, almost as if the aREa was meant for a gathEring. A trapdoor lies on the floor, which seems to lead to a sewer. To your north is the grassy field, '
           'to your south is the study room, and to your east is the hallway.',
    '124': 'You are now in the grass room. Besides having grass, this room is strange for a different reason:'
           'the room is surrounded by glass; and beyond it you can see nothing but darkness. A newspaper lies on a small table.'
           'A sign next to the table says, When taken together, the letters spell out the following pattern: BCEFGHJKMNOPQRSTUVWXZ. To your south is the cafeteria.',
    '132': "You are in the prison cell. The dark, discolored walls are constraining and mice scuttle around your "
           "feet. A table with three levers, red, yellow, and green is illuminated by a hanging tungsten bulb.",
    '133': 'You have arrived in the hallway connecting the Cafeteria and Control Panel room. It is fairly narrow;'
           'you can touch both sides of the wall by spreading your arms. A picture lines the wall every few feet'
           'or so, with a flower vase filled in front. In the hallway, a sign has a riddle written on it. \nIt says: '
           'I am both a color and a fruit. What am I?\n'
           'The door to the control panel room to the east is shut behind an iron door. To you south is the prison cell, '
           'and to your west is the cafeteria. To your west is the control panel room, but it is locked behind bars.'
           'You may only enter after completing the riddles for the other rooms.',
    '143': 'You are now in the control panel room. Hundreds of buttons cover each surface of the room, each having numbers '
           'corresponding with parts of the map. In the center of it all sits a digital display with spaces for 9 letters.'
           'What do you type? To your east is the hallway.'
           'Next to the digital display, a security log contains information from the prison. It reads:\nThe guard walked'
           'into the prison cell to check on the prisoner.\nHe then went to the hallway to look at the paintings.\nThen, he '
           'walked to the grass field for a breath of fresh air.\nHe then walked to the cafeteria to have lunch.\nHe then went to the'
           'lab to make sure the equipment was orderly, and finally went to the sewer to check the prisoners escape routes. ',
    'help': '\n\nCommands:\n"{north,west,east,south}": in {} direction \n"hint" or "verb": Displays a hintverb for the puzzle or task verb in the room.'
            '\n\"{up, down}\": used to descend/ascend in the sewer lever/cafeteria, respectively.'
            '\n\"take {item}\": take the specified item\nExample: take red key'
            '\n\"inventory\": allows player to see inventory'
            '\n\"flick {color} lever\": allows you to flick the specified lever\nExample: flick red lever'
            '\n\"move {item} in {location} to {new location}\": Allows you to move a specified item between two places\nExample: move red box cafeteria to central sewer'
            '\nRemember: Every room has a riddle.'
            '\nMake sure to keep track of answers, as you will need them in the final room!'
}

room = 132


def room021():
    global room
    room = 0o21
    desc_output.delete(1.0, END)
    desc_output.insert(END, roomDescDict.get(str(0o21)) + '\n')
    main_output.yview(END)
    response = e1.get()
    e1.delete(0, END)
    if response.lower() == "west":
        main_output.insert(END, 'The wall is in the way.\n')
    elif response.lower() == "north":
        room = 0o22
        main_output.insert(END, 'The wall is in the way.\n')
    elif response.lower() == "east":
        main_output.insert(END, ">The wall is in the way.\n")
    elif response.lower() == "south":
        main_output.insert(END, ">The wall is in the way.\n")
    elif response.lower() == "north":
        room = 0o23
        main_output.insert(END,
                           f"------------------------------------------------------------------\nYou have moved {response.lower()[-5:]}.")
        desc_output.delete(1.0, END)
        desc_output.insert(END, roomDescDict.get('0o23') + '\n')

        main_output.yview(END)
        room_output.insert('1.0', f'Room: 023')

    elif response.lower() == "east":
        main_output.insert(END, "The wall is in the way.\n")
    elif response.lower() == "west":
        main_output.insert(END, "The wall is in the way.\n")
    elif response.lower() == "south":
        room = 0o21
        main_output.insert(END,
                           f"------------------------------------------------------------------\nYou have moved {response.lower()[-5:]}.")
        desc_output.delete(1.0, END)
        desc_output.insert(END, roomDescDict.get('0o21') + '\n')

        main_output.yview(END)
        room_output.insert('1.0', f'Room: 021')

    elif response.lower() == "up":
        room = 123
        main_output.insert(END,
                           f"------------------------------------------------------------------\nYou have moved {response.lower()[-5:]}.")
        desc_output.delete(1.0, END)
        desc_output.insert(END, roomDescDict.get(str(room)) + '\n')

        main_output.yview(END)
        room_output.insert('1.0', f'Room: {room}\n')
    elif response.lower() == "west":
        main_output.insert(END, 'You walked into the wall.\n')
    elif response.lower() == "north":
        main_output.insert(END, 'You walked into the wall.\n')
    elif response.lower() == "east":
        main_output.insert(END, 'You walked into the wall.\n')
    elif response.lower() == "south":
        room = 0o22
        main_output.insert(END,
                           f"\nYou have moved {response.lower()[-5:]}.")
        desc_output.delete(1.0, END)
        desc_output.insert(END, roomDescDict.get('0o22') + '\n')

        main_output.yview(END)
        room_output.insert('1.0', f'Room: 0o23')

    elif response.lower() == "second":
        main_output.insert(END, 'Good job! You have found the answer to the next riddle!')
        main_output.yview(END)
        global answer_sewer
        answer_sewer = True
    else:
        main_output.insert(END, 'That is the wrong answer, try again. ')
    main_output.yview(END)


def room113():
    global room
    room = 113
    desc_output.delete(1.0, END)
    desc_output.insert(END, roomDescDict.get(str(room)) + '\n')
    main_output.yview(END)
    response = e1.get()
    e1.delete(0, END)
    dictPost = {
        1: "Actinium Carbon Einsteinium Sulfur",
        2: "Boron Radium Indium",
        3: "Chlorine Oxygen Carbon Potassium",
        4: "Dysprosium Nitrogen Americium Iodine Carbon",
        5: "Flerovium Oxygen Tungsten",
        6: "Fluorine Uranium Nitrogen",
        7: "Germanium Nickel Uranium Sulfur",
        8: "Hydrogen Actinium Potassium Erbium",
        9: "Indium Sulfur Phosphorus Iodine Rhenium",
        10: "Potassium Nobelium Tungsten",
        11: "Lutetium Carbon Potassium Yttrium",
        12: "Molybdenum Titanium Oxygen Nitrogen",
        13: "Phosphorus Holmium Neon",
        14: "Phosphorus Lanthanum Yttrium Erbium",
        15: "Rhenium Uranium Nickel Tellurium",
        16: "Sulfur Aluminum Vanadium Astatine Iodine Oxygen Nitrogen",
        17: "Ruthenium Nitrogen",
        18: "Sulfur Oxygen Carbon Iodine Aluminum",
        19: "Scandium Argon Yttrium",
        20: "Tungsten Argon"
    }
    try:
        a = int(response.lower())
        if 21 > a > 0:
            main_output.insert(END, '\nThis Post-It reads: ' + dictPost.get(int(response)))
    except ValueError:
        if response.lower() == "open table":
            main_output.insert(END, '\nYou can\'t open a table, what were you thinking?')
        elif response.lower() == "open periodic table":
            main_output.insert(END,
                               '\nYou remove the frame, and a pink Post-It falls out. It has the sequence: Rhenium Vanadium Erbium Selenium.')
        elif response.lower() == "west":
            main_output.insert(END, 'You walked into the wall.\n')
        elif response.lower() == "north":
            main_output.insert(END, 'You walked into the wall.\n')
        elif response.lower() == "east":
            room = 123
            main_output.insert(END,
                               f"\nYou have moved {response.lower()[-5:]}.")
            desc_output.delete(1.0, END)
            desc_output.insert(END, roomDescDict.get(str(room)) + '\n')

            main_output.yview(END)
            room_output.insert('1.0', f'Room: {room}\n')
        elif response.lower() == "south":
            main_output.insert(END, "The wall is in the way.\n")
        elif response.lower() == "reverse":
            main_output.insert(END, '\nGood job! You have found the answer to the riddle!')
            main_output.yview(END)
            global answer_lab
            answer_lab = True
        else:
            main_output.insert(END, '\nThat is not the answer, try again.')
        main_output.yview(END)


def room123():
    global room
    room = 123
    desc_output.delete(1.0, END)
    desc_output.insert(END, roomDescDict.get(str(room)) + '\n')
    main_output.yview(END)
    response = e1.get()
    e1.delete(0, END)
    if response.lower() == "west":
        room = 113
        main_output.insert(END,
                           f"------------------------------------------------------------------\nYou have moved {response.lower()[-5:]}.")
        desc_output.delete(1.0, END)
        desc_output.insert(END, roomDescDict.get(str(room)) + '\n')

        main_output.yview(END)
        room_output.insert('1.0', f'Room: {room}\n')

    if response.lower() == "north":
        room = 124
        main_output.insert(END,
                           f"------------------------------------------------------------------\nYou have moved {response.lower()[-5:]}.")
        desc_output.delete(1.0, END)
        desc_output.insert(END, roomDescDict.get(str(room)) + '\n')

        main_output.yview(END)
        room_output.insert('1.0', f'Room: {room}\n')

    if response.lower() == "east":
        room = 133
        main_output.insert(END,
                           f"------------------------------------------------------------------\nYou have moved {response.lower()[-5:]}.")
        desc_output.delete(1.0, END)
        desc_output.insert(END, roomDescDict.get(str(room)) + '\n')

        main_output.yview(END)
        room_output.insert('1.0', f'Room: {room}\n')

    if response.lower() == "south":
        main_output.insert(END, "The wall is in the way.\n")
    if response.lower() == "down":
        room = 0o22
        main_output.insert(END,
                           f"------------------------------------------------------------------\nYou have moved {response.lower()[-5:]}.")
        desc_output.delete(1.0, END)
        desc_output.insert(END, roomDescDict.get('0o21') + '\n')

        main_output.yview(END)
        room_output.insert('1.0', f'Room: 021')

    if response.lower() == 'entree':
        main_output.insert(END, '\nGood job. You gave completed the next riddle!\nWhere do you go from here?')
        global answer_cafe
        answer_cafe = True
    main_output.yview(END)


def room124():
    global room
    room = 124
    desc_output.delete(1.0, END)
    desc_output.insert(END, roomDescDict.get(str(room)) + '\n')
    main_output.yview(END)
    response = e1.get()
    e1.delete(0, END)
    if response.lower() == "west":
        main_output.insert(END, 'The wall is in the way.\n')
    if response.lower() == "north":
        main_output.insert(END, ">The wall is in the way.\n")
    if response.lower() == "east":
        main_output.insert(END, ">The wall is in the way.\n")
    if response.lower() == "south":
        room = 123
        main_output.insert(END, f"\nYou have moved {response.lower()[-5:]}.")
        desc_output.delete(1.0, END)
        desc_output.insert(END, roomDescDict.get(str(room)) + '\n')

        main_output.yview(END)
        room_output.insert('1.0', f'Room: {room}\n')
    if response.lower() == "read newspaper":
        main_output.insert(END,
                           "This newspaper issued by Daily News from the 1930s, talking about the Great Depression")
    if response.lower() == "daily":
        main_output.insert(END, "Good job! You have solved the next riddle. Where are you going next?")
        global answer_grass
        answer_grass = True
        main_output.yview(END)
    main_output.yview(END)


def room132():
    global startgame
    global room
    global desc_output
    room = 132
    if not startgame:
        b2.place_forget()
        b1.place(x=608, y=500)
        cmd_help_output.insert(END, 'Here is the command list.')
        cmd_help_output.insert(END, roomDescDict.get('help'))
        room = 132
        startgame = True
        room_output.insert('1.0', f'Room: {room}\n')
        main_output.insert(END,
                           "------------------------------------------------------------\n                            "
                           "Riddler\n------------------------------------------------------------")
        desc_output.insert(END, roomDescDict.get(str(room)))
        e1.configure(state="normal")
    elif startgame:
        global answer_prison
        desc_output.insert(END, roomDescDict.get(str(room)))
        global answer_lab
        response = e1.get()
        if response.lower() == "north" and not answer_prison:
            main_output.insert(END, ">The wall is in the way.\n\n")
        elif response.lower() == "flick red lever":
            main_output.insert(END,
                               ">You activate a an explosion.\nKABOOM!\n You have respawned in the prison cell, and you keep your progress.\n\n")
        elif response.lower() == "flick yellow lever":
            main_output.insert(END, ">The light illuminating the levers turns off. What were you expecting?!\n\n")
        elif response.lower() == "flick green lever":
            main_output.insert(END,
                               ">A hole opens up in the ceiling and a message falls through. It says:\n\nI’m tall when I’m young, and I’m short when I’m old. What am I?\n\n")
        elif response.lower() == "candle":
            main_output.insert(END,
                               ">*cell gates open*\nGreat job!\nMake sure to keep track of the answers to each riddle in the escape for the final room.\nWhere do you go?\n")
            answer_prison = True

        elif response.lower() == "candle":
            main_output.insert(END, ">*cell gates open*\nWhere do you go?\n")
            answer_lab = True
        elif response.lower() == "north" and answer_prison:
            room = 133
            main_output.insert(END,
                               f"\nYou have moved {response.lower()[-5:]}.")
            desc_output.delete(1.0, END)
            desc_output.insert(END, roomDescDict.get(str(room)) + '\n')

            main_output.yview(END)
            room_output.insert('1.0', f'Room: {room}\n')

        elif response.lower() == "east":
            main_output.insert(END, ">The wall is in the way.\n\n")
        elif response.lower() == "west":
            main_output.insert(END, ">The wall is in the way.\n\n")
        elif response.lower() == "south":
            main_output.insert(END, ">The wall is in the way.\n\n")
        else:
            main_output.insert(END, "I don't recognize this command.\n\n")
        e1.delete(0, END)
        e1.configure(state="normal")
    main_output.yview(END)


def room133():
    global answer_hall
    global room
    room = 133
    desc_output.insert(END, roomDescDict.get(str(room)) + '\n')
    response = e1.get()
    e1.delete(0, END)
    if response.lower() == "north":
        main_output.insert(END, ">The wall is in the way.")
    if response.lower() == "east" and (
            not answer_lab or not answer_cafe or not answer_grass or not answer_prison or not answer_hall or not answer_sewer):
        main_output.insert(END,
                           "\nThe door to the control panel is locked. You may not proceed without finding the answers to the riddles in the other rooms.\n")
    if response.lower() == "east" and (answer_lab and answer_cafe and answer_grass
                                       and answer_prison and answer_hall and answer_sewer):
        main_output.insert(END, ">The door to the control panel has opened after you cracked each of the riddles.\n")
        room = 143
        desc_output.delete(1.0, END)
        desc_output.insert(END, roomDescDict.get(str(room)) + '\n')
        main_output.insert(END,
                           f"\nYou have moved {response.lower()[-5:]}.")
        main_output.yview(END)

        room_output.insert('1.0', f'Room: {room}\n')

    if response.lower() == "west":
        room = 123
        main_output.insert(END,
                           f"\nYou have moved {response.lower()[-5:]}.")
        desc_output.delete(1.0, END)
        desc_output.insert(END, roomDescDict.get(str(room)) + '\n')
        main_output.yview(END)

        room_output.insert('1.0', f'Room: {room}\n')

    if response.lower() == "south":
        room = 132
        main_output.insert(END,
                           f"\nYou have moved {response.lower()[-5:]}.")
        desc_output.delete(1.0, END)
        desc_output.insert(END, roomDescDict.get(str(room)) + '\n')
        main_output.yview(END)

        room_output.insert('1.0', f'Room: {room}\n')

    if response.lower() == "orange":
        answer_hall = True
        main_output.insert(END, 'Good job!\nYou have cracked the next riddle!\nWhere do you go next?')
        main_output.yview(END)
        room_output.insert('1.0', f'Room: {room}\n')

    main_output.yview(END)


def room143():
    global room
    room = 143
    desc_output.delete(1.0, END)
    desc_output.insert(END, roomDescDict.get(str(room)) + '\n')
    main_output.yview(END)
    response = e1.get()
    e1.delete(0, END)
    if response.lower() == "west":
        room = 133
        main_output.insert(END,
                           f"\nYou have moved {response.lower()[-5:]}.")
        desc_output.delete(1.0, END)
        desc_output.insert(END, roomDescDict.get(str(room)) + '\n')

        main_output.yview(END)
        room_output.insert('1.0', f'Room: {room}\n')

    if response.lower() == "north":
        main_output.insert(END, 'You walked into the wall.\n')
    if response.lower() == "east":
        main_output.insert(END, 'You walked into the wall.\n')
    if response.lower() == "south":
        main_output.insert(END, 'You walked into the wall.\n')
    main_output.yview(END)
    if response.lower() == "coders":
        main_output.insert(END, '\nCongratulations! You have escaped the prison. You won!\n')


def input_command(e):
    if e1.get() == "":
        main_output.insert(END, ">Please enter a valid input\n\n")
        main_output.yview(END)
    elif e1.get() == 'help':
        main_output.insert(END, 'You are viewing the command list.')
        cmd_help_output.insert(END, roomDescDict.get('help'))
        main_output.yview(END)
        cmd_help_output.yview(END)
    desc_output.delete(1.0, END)
    while True:
        if room == 0o21:
            room_output.insert('1.0', f'Room: {room}\n')
            room021()
            break
        elif room == 113:
            room_output.insert('1.0', f'Room: {room}\n')
            room113()
            break
        elif room == 123:
            room_output.insert('1.0', f'Room: {room}\n')
            room123()
            break
        elif room == 124:
            room_output.insert('1.0', f'Room: {room}\n')
            room124()
            break
        elif room == 132:
            room_output.insert('1.0', f'Room: {room}\n')
            room132()
            break
        elif room == 133:
            room_output.insert('1.0', f'Room: {room}\n')
            room133()
            break
        elif room == 143:
            room_output.insert('1.0', f'Room: {room}\n')
            room143()
            break
    e1.delete(0, END)


heading1 = Label(root, text="Welcome to Riddler!", font="Arial")
heading1.place(x=100, y=20)
room_output = Text(root, font=('Arial', 14), borderwidth=2, height=1.2, width=9, wrap=WORD)
room_output.place(x=625, y=80)
main_output = ScrolledText(root, font=('Arial', 18), borderwidth=2, height=8, width=37, wrap=WORD)
main_output.place(x=425, y=170)

e1 = Entry(root, font=('Arial', 15), borderwidth=2, width=15, state="disabled")
e1.place(x=575, y=450)
e1.place(x=575, y=450)
b1 = Button(root, text="Submit", width=15, height=1, command=input_command)
b2 = Button(root, text="Start Game", width=15, height=1, command=room132)
b2.place(x=608, y=500)

root.bind('<Return>', input_command)

root.mainloop()

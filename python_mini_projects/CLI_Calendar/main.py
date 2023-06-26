"""
Calendar in the command line App
"""

import json
from time import sleep, strftime

user_first_name = "Francisco"

calendar = {}

def load_calendar():
    try:
        with open("events.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_calendar():
    with open("events.json", "w") as file:
        json.dump(calendar, file)

def welcome():
    print('Welcome, {}!'.format(user_first_name))
    print("Calendar starting...")
    sleep(1)
    print("Today is: " + strftime("%A %B %d, %Y"))
    print(strftime("%H:%M:%S"))

def start_calendar():
    global calendar
    calendar = load_calendar()
    welcome()
    start = True
    while start:
        user_choice = input("A to Add, U to Update, V to View, D to Delete, X to Exit: ")
        user_choice = user_choice.upper()

        if user_choice == "V":
            if len(calendar.keys()) < 1:
                print('Calendar is empty.')
            else:
                print(calendar)

        elif user_choice == "U":
            date = input("What date? ")
            update = input("Enter the update: ")
            calendar[date] = update
            save_calendar()
            print("Update successful.")
            print(calendar)

        elif user_choice == "A":
            event = input("Enter event: ")
            date = input("Enter date (MM/DD/YYYY): ")
            if len(date) > 10 or int(date[6:]) < int(strftime("%Y")):
                print("You have entered an invalid date.")
                try_again = input("Try Again? Y for Yes, N for No: ")
                try_again = try_again.upper()
                if try_again == 'Y':
                    continue
                else:
                    start = False
            else:
                calendar[date] = event
                save_calendar()
                print("Event added successfully.")
                print(calendar)

        elif user_choice == "D":
            if len(calendar.keys()) < 1:
                print('Calendar is empty.')
            else:
                event = input("What event?")
                for date in calendar.keys():
                    if event == calendar[date]:
                        del calendar[date]
                        save_calendar()
                        print("The event was successfully deleted.")
                        break
                else:
                    print('There is no event with that name in the calendar.')

        elif user_choice == "X":
            start = False

        else:
            print('')
            start = False

start_calendar()


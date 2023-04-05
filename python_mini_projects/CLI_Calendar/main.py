"""
Calendar in the command line App
"""
from time import sleep, strftime

user_first_name = "Francisco"

calendar = {}

def welcome():
  print('welcome {} to your calendar'.format(user_first_name))
  print ("Calendar starting...")
  sleep(1)
  print ("Today is: " + strftime("%A %B %d, %Y"))
  print (strftime("%H:%M:%S"))

def start_calendar():
  welcome()
  start = True
  while start:
    user_choice = input("A to Add, U to Update, V to View, D to Delete, X to Exit: ")
    user_choice = user_choice.upper()

    if user_choice == "V":
      if len(calendar.keys()) < 1:
        print('calendar empty')
      else:
        print(calendar)

    elif user_choice == "U":
      date = input("What date? ")
      update = input("Enter the update: ")
      calendar[date] = update
      print("update sucesfull")
      print(calendar)

    elif user_choice == "A":
      event = input("Enter event: ")
      date = input("Enter date (MM/DD/YYYY): ")
      if (len(date) > 10) or (int(date[6:]) < int(strftime("%Y"))):
        print("you have entered an invalid date")
        try_again = input("Try Again? Y for Yes, N for No: ")
        try_again = try_again.upper()
        if try_again == 'Y':
          continue
        else:
          start = False   
      else:
        calendar[date] = event 
        print("update sucesfull")
        print(calendar)  

    elif user_choice == "D":
      if len(calendar.keys()) < 1:
        print('calendar empty')
      else:
        event = input("What event?")
        for date in calendar.keys():
          if event == calendar[date]:
            del (calendar[date])
            print("the event was succesfully deleted")
          else:
            print('There is no event with that name in the calendar')
    elif user_choice == "X":
      start = False
      
    else:
      print('')
      start = False

start_calendar()   
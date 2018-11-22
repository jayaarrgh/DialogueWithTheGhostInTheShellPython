from os import system, name 
  
# import sleep to show output for some time period 
from time import sleep 
  
# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')
 

class Messenger:
    #TODO: speech synthesis

    def inform_user_of_exit():
        clear()
        print("Press ESC at any time to leave")
        sleep(1.25)
        clear()

    def display_node(n):
        clear()
        print(n.text)
        print("-----------------------------------")
        print("Type a response number: ")
        i = 1
        for option in n.options:
            print(f"{i}: {option.text}")
            i += 1
        print("-----------------------------------")

    def escape_key_hit():
        clear()
        print("Are you sure you want to leave?")
        print("Press ESC to leave, OR anything else to stay")

    def player_wants_to_leave():
        clear()
        print("Maybe I don't want to let you leave")
        sleep(.8)
        print("...")
        sleep(.8)
        print("Just kidding")
        sleep(.8)
        print("See ya later!")
        sleep(1)

    def player_wants_to_stay():
        clear()
        print("Im glad you want to stay a little longer")
        sleep(2)
        clear()
    
    def range_exception():
        clear()
        print("That number isn't going to work")
        sleep(1.75)
        clear()

    def format_exception():
        clear()
        print("Are you even trying?")
        sleep(1)
        clear()
        print("Please enter a number from the options displayed")
        sleep(1.75)
        clear()

    def clear():
        clear()
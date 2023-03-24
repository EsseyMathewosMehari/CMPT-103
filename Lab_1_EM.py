#  ----------------------------------------------------
#  I  acknowledge this program is my own work. 
#  Name: Essey Mehari
#  ----------------------------------------------------

# In this function we are collecting input form a user indicating them to put a number between 1-5. 
def get_choice():
    #While the condition is meant we will continue on with the program(Note to self, do not make while true for next lab)
    while True:
        try:
            choice = int(input("Please enter a number between 1 and 5: "))
            if choice >= 1 and choice <= 5:
                return choice
            else:
                print("Invalid input. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            
def get_input(iterable):
    #accepts an iterable object named iterable as its parameter and returns 3-tuples back The function returns a 3-tuple: the first and secound integer and either -1 if the user entered D or 1 if the user entered A.
    while True:
        #Note to self, do not make while true for next lab)
        order = input("Please enter 'A' for ascending or 'D' for descending: ").upper()
        if order not in ['A', 'D']:
            print("Invalid input. Please enter 'A' for ascending or 'D' for descending.")
            continue
        break
    while True:#Note to self, do not make while true for next lab)
        try:
            first_index = int(input("Please enter an integer between 0 and {}: ".format(len(iterable)-1)))
            if 0 <= first_index < len(iterable):
                break
            else:
                print("Invalid input. Please enter an integer between 0 and {}.".format(len(iterable)-1))
        except ValueError:
            print("Invalid input. Please enter an integer between 0 and {}.".format(len(iterable)-1))
    while True:#Note to self, do not make while true for next lab)
        try:
            second_index = int(input("Please enter another integer between 0 and {}: ".format(len(iterable)-1)))
            if 0 <= second_index < len(iterable):
                break
            else:
                print("Invalid input. Please enter another integer between 0 and {}.".format(len(iterable)-1))
        except ValueError:
            print("Invalid input. Please enter another integer between 0 and {}.".format(len(iterable)-1))
    return (first_index, second_index, 1 if order == 'A' else -1)

def loops(start, stop, step, iterable):#accepts four arguments and checking if start is greater than stop in the casse that it is it will switch the values
    if step > 0 and start > stop:
        start, stop = stop, start
    elif step < 0 and start < stop:
        start, stop = stop, start
    print('Output for "for" loop:')        
    for i in range(start, stop, step):#use a for loop to display the sequence ofumbers horizontally
        print(i, end=' ')
    print()
    i = start
    print('Output for "while" loop:')
    while i != stop:#and a while loop to display the numbers horizontally.
        print(i, end=' ')
        i += step
    print()            
            
def main():#This function displays a menu
    iterable = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]#Within this function we haveiterable objects
    while True:#Note to self, do not make while true for next lab)
        print("Options:\n1. Demo 'for' and 'while' loops")
        print("2. Display 'Option 2 selected")
        print("3. Display 'Option 3 selected")
        print("4. Display 'Option 4 selected")
        print("5. Quit\n")
        choice =(input("Select option (1-5):"))
        choice = int(choice)
        
        #gets a choice from the user, and executes that choice.
        if choice == 1:
            iterable=[0,1,2,3,4]
            loops(4,2,1,iterable)
        elif choice == 2:
            print("Option 2 selected\n")
        elif choice == 3:
            print("Option 3 selected\n")
        elif choice == 4:
            print("Option 4 selected\n")
        elif choice == 5:
            print("Goodbye")
            break 
        else:
            print("Invalid choice. Please enter a number between 1 and 5.\n")  

main()
#---------------------------------
# Name:Essey Mehari
# Program: Lab_8_EM.py
#----------------------------------
#I certify that this work is mine
#----------------------------------
#The code defines a class called ComboLock which represents a combination lock. The constructor takes in three parameters representing the correct number of clockwise turns, the correct number of counterclockwise turns, and the correct number of clockwise turns again, respectively. It initializes the lock with no code set, and checks if the inputs are integers and within a valid range.
class ComboLock:
    #This code defines the "ComboLock" class with three parameters: cw1 for the first correct clockwise turn, ccw1 for the second correct counterclockwise turn, and cw2 for the last correct clockwise turn. The purpose of this initialization is to set up the necessary variables and perform error checking.
    def __init__(self,cw1,ccw1,cw2):
        code1 = "None"
        code2 = "None"
        code3 = "None"
        self.code1 = code1
        self.code2 = code2
        self.code3 = code3
        try: 
            cw1 = int(cw1)
            ccw1 = int(ccw1)
            cw2 = int(cw2)
        except:
            raise TypeError("wrong type, please input an integer")
        self.cw1 = cw1
        self.ccw1 = ccw1
        self.cw2 = cw2        
        dial = 0
        self.dial = dial        
        if cw1 > 59 or cw1 < 0 and ccw1 > 59 or ccw1 < 0 and cw2 > 59 or cw2 < 0:
            raise ValueError("value out of bounds. ")
    #resetting the dial and turns to 0
    def reset(self):
        self.dial = "None"
        self.code1 = "None"
        self.code2 == "None"
        self.code3 = "None"
    #to allow the lock to be printable and returns a a printable version of the class
    def __repr__(self):
       
        return f'ComboLock({self.cw1}, {self.ccw1}, {self.cw2})'
    
    #number of ticks to rotate the lock, decision - an integer representing the decision to rotate the lock either for the first or second clockwise movement (third if counting counterclockwise) determies easy manipulation of the first and second clockwise rotations    
    def turn_clockwise(self, tick, decision): #for decision, 1 stands for the first clockwise rotaion, 2 stands for second clockwise rotation respectively.
        if decision == 1:
            if self.code1 == "None":
                self.code1 = 0
            self.code1 += tick
            self.dial = (self.dial + (tick%60))%60
        elif decision == 2:
            if self.code3 == "None":
                self.code3 = 0            
            self.code3 += tick
            self.dial = (self.dial + (tick%60))%60
        else:
            raise ValueError("please input 1 for the first clockwise turn and 2 for the counterclockwise turn")
        
    #updates the lock's state by adding to the second code, which is used in the process of trying to open the lock.
    def turn_counterclockwise(self, ctick):
        if self.code2 == "None":
            self.code2 = 0        
        self.code2 += ctick
        self.dial = (self.dial - (ctick%60))%60
    #The method returns a tuple of four items that represent the current state of the lock. The first item in the tuple is the current position of the lock dial. The second, third, and fourth items are the current values of the three codes that the user has entered.
    def get_state(self):
        return (self.dial, self.code1, self.code2, self.code3)
    
    #Checks whether the current state of the lock's three codes (code1, code2, and code3) matches the correct values (cw1, ccw1, and cw2), and returns True if the lock is open or False otherwise.
    def is_open(self):
        if self.code1 == self.cw1 and self.code2 == self.ccw1 and self.code3 == self.cw2:
            return True
        else:
            return False
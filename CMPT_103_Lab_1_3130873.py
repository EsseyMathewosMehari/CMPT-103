# ID# 3130873
# Lab 1


#Define a function called count_hyphens
def count_hyphens():
    #Prompt the user to enter a string and store it in the variable userinput
    userinput = input('Please enter a string: ')
    
    #Check if the input string contains a hyphen ('-')
    if '-' in userinput:
        #If it contains hyphens, print the count of hyphens in the string
        print('The string contains', userinput.count('-'), 'hyphen(s)\n')
    else:
        #If it doesn't contain hyphens, print that there are 0 hyphens
        print('The string contains 0 hyphen(s)\n')
    return userinput.count('-')



#Define a function called moon_weight
def moon_weight():
    #Ask the user for their weight here on Earth
    weight = float(input('What is the weight you would like to know on the moon (units will be the same)?: '))
    #Calculate the weight on the moon
    moonweight = (weight/9.81)*1.62
    #Return the moon weight as a string
    #asked instructor to give me an idea on how to do the rounding
    print('On the moon', weight, 'units of weight converts into', round(moonweight,2),'units of weight\n')
    return str(round(moonweight,2))

#Define a function called last_word
def last_word(s:str):
    #Split the string by spaces to separate words
    words = s.split()
    
    # Check if there are any words in the list
    if words:
        # Get the last word from the list
        last_word = words[-1]
        
        # Return the length of the last word as an integer
        return len(last_word)
    else:
        # If no words found, return 0
        return 0
    
    
#Calls the above functions
count_hyphens()
moon_weight()
last_word('hey')
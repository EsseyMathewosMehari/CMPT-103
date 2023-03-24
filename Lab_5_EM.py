#---------------------------------
# Name:Essey Mehari
# Program: Lab_5_EM.py
#----------------------------------


from pprint import pprint
#In this function, we first try to open the file using with open statement, which automatically closes the file once we're done. If the file does not exist, the FileNotFoundError exception will be caught by the except block, and the function will print "File does not exist" and return nothing. Once all rows have been processed, we return the data list of lists.

def open_file(filename):
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            data = []
            header_skipped = False
            for row in reader:
                if not header_skipped:
                    header_skipped = True
                    continue
                try:
                    year_discovered = int(row[7])
                except ValueError:
                    year_discovered = 0
                row_data = [int(row[0]), row[1], row[2], row[3], row[4], int(row[5]), int(row[6]), float(row[8]), year_discovered]
                data.append(row_data)
        return data
    except FileNotFoundError:
        print("File does not exist")

#This function takes a list of lists as input, loops through each row in the list, extracts the atomic mass value from the row, and modifies it by removing any brackets and converting it to a float. The updated atomic mass value is then assigned back to the same position in the original list of lists. Finally, the modified list of lists is returned.
def clean_atomic_mass(data):
    for row in data:
        atomic_mass = row[3]
        if atomic_mass.startswith('['):
            # Remove square brackets and convert to float
            atomic_mass = float(atomic_mass[1:-1])
        else:
            # Remove round brackets and number and convert to float
            atomic_mass = float(atomic_mass.split('(')[0])
        row[3] = atomic_mass
    return data
#This function first checks if the start and end arguments are integers and if the start is before the end. If not, it prints an error message and returns None. It then calls the validate_range function with the start and end arguments to ensure that they are within the range of known discovery dates.
def discovery_date(data, start, end):
    if not type(start, int) or not type(end, int) or start > end:
        print("Years must integers or the start must be before the end")
        return None

    validate_range(start, end)
    discoveries = []
    for element in data:
        year = element[1]
        if start <= year <= end:
            discoveries.append((year, element[0]))
    return sorted(discoveries)
#This function first checks whether both start and end are integers using the type() function. If either of them is not an integer, the function returns False.

#Next, the function checks whether start is greater than end. If it is, the function returns False, since this would represent an invalid range.

#If both checks pass, the function returns True, indicating that the range is valid.
def validate_range(start, end):
    if not type(start, int) or not type(end, int):
        return False
    elif start > end:
        return False
    else:
        return True
#To begin with, this function determines whether the state parameter is a string and whether the result of validate state(state) is True. The method returns False if one or both checks are unsuccessful.
    
#Each row of the data list of lists is looped through if the status is valid. The function examines each row to determine whether the element's standard state (column 7 of the row) corresponds to the state parameter (ignoring case). If so, the function retrieves the element's name from column 2 of the row and the year it was found from column 4 of the row, adding a tuple with this data to the elements list.
def standard_state(data, state):
    if not type(state, str) or not validate_state(state):
        return False
    
    elements = []
    for row in data:
        if row[7].lower() == state.lower():
            element_name = row[2]
            year_discovered = int(row[4])
            elements.append((element_name, year_discovered))
    
    elements.sort()
    return elements
#The type() method is used to determine whether the parameter is a non-string first. It returns False if the value is not a string. If not, it makes the string case-insensitive by converting it to lowercase using the lower() method. Next, using a list of strings, it determines if the lowercase state is one of the permitted values. It returns False if it isn't in the list. Lastly, it returns True if the state is a valid string.
def validate_state(state):
    if not type(state, str):
        return False
    state = state.lower()
    if state not in ['solid', 'liquid', 'gas']:
        return False
    return True

#Here, we first determine whether or not the string parameter is a string. We return a message in the event that it is not a string. If not, we cycle over each entry in the data list and check—case-insensitively—whether its symbol begins with the supplied text. If a match is discovered, we add a tuple with the element's name and symbol to the list of matching elements.
#If no matches are found, we provide an error message. Otherwise, we return the list of matched items sorted from A to Z by element name.
def find_names(data, string):
    if not type(string, str):
        return "There are no elements with " + str(string)
    
    matching_elements = []
    for element in data:
        if element[1].lower().startswith(string.lower()):
            matching_elements.append((element[0], element[1]))
            
    if not matching_elements:
        return "There are no elements that start with \"" + string + "\""
    
    return sorted(matching_elements, key=lambda x: x[0])

def main():
    filename = 'periodic_table.csv'
    data = open_file(filename)
    cleaned_data = clean_atomic_mass(data)
    
    # Testing the discovery_date function
    element = 'Oxygen'
    discovery = discovery_date(cleaned_data, element)
    print(f"The discovery date of {element} is {discovery}")
    
    # Testing the validate_range function
    start_year = 1900
    end_year = 2000
    is_valid = validate_range(start_year, end_year)
    print(f"Is the range valid? {is_valid}")
    
    # Testing the standard_state function
    state = 'gas'
    elements = standard_state(cleaned_data, state)
    print(f"The elements that are {state} at room temperature are: {elements}")
    
    # Testing the validate_state function
    state = 'plasma'
    is_valid = validate_state(state)
    print(f"Is {state} a valid state? {is_valid}")
    
    # Testing the find_names function
    symbol = 'H'
    names = find_names(cleaned_data, symbol)
    print(f"The element(s) with the symbol {symbol} is/are: {names}")

main()
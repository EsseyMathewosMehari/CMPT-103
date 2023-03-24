import csv
import pickle

# This method provides a list of lists containing the data from the CSV file and accepts a
#  filename string as an argument. The first four rows of data are skipped by the function,
#  which reads the file using the csv module. The strings are then converted to numbers using
#  a layered list comprehension as necessary. The function produces an error message and returns 
# None in the event that the file cannot be opened or is invalid. Keep in mind that, as asked, the 
# try and except lines are used to handle errors.
def open_file(filename):
    try:
        with open(filename, newline='') as csvfile:
            datareader = csv.reader(csvfile)
            data = []
            for row in datareader:
                if datareader.line_num > 4:
                    row_data = []
                    for item in row:
                        try:
                            row_data.append(int(item))
                        except ValueError:
                            row_data.append(item)
                    data.append(row_data)
        return data
    except FileNotFoundError:
        print(f"{filename} not found.")
        return None
    except csv.Error:
        print(f"{filename} is not a valid csv file.")
        return None
# An empty dictionary and the raw data list of lists supplied by open file are the 
# only inputs for this function. Iteratively processing each row of the raw data, it 
# extracts the name, frequency, gender, and year and adds them to a list that is stored as
#  the value of the name key in the dictionary. A new key is inserted with an empty list as 
# the value if the name is not already present in the dictionary. The dictionary is then sent,
#  complete with values for the frequency, gender, and year lists that match to the name keys.
def create_names_dict(raw_data, names_dict):
    for row in raw_data:
        name = row[1]
        if name not in names_dict:
            names_dict[name] = []
        names_dict[name].append(row[2:])
    return names_dict
# An empty dictionary and the raw data list of lists supplied by open file are the only 
# inputs for this function. It iteratively analyses the raw data, extracting the rank, name,
#  frequency, gender, and year from each row. The year is added as a new key with an empty list 
# for both "Boy" and "Girl" if there is not already one in the top ten dict. The rank, name, frequency, 
# and gender are included to the list if the number of names for the gender in the corresponding year 
# is fewer than 10. When all rows have been processed, the top ten dict dictionary, which uses years
#  as keys to identify the top ten boy's names and top ten girl's names, as well as a list of lists 
# with rank, name, and gender in each entry,
def create_top_ten_dict(raw_data, top_ten_dict):
    for row in raw_data:
        rank = row[0]
        name = row[1]
        gender = row[3]
        year = row[4]
        if gender == 'Boy':
            if year not in top_ten_dict:
                top_ten_dict[year] = []
            if rank <= 10:
                top_ten_dict[year].append([rank, name, gender, year])
        else:
            if year not in top_ten_dict:
                top_ten_dict[year] = []
            if rank <= 10:
                top_ten_dict[year].append([rank, name, gender, year])
    return top_ten_dict


# If no filename is entered when the user is prompted for one, the default filename is used.
#  The raw data is then used to update the names dict and top ten dict using the create names 
# dict and create top ten dict functions, respectively, after calling open file to extract the
#  data from the CSV file. The maximum year in the names dict is used to calculate the most recent 
# year as well. Lastly, it returns the most recent year and the updated dictionaries. The original
#  dictionaries and None for the most recent year are returned if there is a problem loading the 
# file, along with an error message.
def load_file(default_filename, names_dict, top_ten_dict):
    filename = input(f"Enter a file name [{default_filename}]: ").strip() or default_filename
    raw_data = open_file(filename)
    if raw_data:
        names_dict = create_names_dict(raw_data, names_dict)
        top_ten_dict = create_top_ten_dict(raw_data, top_ten_dict)
        latest_year = max([row[4] for row in raw_data])
        return names_dict, top_ten_dict, latest_year
    
# A filename, a dictionary of names, and a dictionary of top ten lists are required inputs 
# for this function. It determines whether or not the filename is given. It changes the filename
#  to the default value of "baby names.pkl" if no filename is specified. Next, using the "wb" 
# mode specifier, it opens the file in binary write mode and uses the pickle.dump method to save 
# the names and top ten dictionaries in the file.
def pickle_dicts(default_filename, names_dict, top_ten_dict):
    filename = input(f"Enter a file name [{default_filename}]: ")
    if filename == "":
        filename = default_filename
    try:
        with open(filename, 'wb') as file:
            pickle.dump((names_dict, top_ten_dict), file)
    except:
        print("Error: could not save file")

# This function prompts the user for a filename, and if none is entered, uses the default filename.
#  It then attempts to open the file and load the pickled data. If the file is not found or the file 
# format is invalid, it prints an error message and returns None. Otherwise, it returns the loaded data 
# as a tuple of dictionaries.
def load_pickle(default_filename='baby_names.pkl'):
    try:
        filename = input('Enter a file name [' + default_filename + ']: ').strip()
        if filename == '':
            filename = default_filename
        with open(filename, 'rb') as f:
            data = pickle.load(f)
            return data
    except FileNotFoundError:
        print('File not found.')
    except (pickle.UnpicklingError, EOFError):
        print('Invalid file format.')
    return None

def main():
    # Create empty dictionaries for names and top ten lists
    names_dict = {}
    top_ten_dict = {}

    # Display menu
    while True:
        print("Alberta Baby names")
        print("--------------------")
        print("(0) Quit")
        print("(1) Load and process spreadsheet file")
        print("(2) Save processed data")
        print("(3) Open processed data")
        print("(4) Search for a name")

        # Get menu choice from user
        choice = input("Enter command: ")

        # Error check to ensure valid choice
        if choice not in ["0", "1", "2", "3", "4"]:
            print("Invalid choice. Please enter a valid choice.")
            continue

        # Execute user's choice
        if choice == "0":
            # Quit
            print("Goodbye")
            return
        elif choice == "1":
            # Load and process spreadsheet file
            filename = input("Enter a file name [baby-names-frequency_1980_2021.csv]: ") or "baby-names-frequency_1980_2021.csv"
            try:
                raw_data = open_file(filename)
                names_dict = create_names_dict(raw_data, {})
                top_ten_dict = create_top_ten_dict(raw_data, {})
                latest_year = max(names_dict.values())[0][0][2]
                print("File loaded and processed successfully.")
            except FileNotFoundError:
                print(f"Could not find file {filename}. Please enter a valid filename.")
            except:
                print("An error occurred while processing the file.")
        elif choice == "2":
            # Save processed data
            if not names_dict or not top_ten_dict:
                print("There are no data.")
                continue
            filename = input("Enter a file name [baby_names.pkl]: ") or "baby_names.pkl"
            try:
                pickle_dicts(filename, names_dict, top_ten_dict)
                print("Data saved successfully.")
            except:
                print("An error occurred while saving the data.")
        elif choice == "3":
            # Open processed data
            filename = input("Enter a file name [baby_names.pkl]: ") or "baby_names.pkl"
            try:
                names_dict, top_ten_dict = load_pickle(filename)
                print("Data loaded successfully.")
            except FileNotFoundError:
                print(f"Could not find file {filename}. Please enter a valid filename.")
            except:
                print(f"Could not load pickle from file {filename}.")
        elif choice == "4":
            # Search for a name
            if not names_dict or not top_ten_dict:
                print("There are no data.")
                continue
            name = input("Enter a name to search for: ")
            result = names_dict(name, names_dict)
            if result:
                print(f"Name: {name}")
                for entry in result:
                    print(f"Year: {entry[2]}, Gender: {entry[1]}, Frequency: {entry[0]}")
            else:
                print(f"No entries found for name {name}.")
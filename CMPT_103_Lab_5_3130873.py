# Question 1
# for the following function what happens when the first line of the file baby_names.csv is processed?
# the line contains the text:
# "name","year","percent","sex"\n

def get_babynames_for_loop():
     with open("baby_names.csv", "r") as f:
         data = []
         for line in f.readlines()[1:]:
             sub_data = []
             for i, entry in enumerate(line.strip().split(",")):
                 if i != 3:
                     sub_data.append(entry.strip('"'))
             data.append(sub_data)
     return data
# A read-only window is established for the "baby_names.csv" file.
# An empty list is used as the variable data's first value.
# The for loop loops over the file's lines one by one.
#The operation strip().split(",") separates the line into a list.
# The if i!= 3 condition determines if the current element is not at index 3. The sex column is skipped by the code.
# The data list will be attached to the sub_data list ['name', 'year', 'percent'] that is created after processing the first line.
# In order to add cleaned data from # The lines to the data list, the method is repeated for each line in the file, skipping the first 
# line that contains the column headers. The final result is a list of lists that don't have the "sex" column but still contain the data from the CSV.


# for the following function what happens when the second line of the file baby_names.csv is processed?
# the line contains the text:
# "Tommie",1880,0.00022899999999999998,"boy"\n
#
def get_babynames_for_loop():
     with open("baby_names.csv", "r") as f:
         data = []
         for line in f.readlines()[1:]:
             sub_data = []
             for i, entry in enumerate(line.strip().split(",")):
                 if i != 3:
                     sub_data.append(entry.strip('"'))
             data.append(sub_data)
     return data
# A read-only window is established for the "baby_names.csv" file.
# An empty list is used as the variable data's first value.
# The file is opened and the line "Tommie",1880,0.00022899999999999998,"boy"n is read.
# The line is divided into a list by the operation line.strip().split(","), producing the result list ['"Tommie"', '1880', '0.00022899999999999998', '"boy"n']
# This list is iterated through in the outer for loop.
# The "sex" column, which is at index 3 (zero-based index), is checked to determine whether the current element is not in it by checking whether i!=3. 
# The code omits the "Sex" column.
#Once the second line has been processed, the resultant sub_data list will be ['Tommie', '1880', '0.00022899999999999998'] 
# ^and the data list will be enlarged to include this list.
# The procedure is repeated for each line in the file, omitting the first line that contains the column headers, and the cleaned data from the other 
# lines is used to fill the data list. The end output is a list of lists without the "sex" column that contains the information from the CSV file.

# Question 2
# Annotate the function for each line of the following code.
# Explain what each statement does.

def get_babynames_for_loop():
     # Open the "baby_names.csv" file in read mode and create a context using the 'with' statement
     with open("baby_names.csv", "r") as f:
         # Initialize an empty list to store the extracted data
         data = []
         # Iterate through the lines of the file, starting from the second line (index 1)
         for line in f.readlines()[1:]:
             # Initialize an empty list to store the data for the current line.
             sub_data = []
             # Split the line into elements using a comma as the delimiter and iterate through them
             for i, entry in enumerate(line.strip().split(",")):
                 # Check if the current element is not the fourth element (index 3), which is the "sex" column
                 if i != 3:
                     # Remove double quotes around the element and append it to the 'sub_data' list
                     sub_data.append(entry.strip('"'))
                     # Append the 'sub_data' list (representing data for one line) to the 'data' list
             data.append(sub_data)
             # Return the 'data' list containing the extracted data from the CSV file (excluding the "sex" column)
     return data

# List comprehension is used to condense the data list in the get_babynames_list_comprehension version. The code may be made 
# shorter and simpler to understandby using list comprehension to create lists from existing data in a more expressive and compact manner
def get_babynames_list_comprehension():
    with open("baby_names.csv", "r") as f:
        return [
            [x.strip('"') for i, x in enumerate(line.strip().split(",")) if i != 3]
            for line in f.readlines()[1:]
        ]


def get_babynames_for_loop():
    with open("baby_names.csv", "r") as f:
        data = []
        for line in f.readlines()[1:]:
            sub_data = []
            for i, entry in enumerate(line.strip().split(",")):
                if i != 3:
                    sub_data.append(entry.strip('"'))
            data.append(sub_data)
    return data

# If the data transformation becomes more complex, the get_babynames_for_loop version with nested loops and 
# explicit variable names might be easier to understand and maintain.
# 'get_babynames_for_loop' does a good step by step breakdown even though as mentioned above it may be harder in the future with more complexity.
if __name__ == "__main__":
    data = get_babynames_for_loop()
    print(data[0:5])


def most_popular(name: str) -> int:
    """
    Find the year in which a given name was most popular.

    Argument:
        name: The name to search for. Case-insensitive search is performed.

    Returns:
        The year in which the name was most popular, or -1 if the name is not found in the dataset.

    The function reads data from a CSV file containing name and year information. It disregards the 'sex' column
    and performs a case-insensitive search for the input name. If the name is found in the dataset, it returns the
    year in which it was most popular. If the name is not found, it returns -1.
    """
     # Create a dictionary to store names as keys and years as values.
    name_data = {}

    # Open the CSV file and read data into the dictionary.
    with open("baby_names.csv", "r") as f:
        for line in f.readlines()[1:]:
            data = line.strip().split(",")
            name_data[data[0].lower()] = int(data[1])  # Convert the name to lowercase for case-insensitive matching

    # Check if the name exists in the dictionary.
    if name.lower() in name_data:
        return name_data[name.lower()]
    else:
        return -1
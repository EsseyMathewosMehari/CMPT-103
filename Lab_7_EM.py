#---------------------------------
# Name:Essey Mehari
# Program: Lab_7_EM.py
#----------------------------------
#I certify that this work is mine
#----------------------------------
# Prompt user for filename
filename = input("Filename for CSV file: ")
filename = "temps/" + filename  # add "temps/" to filename

# Load data from file into dictionary of lists
data = {}
try:
    with open(filename) as file:
        for line in file:
            line = line.strip().split(",")
            city = line[0]
            temperatures = [float(temp) for temp in line[1:]]
            data[city] = temperatures
except FileNotFoundError:
    print("File not found")

# Create plot window
win = GraphWin("Temperature Plot", 500, 500)
win.setCoords(1, -50, 31, 50)

# Plot data
colors = ["red", "green", "blue", "black", "orange"]
legend_x, legend_y = 2, 45
for i, (city, temps) in enumerate(data.items()):
    color = colors[i % len(colors)]
    for j, temp in enumerate(temps):
        x = j + 1
        y = temp
        pt = Point(x, y)
        pt.setFill(color)
        pt.draw(win)
    legend_pt = Point(legend_x, legend_y - i*2)
    legend_text = Text(legend_pt, city)
    legend_text.setFill(color)
    legend_text.draw(win)

# Initialize value label
value_text = Text(Point(15, -45), "Value: N/A")
value_text.draw(win)

# Handle user clicks

click = win.getMouse()
x, y = click.getX(), click.getY()
if 1 <= x <= 31 and -50 <= y <= 50:
    value = round(y, 2)
    value_text.setText("Value: {}".format(value))
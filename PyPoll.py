# Exercise 3.4.2

# To access and open a file for which the direct path is unknown, we use the os module.
import os
import csv

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv") # To declare a variable for the file to load.

# Open the election results and read the file.
with open(file_to_load) as election_data:

# Read the file object with the reader function.
    file_reader = csv.reader(election_data)

 # Exercise 3.4.4
 
    # Print the header row.
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file.
    #for row in file_reader:
        #print(row)

# Print the file object.
    print(election_data)

# Exercise 3.4.3
 
# Assign a variable to save the file to a path. This is to save analysis into the OS.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Use the open() function in the "w" mode to open a file and write data to the file.
open(file_to_save, "w") # To work, an empty folder has to be created in the Election_Analysis folder named Analysis. 

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write three counties to the file. Add a comma and space after the county. \n is like hitting return.
    txt_file.write("""Counties in the Election
    
    ------------------------------------------\n""")
    
    txt_file.write("Arapahoe\nDenver\nJefferson")

# Close the file
outfile.close()





#To do: perform analysis.

# Close the file.
election_data.close()
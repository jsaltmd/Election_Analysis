print("Hello World")

print("--------------------------------------------------")

# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")

print("--------------------------------------------------")

counties = ["Arapahoe", "Denver", "Jefferson"]
if counties [1] == 'Denver' :
    print(counties[1])

print("--------------------------------------------------")

temperature = int(input("What is the temperature outside?"))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows")

print("--------------------------------------------------")

#What is the score?
score = int(input("What is your test score?"))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
else:
    if score >=80:
        print('Your grade is B.')
    else:
        if score >= 70:
            print('Your grade is a C.')
        else:
            if score >= 60:
                print('Your grade is a D.')
            else:
                print('Your grade is an F.')

print("--------------------------------------------------")

# What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')

print("--------------------------------------------------")

counties = ["Arapahoe", "Denver", "Jefferson"]
if "El paso" in counties:
    print("El paso is in the listi of counties.")
else:
    print("El Paso is not in the list of counties.")

print("--------------------------------------------------")

if "Arapahoe"in counties and "El Paso" in counties:
    print("Arapahoe and El paso are in the list of counties.")
else:
    print("Arapahoe or El paso is not in the list of counties.")

print("--------------------------------------------------")

if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El paso is not in the list of counties.")

print("--------------------------------------------------")

x = 0
while x <=5:
    print(x)
    x = x + 1
    
print("--------------------------------------------------")

for county in counties:
    print(county)

print("--------------------------------------------------")

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

print("--------------------------------------------------")

for i in range(len(counties)):
    print(counties[i])

print("--------------------------------------------------")

counties_dict = {}

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict:
    print(county)

print("--------------------------------------------------")

for county in counties_dict.keys():
    print(county)

print("--------------------------------------------------")

for voters in counties_dict.values():
    print(voters)

print("--------------------------------------------------")

#Creating a voting_data dictionaries

voting_data = {}

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

print("--------------------------------------------------")

#Using range here

for i in range(len(voting_data)):

      print(voting_data[i])

print("--------------------------------------------------")

#Retrieve only the values from each dictionary in the list of dictionaries, we need to use a nested for loop.

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

print("--------------------------------------------------")

#If we only want to print the county name from each dictionary, we can use county_dict['county'] in the print statement 
 
for county_dict in voting_data:
    print(county_dict['county'])

print("--------------------------------------------------")

#If we only want to print the registered voters from each dictionary, we can use county_dict['registered voters'] in the print statement 

for county_dict in voting_data:
    print(county_dict["registered_voters"])

print("--------------------------------------------------")

#The print() Function
#F-strings: Formatted String Literals

#Skill drill 3.2.10:

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}

for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

print("--------------------------------------------------")

#Skill drill 3.2.11

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")

print("--------------------------------------------------")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

print("--------------------------------------------------")

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)

print("--------------------------------------------------")

# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)

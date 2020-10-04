grocery_list = ["Milk","Bread","Eggs","Peanut_Butter","Jelly"]
print(grocery_list)
grocery_list[3]="Almond Butter"
print(grocery_list)
grocery_list.remove("Jelly")
print(grocery_list)
grocery_list.append("Coffee")
print(grocery_list)

print("----------------------------------------------------------------")

my_hobbies = {
    "name": "John Salvador",
    "age" : 44,
    "hobbies": [
        "sports",
        "hiking",
        "singing"],
    "wake_up_times":{"Mon":"7am", "Tue":"8am", "Wed":"10am"},
    }
print(f"My name is {my_hobbies["name"]}, I am {my_hobbies["age"]}, My hobby is {my_hobbies["hiking"]")
print(f"I wake up at {my_hobbies["wake_up_times"]["Mon"]}")

print("----------------------------------------------------------------")

for i in range(5)
    print(i)

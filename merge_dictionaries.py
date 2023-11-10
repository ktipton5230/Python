#define the merge function to combine dictionaries
#to find the GPA of students in class
def merge(dict1, dict2):
    for i in dict2.keys():
        dict1[i]=dict2[i]
    return dict1


dict1 = {
    "Fred": "Student",
    "Samantha": "Student",
    "Jeffery": "Teacher",
    "John": "Student",
    "Jacob": "Student",
    "Jimmy": "Student"
}

dict2 = {

    "Fred": 4.0,
    "Samantha": 3.6,
    "Jeffery": "N/A",
    "John": 3.7,
    "Jacob": 2.7,
    "Jimmy": 3.0
}

dict3 = merge(dict1, dict2)

print(dict3)


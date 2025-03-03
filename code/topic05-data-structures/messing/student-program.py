students = {}
new_name = "blank"
while new_name != "":
    new_name = input("Enter name: ")
    if new_name == "":
        break
    students[new_name]={"modules":[]}
    new_module="blank"
    while new_module != "":
        new_module = input("Enter module name: ")
        if new_module== "":
            break
        new_grade = input("Enter grade: ")
        students[new_name]["modules"].append({"name":new_module,"grade":new_grade})

print(students)

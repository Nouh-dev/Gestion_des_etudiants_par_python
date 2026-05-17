# students management 
from openpyxl import Workbook
n = int(input("Enter numbers students: "))
students = []

def save_excel():
    page_excel = Workbook()
    page = page_excel.active
    page.append(["name","number","division","note"])
    for i in students:
        page.append([i["name"],i["number"],i["division"],i["note"]])
    page_excel.save("save password.xlsx")

for i in range(n):
    name = input("Enter name: ")
    number = int(input("Enter number student: "))
    division = input("Enter division: ").upper()
    note = float(input("Enter note: "))

    student = {
        "name": name,
        "number": number,
        "division": division,
        "note": note 
    } 
    students.append(student)

print("\nStudent list:\n")
for s in students:
    print(s)

while True:
    choix = int(input("\nDelete (1) | Add (2) | Search (3): | EXIT(0) : "))

    # DELETE
    if choix == 1:
        num = int(input("Enter number of student to delete: "))
        
        for s in students:
            if s["number"] == num:
                students.remove(s)
                print("Deleted ")
                break
        else:
            print("Student not found ")

    # ADD
    elif choix == 2:
        name = input("Enter name: ")
        number = int(input("Enter number student: "))
        division = input("Enter division: ").upper()
        note = float(input("Enter note: "))

        student = {
            "name": name,
            "number": number,
            "division": division,
            "note": note 
        } 
        students.append(student)
        print("Added ")

    # SEARCH
    elif choix == 3:
        name_search = input("Enter name to search: ")

        for s in students:
            if s["name"].lower() == name_search.lower():
                print("Found:", s)
                break
        else:
            print("Not found !!")

    #exit
    elif choix == 0:
        save_excel()
        print("good bye")
        break

    # INVALID
    else:
        print("Invalid choice !! ")

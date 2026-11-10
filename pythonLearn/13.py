students = [
    {
        "id": 101,
        "name": "Hari",
        "marks": 85
    },
    {
        "id": 102,
        "name": "Ravi",
        "marks": 55
    },
    {
        "id": 103,
        "name": "Kiran",
        "marks": 75
    }
]


def check_eligibility(marks):
    if marks >= 60:
        return "Eligible"
    else:
        return "Not Eligible"


def display_students():

    for student in students:

        print("Student ID:", student["id"])
        print("Name:", student["name"])
        print("Marks:", student["marks"])

        status = check_eligibility(student["marks"])

        print("Admission Status:", status)
        print("------------------------")


display_students()
"""
students = {
    "sadid" : "puran bazar",
    "abdullah" : "natore",
    "shadman" : "saheb bazar", 
}
for student in students:
    print(student,students[student].title(),sep=", ")

"""

students = [
    {"name" : "shadman","house": "chandpur","mobile":"0192108231"},
    {"name" : "sadid", "house": "chandppur","mobile":"091238123"},
    {"name" : "abdullah","house":"None","mobile":"010922313"},
]   

for student in students:
    print(student["name"],student["house"],student["mobile"],sep =", ")
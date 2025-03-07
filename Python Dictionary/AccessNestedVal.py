# Program to access the values of nested dictionary.
students={
    1:{'Name':'Divya','Branch':'BCA'},
    2:{'Name':'Amrutha','Branch':'BSC'},
    3:{'Name':'Prasad','Branch':'MCA'},
    4:{'Name':'Ram','Branch':'Bcom'},
    5:{'Name':'Chandu','Branch':'Btech'}
}
'''# 1.5 Accessing values from a nested dictionary
student_id=2
print(f"Student {student_id} Details: {students.get(student_id, 'Not Found')}")
print(f"Name of Student {student_id}: {students[student_id]['Name']}")
print(f"Grade of Student {student_id}: {students[student_id]['Branch']}")'''
n=int(input("Enter Roll_no"))
print("Name of student:",students[n]['Name'])
print("Branch: ",students[n]['Branch'])
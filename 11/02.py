# n = int(input())
# students = []
# for _ in range(n):
#     students.append(input())
# for i in range(n):
#     student = students[i]
#     if student[-1] == '5' or student[-1] == '4':
#         print(student)

students = []
for _ in range(int(input())):
    students.append(input())
for student in students:
    print(student)
print()
for student in students:
    if int(student[-1]) > 3:
        print(student)
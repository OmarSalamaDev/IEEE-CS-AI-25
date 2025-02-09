

n = int(input())
students = {}

for i in range(n):
    name = input()
    degree = float(input())
    students[name] = degree

unique_grades = sorted(set(students.values()))
secondLeast = unique_grades[1]

ans = sorted([
    name for name,
    grade in students.items() if grade == secondLeast])

for name in ans:
    print(name)

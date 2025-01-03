n = int(input())
students = {}

for _ in range(n):
    fn = input("Fn:")
    name = input("Name:")
    students[fn] = name

print(students)
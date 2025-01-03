grade_a = float(input())
grade_b = float(input())
grade_c = float(input())

if grade_a > 6 or grade_a < 2 or grade_b > 6 or grade_b < 2 or grade_c > 6 or grade_c < 2:
    print('Invalid grade')

else:
    avg_grade = (grade_a + grade_b + grade_c) / 3
    print(f"{avg_grade:.2f}")
    if avg_grade > 2.49:
        print('Passed')
    else:
        print('Failed')
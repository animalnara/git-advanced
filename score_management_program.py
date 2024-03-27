###2021041098 강태광###





#학생정보 입력 함수
def input_student_info():
    student_info = []
    for i in range(num_students):
        student_id = input("학번: ")

        name = input("이름: ")
        
        english_score = float(input("영어: "))
        c_score = float(input("C언어: "))
        python_score = float(input("파이썬:"))
        student_info.append({
            '학번': student_id,
            '이름': name,
            '영어': english_score,
            'C언어': c_score,
            '파이썬': python_score
        })
    return student_info


# 총점/평균 계산 함수
def calculate_total_average(students):
    for student in students:
        student['총점'] = student['영어'] + student['C언어'] + student['파이썬']
        student['평균'] = student['총점'] / 3


# 학점 계산 함수
def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    else:
        return 'F'


# 등수 계산 함수
def calculate_rank(students):
    students.sort(key=lambda x: x['총점'], reverse=True)
    for i, student in enumerate(students):
        student['학점'] = calculate_grade(student['평균'])
        student['등수'] = i + 1


# 출력 함수
def print_student_info(students):
    print("\n=========== 학번\t이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수 ===========")
    for student in students:
        print("      {학번}\t{이름}\t{영어}\t{C언어}\t{파이썬}\t{총점}\t{평균:.2f}\t{학점}\t{등수}      ".format(**student))



# 학생 수 설정
num_students = 5

# 학생 정보 입력
students_info = input_student_info()


# 총점/평균 계산
calculate_total_average(students_info)

# 등수 계산
calculate_rank(students_info)

# 결과 출력
print_student_info(students_info)
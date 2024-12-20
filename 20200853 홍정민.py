import random

def generate_students():
    """Generate a list of 30 students with random names, ages, and scores."""
    students = []
    for _ in range(30):
        name = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=2))
        age = random.randint(18, 22)
        score = random.randint(0, 100)
        students.append({"이름": name, "나이": age, "성적": score})
    return students

# Sorting algorithms
def selection_sort(students, key, reverse=False):
    n = len(students)
    for i in range(n):
        idx = i
        for j in range(i + 1, n):
            if (students[j][key] < students[idx][key]) ^ reverse:
                idx = j
        students[i], students[idx] = students[idx], students[i]
        print(f"Selection Sort Step {i+1}: {students}")

def insertion_sort(students, key, reverse=False):
    for i in range(1, len(students)):
        current = students[i]
        j = i - 1
        while j >= 0 and ((current[key] < students[j][key]) ^ reverse):
            students[j + 1] = students[j]
            j -= 1
        students[j + 1] = current
        print(f"Insertion Sort Step {i}: {students}")

def quick_sort(students, key, reverse=False):
    if len(students) <= 1:
        return students
    pivot = students[0]
    less = [student for student in students[1:] if (student[key] < pivot[key]) ^ reverse]
    greater = [student for student in students[1:] if not (student[key] < pivot[key]) ^ reverse]
    sorted_list = quick_sort(less, key, reverse) + [pivot] + quick_sort(greater, key, reverse)
    print(f"Quick Sort Step with pivot {pivot[key]}: {sorted_list}")
    return sorted_list

def radix_sort(students):
    """Radix sort only for the '성적' field."""
    max_score = max(student['성적'] for student in students)
    exp = 1
    while max_score // exp > 0:
        counting_sort(students, exp)
        print(f"Radix Sort Step for exp {exp}: {students}")
        exp *= 10

def counting_sort(students, exp):
    n = len(students)
    output = [0] * n
    count = [0] * 10

    for student in students:
        index = (student['성적'] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = (students[i]['성적'] // exp) % 10
        output[count[index] - 1] = students[i]
        count[index] -= 1

    for i in range(n):
        students[i] = output[i]

def display_students(students):
    for student in students:
        print(f"이름: {student['이름']}, 나이: {student['나이']}, 성적: {student['성적']}")

# Main program
def main():
    students = generate_students()

    while True:
        print("\n현재 학생 목록:")
        display_students(students)

        print("\n메뉴:")
        print("1. 이름을 기준으로 정렬")
        print("2. 나이를 기준으로 정렬")
        print("3. 성적을 기준으로 정렬")
        print("4. 프로그램 종료")
        choice = input("선택: ")

        if choice == '4':
            print("프로그램을 종료합니다.")
            break

        key_map = {'1': '이름', '2': '나이', '3': '성적'}
        if choice not in key_map:
            print("잘못된 입력입니다. 다시 시도하세요.")
            continue

        key = key_map[choice]
        reverse = input("오름차순(0) 또는 내림차순(1)을 선택하세요: ") == '1'

        print("정렬 알고리즘 선택:")
        print("1. 선택 정렬")
        print("2. 삽입 정렬")
        print("3. 퀵 정렬")
        print("4. 기수 정렬 (성적 기준 정렬만 가능)")
        algo_choice = input("선택: ")

        if algo_choice == '1':
            selection_sort(students, key, reverse)
        elif algo_choice == '2':
            insertion_sort(students, key, reverse)
        elif algo_choice == '3':
            students = quick_sort(students, key, reverse)
        elif algo_choice == '4' and key == '성적':
            radix_sort(students)
        else:
            print("잘못된 입력입니다. 다시 시도하세요.")
            continue

        print("\n정렬된 학생 목록:")
        display_students(students)

if __name__ == "__main__":
    main()

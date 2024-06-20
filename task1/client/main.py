import requests

BASE_URL = "http://127.0.0.1:80"

def get_students():
    response = requests.get(f"{BASE_URL}/students")
    return response.json()

def get_student(student_id):
    response = requests.get(f"{BASE_URL}/students/{student_id}")
    return response.json()

if __name__ == "__main__":
    students = get_students()
    print("Все студенты:", students)

    student_id = 1
    student = get_student(student_id)
    print(f"Студент с ID {student_id}:", student)

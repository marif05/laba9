import requests

BASE_URL = "http://127.0.0.1:80"

def add_student(student_data):
    response = requests.post(f"{BASE_URL}/students", json=student_data)
    return response.json()

if __name__ == "__main__":
    new_student = {
        "id": 4,
        "name": "Новый Студент",
        "age": 22,
        "major": "Биология"
    }
    
    result = add_student(new_student)
    print(result)

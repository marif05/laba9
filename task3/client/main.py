import requests

def update_student_info(student_id, updated_data):
    url = f"http://localhost/students/{student_id}/"
    response = requests.put(url, json=updated_data)
    return response.json()

# Пример использования функции:
student_id = 1
updated_student_data = {
    "name": "Новый Студент",
    "age": 23,
    "major": "Химия"
}

response = update_student_info(student_id, updated_student_data)
print(response)

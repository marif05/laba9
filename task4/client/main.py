import requests

def delete_student_info(student_id):
    url = f"http://localhost/students/{student_id}/"
    response = requests.delete(url)
    return response.json()

# Пример использования функции:
student_id = 1
response = delete_student_info(student_id)
print(response)

from django.test import TestCase
import requests


# Create your tests here.
response = requests.post('http://127.0.0.1:8000/v1/user_joined/447186885')
print(response.status_code)
print(response.json())
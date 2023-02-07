from django.test import TestCase
import requests


# Create your tests here.
response = requests.get('http://127.0.0.1:8000/v1/user_stats/123')
print(response.status_code)
print(response.json())
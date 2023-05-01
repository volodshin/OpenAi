import openai
from config import API_KEY


openai.api_key = f'{API_KEY}'

with open('text.txt') as f:
        txt = f.readlines()

response = openai.ChatCompletion.create(
model="gpt-3.5-turbo",
messages=[
        {"role": "user", "content": f"Напиши мені статистику по кількості слів, речень та іменованих сутностей у тексті: {txt}"}
]
)

print(str(response.choices[0].message.content))
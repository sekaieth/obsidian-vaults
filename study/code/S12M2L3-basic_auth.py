import requests

response = requests.get('https://postman-echo.com/basic-auth', auth=('postman','password'))

print(response)

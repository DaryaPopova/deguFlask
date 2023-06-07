import requests

# response = requests.get('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQYXOk_G2JCZNZvXwTtoIEGJXrqLA8LUSq0nYoj2H42XQ&s')
url = "http://worldtimeapi.org/api/timezone/Europe/Podgorica"
response = requests.get(url)
print(response)

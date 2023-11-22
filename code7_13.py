import requests
response = requests.get("https://www.python.org/downloalds/")
text = response.text
print(text)
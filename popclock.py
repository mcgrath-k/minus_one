import requests


while True:
	stat = requests.get('http://localhost:3000/').status
	print(stat, r)

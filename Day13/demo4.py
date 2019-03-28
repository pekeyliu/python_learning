import json
import requests

def get_json():
	mydict = {
		'name': 'pekey',
		'age': 30,
		'email': 'pekeyliu@126.com',
		'hobby': ['ping-pang', 'chess'],
		'cars': [
			{'brand': 'BYD', 'max-speed': 180},
			{'brand': 'Audi', 'max-speed': 280},
			{'brand': 'Benz', 'max-speed': 320}
		]
	}

	try:
		with open('./doc/data.json', 'w', encoding='utf-8') as fs:
			json.dump(mydict, fs)
	except Exception as e:
		raise e
	finally:
		pass

def main():
	resp = requests.get('http://api.tianapi.com/guonei/?key=0dab8329cb088e839e450741d40becdf&num=10')
	data_modle = json.loads(resp.text)
	for news in data_modle['newslist']:
		print(news['title'])

if __name__ == '__main__':
	main()
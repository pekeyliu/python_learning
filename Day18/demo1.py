from time import time
from threading import Thread

import requests

class DownloadHanlder(Thread):
	"""docstring for DownloadHanlder"""
	def __init__(self, url):
		super().__init__()
		self._url = url

	def run(self):
		filename = self._url[self._url.rfind('/') + 1:]
		resp = requests.get(self._url)
		file_name = './picture/' + filename
		print(file_name)
		with open(file_name, 'wb') as f:
			f.write(resp.content)

def main():
	resp = requests.get('http://api.tianapi.com/meinv/?key=0dab8329cb088e839e450741d40becdf&num=10')
	data_model = resp.json()
	for pic_info in data_model['newslist']:
		url = pic_info['picUrl']
		DownloadHanlder(url).start()

if __name__ == '__main__':
	main()
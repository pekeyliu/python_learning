from socket import socket, SOCK_STREAM, AF_INET
from base64 import b64encode
from json import dumps
from threading import Thread

def main():
	class FileTransferThread(Thread):
		"""docstring for FileTransferThread"""
		def __init__(self, cclient):
			super().__init__()
			self.cclient = cclient
			
		def run(self):
			my_dict = {}
			my_dict['filename'] = 'aaa.jpg'
			my_dict['data'] = data
			json_str = dumps(my_dict)
			self.cclient.send(json_str.encode('utf-8'))
			self.cclient.close()

	server = socket()
	server.bind(('192.168.8.100', 5659))
	server.listen(512)
	print('服务监听启动...')

	with open('./picture/aaa.jpg', 'rb') as f:
		data = b64encode(f.read()).decode('utf-8')

	while True:
		client, addr = server.accept()
		FileTransferThread(client).start()

if __name__ == '__main__':
	main()

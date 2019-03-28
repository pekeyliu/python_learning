from socket import socket
from json import loads
from base64 import b64decode

def main():
	client = socket()
	client.connect(('192.168.8.100', 5659))
	in_data = bytes()
	data = client.recv(1024)

	while data:
		in_data += data
		data = client.recv(1024)

	my_dict = loads(in_data.decode('utf-8'))
	filename = my_dict['filename']
	data = my_dict['data'].encode('utf-8')
	with open('./icon/' +filename, 'wb') as f:
		f.write(b64decode(data))
	print('图片下载成功')

if __name__ == '__main__':
	main()
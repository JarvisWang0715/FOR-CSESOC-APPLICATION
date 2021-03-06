import socket, time, re

file = input('Enter URL - ')
request = 'GET ' + file + 'HTTP/1.0\r\n\r\n'
host = file.split('/')

try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host[2], 80))
    cmd = request.encode()
    # mysock.connect(('data.pr4e.org', 80))
    # cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)

except:
    print('non-existent URL')
    quit()

while True:
    data = mysock.recv(3000)
    count = re.findall('Content-Length: ([0-9]+)', data.decode())
    print(data.decode())
    print('character count:', count[0])
    break

mysock.close()
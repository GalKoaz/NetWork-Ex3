from socket import *
import sys
serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 6789
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        print(message)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        header = "HTTP/1.1 200 OK\r\n\r\n"
        connectionSocket.send(header.encode())
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        f.close()
        connectionSocket.close()
    except IOError:
        message = "HTTP/1.1 404 Not Found\r\n\r\n"
        connectionSocket.send(message.encode())
        connectionSocket.close()
        break
serverSocket.close()
sys.exit()

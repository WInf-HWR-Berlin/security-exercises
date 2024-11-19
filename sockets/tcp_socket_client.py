import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
sock.connect(('localhost', 12001))
sock.send(
    'TEST'.encode())
rawreply = sock.recv(1024).decode() 
print(rawreply)
sock.close()
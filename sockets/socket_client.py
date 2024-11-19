import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.sendto(
    'TEST'.encode(), ('localhost', 12000))
rawreply = sock.recv(2048).decode() 
print(rawreply)
sock.close()
import socket
sock = socket.socket() 
sock.connect(('maps.google.com', 80)) 
sock.sendto(
    'GET /maps/place/PETER+PANE+Burgergrill+%26+Bar/@52.5271589,13.3681711,17z/data=!3m2!4b1!5s0x47a851966fd76a63:0x7259cc29013d8995!4m5!3m4!1s0x47a851967168e25d:0xbd2d115b4cc3a5c1!8m2!3d52.5271589!4d13.3703598'
    '&output=json&oe=utf8&sensor=false HTTP/1.1\r\n'
    'Host: maps.google.com:80\r\n'
    'User-Agent: search4.py\r\n'
    'Connection: close\r\n'
    '\r\n'.encode(), ('maps.google.com', 80))
rawreply = sock.recv(4096).decode() 
print(rawreply)

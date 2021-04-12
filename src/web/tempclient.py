import socket

def getTempTCP(TCP_IP, TCP_PORT):
    BS=1024
    data="getTemp"

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(10)
    s.connect((TCP_IP, TCP_PORT))
    s.send(data.encode())
    serverdata = s.recv(1024)
    serverdata = serverdata.decode('ascii')
    return(serverdata)

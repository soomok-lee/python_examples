'''
1. 소켓 생성
2. 접속 시도
3. 데이터 송/수신
4. 접속 종료
'''
import socket
print("1. 소켓 생성")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # tcp socket

print("2. 접속 시도")
sock.connect(("127.0.0.1", 12000))

print("3. 데이터 송/수신")
sock.sendall("Hello socket programming".encode())

print("4. 접속 종료")
sock.close()

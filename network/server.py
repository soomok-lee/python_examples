'''
1. 소켓 생성
2. 바인딩
3. 접속 대기
4. 접속 수락
5. 데이터 송/수신
6. 접속 종료
'''
import socket
print("1. 소켓 생성")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # tcp socket

print("2. 바인딩")
sock.bind(("", 12000))

print("3. 접속 대기")
sock.listen()

print("4. 접속 수락")
c_sock, addr = sock.accept()

print("5. 데이터 송/수신")
recv_data = c_sock.recv(1024)
print("수신된 데이터 : {}".format(recv_data))

print("6. 접속 종료")
c_sock.close()
sock.close()
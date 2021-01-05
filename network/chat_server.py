import socketserver

class MyHandler(socketserver.BaseRequestHandler):
    users = {}

    def send_all_messages(self, msg):
        for sock, _ in self.users.values():
            sock.send(msg.encode())

    def handle(self): # overriding
        print(self.client_address)

        while True:
            self.request.send("nickname: ".encode())
            nickname = self.request.recv(1024).decode()
            # print(nickname)
            if nickname in self.users:
                self.request.send("already exists.".encode())
            else:
                self.users[nickname] = (self.request, self.client_address)
                print("{} users.".format(len(self.users)))
                self.send_all_messages("[{}] in.".format(nickname))
                break

        while True:
            msg = self.request.recv(1024)
            if msg.decode() == "/bye":
                self.request.close()
                break
            self.send_all_messages("[{}] {}".format(nickname, msg.decode()))

        if nickname in self.users:
            del self.users[nickname]
            self.send_all_messages("[{}] out.".format(nickname))
            print("{} users.".format(len(self.users)))

class ChatServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

server = ChatServer(("", 12000), MyHandler)
server.serve_forever()
server.shutdown()
server.server_close()
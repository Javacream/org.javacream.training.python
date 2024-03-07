import socketserver

class ChatHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print(f"Accepted connection from {self.request}")
        actions = {
            "who_are_you": lambda name : f"I am the Chat server", 
            "say_hello": lambda name : f"Hi {name}, nice to meet you", 
        }
        self.request.sendall("What is your name?".encode('utf-8'))
        data = self.request.recv(1024)
        if not data:
            return  # Connection closed by the client
        name = data.decode('utf-8')
        self.request.sendall(f"Hi {name}, how can I help you?".encode('utf-8'))
        while True:
            data = self.request.recv(1024)
            if not data:
                break  # Connection closed by the client
            action_command = data.decode('utf-8')
            action = actions.get(action_command)
            if action:
                self.request.sendall(action(name).encode('utf-8'))
            else:
                self.request.sendall(f"Sorry, i did not understand {action_command}".encode('utf-8'))

class ParallelTcpServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass
if __name__ == "__main__":
    HOST = "localhost"  
    PORT = 12347

    with socketserver.ForkingTCPServer((HOST, PORT), ChatHandler) as server:
        server.serve_forever()
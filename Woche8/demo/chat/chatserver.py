import socket
import multiprocessing

def start_echo_server(host, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((host, port))
            server_socket.listen()
            print(f"Server listening on {host}:{port}")
            while True:
                client_socket, address = server_socket.accept()
                print(f"{client_socket}")
                #Sequentiell: chat(client_socket, address)
                new_process = multiprocessing.Process(target=chat, args=(client_socket, address))
                new_process.start()

def chat(client_socket, address):
    with client_socket:
        print(f"Accepted connection from {client_socket}")
        actions = {
            "who_are_you": lambda name : f"I am the Chat server", 
            "say_hello": lambda name : f"Hi {name}, nice to meet you", 
        }
        client_socket.sendall("What is your name?".encode('utf-8'))
        data = client_socket.recv(1024)
        if not data:
            return  # Connection closed by the client
        name = data.decode('utf-8')
        client_socket.sendall(f"Hi {name}, how can I help you?".encode('utf-8'))
        while True:
            data = client_socket.recv(1024)
            if not data:
                break  # Connection closed by the client
            action_command = data.decode('utf-8')
            action = actions.get(action_command)
            if action:
                client_socket.sendall(action(name).encode('utf-8'))
            else:
                client_socket.sendall(f"Sorry, i did not understand {action_command}".encode('utf-8'))

if __name__ == "__main__":
    HOST = "localhost"  
    PORT = 12346

    start_echo_server(HOST, PORT)

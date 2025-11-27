import socket
import pickle
def main():
    IP_ADDRESS = '127.0.0.1'
    PORT = 8001 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        name = input('Enter name: ')
        weight = float(input('Enter weight in kg: '))
        height = int(input('Enter height in kg: '))
        client_socket.connect((IP_ADDRESS, PORT))
        client_socket.sendall(pickle.dumps((height, weight)))
        server_response = client_socket.recv(1024).decode()
        bmi = float(server_response)
        print(f'{name} has a bmi of {bmi}')

if __name__ == '__main__':
    main()
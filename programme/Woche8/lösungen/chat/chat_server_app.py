from chat_server import ChatServer
def main():
    IP_ADDRESS = '127.0.0.1' # 'localhost' oder das Ergebnis von ipconfig (Windows) ip -A
    PORT = 12346
    server = ChatServer(IP_ADDRESS, PORT)
    server.start_up()
if __name__ == '__main__':
    main()
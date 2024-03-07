import socket

host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print(f"{host_name} = {host_ip}")

print(f"localhost = {socket.gethostbyname('localhost')}")



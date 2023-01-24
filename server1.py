import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 1700))
server_socket.listen(1)
print("server establish")
client_socket, address = server_socket.accept()
print("client connected")
client_socket.send("client connected".encode('utf-8'))
server_data = client_socket.recv(1024).decode()
print("server recv " + server_data)
if (int(server_data) % 2 == 0):
    client_socket.send("zugi".encode())
else:
    client_socket.send("ei-zugi".encode())
client_socket.close()
server_socket.close()
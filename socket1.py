import socket
def IfPositive(Num):
    Num = int(Num)
    if Num >= 0:
        return ("positive")
    else:
        return ("negative")

server_socket =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 1729))
server_socket.listen(1)
print("server is running")
client_socket, address = server_socket.accept()
client_socket.send("client connected".encode())
server_data = client_socket.recv(1024).decode()
print("server recv " + server_data)
Positive = IfPositive(server_data)
client_socket.send(str(Positive).encode())
client_socket.close()
server_socket.close()


import socket #import socket module
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 1700))
server_socket.listen(1)
client_socket, address = server_socket.accept()
client_socket.send("client connected".encode())
while True:
 server_data = client_socket.recv(1024).decode()
 print("server recv " + server_data)
 if (server_data != "byby"):
     if (int(server_data) >= 0):
         client_socket.send("positive".encode())
     elif (int(server_data) < 0):
         client_socket.send("negetive".encode())
     else:
         break

client_socket.close()
server_socket.close()


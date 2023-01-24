import socket
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(('127.0.0.1', 1700))
connection = my_socket.recv(1024).decode()
print (connection.encode('utf-8'))

client_data= input("enter num")
my_socket.send(client_data.encode())
x = my_socket.recv(1024).decode()
print(x)
my_socket.close()

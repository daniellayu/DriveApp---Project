import socket
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(('127.0.0.1', 1700))
data = my_socket.recv(1024).decode()
print(data.encode('utf-8'))
while True:
 message = input("enter num:")
 my_socket.send(message.encode())
 num= my_socket.recv(1024).decode()
 if message == "byby":
  break
 print("server send "+ num)

my_socket.close()
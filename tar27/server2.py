import multiprocessing
import socket
import threading


class Server(object):
   def __init__(self, ip, port):
       self.ip = ip
       self.port = port
       self.count = 0
       self.running=True
       self.direcory = "FILE_DIRECTORY_CLIENT"

   def start(self):
       try:
           print('server starting up on ip %s port %s' % (self.ip, self.port))
           # Create a TCP/IP socket
           sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
           sock.bind((self.ip, self.port))
           sock.listen(3)

           while True:
               print('waiting for a new client')
               clientSocket, client_address = sock.accept()
               print('new client entered')
               clientSocket.send('Hello this is server'.encode())
               self.count += 1
               print(self.count)
               # implement here your main logic
               self.handleClient(clientSocket, self.count)

       except socket.error as e:
           print(e)

   def handleClient(self, clientSock, current):
       client_handler = threading.Thread(target=self.handle_client_connection, args=(clientSock, current,))
       client_handler.start()

   def handle_client_connection(self, client_socket, current):
       while self.running:
           data = self.recv_message(client_socket)
           if not data:
               break
           #array len = 2 :  arr[0] = create  , arr[1] - file_name
           #array len = 2 :  arr[0] = read , arr[1] - file_name
           #array len = 3 :  arr[0] =write , arr[1] = text , arr[2] = filename
           #array len = 2 :  arr[0] = delete  , arr[1] - file_name
           arr = data.split(",")
           print(arr)
           if arr and len(arr) == 2 and arr[0]=="create":
               self.read(arr, client_socket)
           elif arr and len(arr) == 2 and arr[0]=="read":
               self.read(arr, client_socket)
           elif arr and len(arr) == 2 and arr[0]=="delete":
               self.delete(arr, client_socket)
           elif arr and len(arr) == 3 and arr[0]=="write":
               self.delete(arr, client_socket)
           else:
               print(arr)
               self.send_message("error message", client_socket)

   def send_message(self, data, socket):
       print("send_message" + data)
       length = str(len(data)).zfill(4)
       msg = length + data
       print("send_message"+msg)
       socket.send(msg.encode())

   def recv_message(self, socket):
       length = socket.recv(4).decode('utf-8')
       if not length:
           return None
       print(int(length))
       data = socket.recv(int(length)).decode('utf-8')
       if not data:
           return None
       print(data)
       return data

   def create(self, arr, client_socket):
       try:
           f = self.direcory + "\\" + arr[1]
           f = open(f, "w")
           f.close()
           self.send_message("file open", client_socket)
       except:
           client_socket.send("cant open".encode())

   def read(self, arr, client_socket):
       try:
           f = self.direcory + "\\" + arr[1]
           f = open(f, "r")
           data = f.read()
           f.close()
           self.send_message(data, client_socket)
       except:
           client_socket.send("cant open to read file".encode())


if __name__ == '__main__':
   ip = '127.0.0.1'
   port = 2000
   s = Server(ip, port)
   s.start()


#first
#1. recursive
#2. Node<T>
# 3. Stack<T>
# 4. Queue<T>
# 5. inheritance

# second five points
# client server socket oop
# sqlite db
# thread
# a game or db admin




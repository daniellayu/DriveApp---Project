import socket
import threading
from DriveProject.server_d.teacherdb import TeacherDb
from DriveProject.server_d.studentdb import StudentDb


class Server(object):
   def __init__(self, ip, port):
       self.ip = ip
       self.port = port
       self.count = 0
       self.running = True
       self.teacherdb = TeacherDb()
       self.studentdb = StudentDb()

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
           server_data = client_socket.recv(1024).decode('utf-8')
           if not server_data:#client disconnected
               break
           arr = server_data.split(",")
           print(arr)
           if arr and len(arr) == 9 and arr[0] == "sign_up_teacher":
               server_data = self.teacherdb.insert(arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[8])
               print("Server data: ", server_data)
               if server_data:
                   client_socket.send("success Sign up teacher".encode())
               elif server_data:
                   client_socket.send("failed Sign up teacher".encode())
           elif arr and len(arr) == 7 and arr[0] == "sign_up_student":
               server_data = self.studentdb.insert(arr[1], arr[2], arr[3], arr[4], arr[5], arr[6])
               print("Server data: ", server_data)
               if server_data:
                   client_socket.send("success Sign up student".encode())
               elif server_data:
                   client_socket.send("failed Sign up student".encode())
           elif arr and len(arr) == 3 and arr[0] == "sign_in_teacher":
               server_data = self.teacherdb.is_exist(arr[1], arr[2])
               print("Server data: ", server_data)#true or false
               if server_data:
                   client_socket.send("success Sign in".encode())
               elif server_data:
                   client_socket.send("failed Sign in".encode())
           elif arr and len(arr) == 3 and arr[0] == "sign_in_student":
               server_data = self.studentdb.is_exist(arr[1], arr[2])
               print("Server data: ", server_data)
               if server_data:
                   client_socket.send("success Sign in".encode())
               elif server_data:
                   client_socket.send("failed Sign in".encode())
           else:
               print(arr)
               self.send_message("error message", client_socket)

   def send_message(self, data, socket):
       print("send_message" + data)
       length = str(len(data)).zfill(4)
       msg = length + data
       print("send_message" + msg)
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




if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 1802
    s = Server(ip, port)
    s.start()

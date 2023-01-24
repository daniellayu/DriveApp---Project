import socket
class Client (object):
   def __init__(self, ip, port):
       self.ip = ip
       self.port = port
   def start(self):
       try:
           print('connecting to ip %s port %s' % (ip, port))
           # Create a TCP/IP socket
           sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
           sock.connect((ip, port))
           print('connected to server')
           # send receive example
           data = sock.recv(1024).decode('utf-8')
           print('received message: :', data)
           while True:
               m= self.menu()
               data = input(m)
               if(data=="screentshot"):
                   self.screentshot()

               #send message
               self.send_message(data, sock)
               #recv message
               data = self.recv_message(sock)
               if not data:
                   break
               print(data)
       except:
           print("connetion failed")
   def screen_shot(self):
       pass
       # take screen shot and send to server according to protoocl
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

   def menu(self):
       m = "1.print screenshot to take ...\n"
       m+= "2.print copy and ..........."
       return  m

ip = '127.0.0.1'
port = 2000
c =Client(ip, port)
c.start()


import socket
import threading
from restaurant import Cities
from restaurant import Restaurant

#create tcp socket object
class Server:
    def __init__(self, ip, port):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #bind to port number
        #0.0.0.0 means that the server listen to every ip
        self.server_socket.bind(('0.0.0.0', 1731))
        self.running = True
        #socket can listen only to one ip
        self.server_socket.listen(1)
        self.city = Cities()
        self.restaurant = Restaurant()
        print("waiting for user accepted")
        self.accept()
        self.ip = ip
        self.port = port
        self.count = 0
        self.running = True

    def accept(self):
        #establish connection with client
        print("accept - waiting for client")
        client_socket, address = self.server_socket.accept()
        client_socket.send("client connected".encode('utf-8'))
        while self.running:
           server_data = client_socket.recv(1024).decode('utf-8')
           #insert,restaurantType,numOfWorkers,cityId
           #delete,id
           #get_all_restaurants
           #exit
           arr = server_data.split(",")
           print(arr)
           if arr!=None and arr[0] == "insert" and len(arr) == 4:
               print("insert")
               data=self.restaurant.insert_restaurant(arr[1],arr[2],arr[3])
               data = str(data)
           elif arr!=None and arr[0] == "delete" and len(arr) == 2:
               print("delete")
               data=self.restaurant.delete_all_restaurant_by_id(arr[1])
           elif arr!=None and arr[0] == "get_all_restaurants" and len(arr) == 1:
               print("get_all_users")
               data=self.restaurant.get_all_restaurant()
               data = ",".join(data) # convert data to string
           elif arr!=None and arr[0] == "exit":
               print("exit")
               self.running = False
               data = "exit"
           else:
               data="send data according to protocol"

           client_socket.send(data.encode())
           print("server send " + data)
        #close the client connection
        client_socket.close()
        #close the server connection
        self.server_socket.close()

    #def __init__(self, ip, port):
        #self.ip = ip
        #self.port = port
        #self.count = 0
        #self.running = True

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
                self.handleClient(clientSocket)

        except socket.error as e:
            print(e)

    def handleClient(self, clientSock):
        client_handler = threading.Thread(target=self.handle_client_connection, args=(clientSock,))
        client_handler.start()

    def handle_client_connection(self, client_socket):
        while self.running:
            request = client_socket.recv(1024).decode('utf-8')
            client_socket.send(request.encode())
            print(request)


ip = '127.0.0.1'
port = 1700
s = Server(ip, port)
s.start()
import socket
class CLient:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        my_socket.connect(('127.0.0.1', 1731))
        data = my_socket.recv(1024).decode('utf-8')
        self.running = True
        print(data.encode('utf-8'))


        while self.running:
            message = input(self.message())
            my_socket.send(message.encode('utf-8'))
            client_data = my_socket.recv(1024).decode()
            if client_data == "exit":
                self.running = False

            print("server send back " + client_data)

        my_socket.close()  # close client socket
    def message(self):
        str_message = "print insert, restaurantType, numOfWorkers, cityId to insert person to db\n "
        str_message += "print delete, restaurantId\n "
        str_message += "print get_all_restaurants to  get array of users\n "
        return str_message

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
                data = input("print someting")
                sock.send(data.encode())
                data = sock.recv(1024).decode('utf-8')
                print(data)
        except:
            print("connetion failed")


ip = '127.0.0.1'
port = 1700
c = CLient(ip, port)
c.start()


import socket
from PIL import Image
import pyautogui
import io
from tcp_by_size import recv_by_size
from tcp_by_size import send_with_size
import glob



class Client():
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip = '127.0.0.1'
        self.port = 6060
        self.counter = 0
        self.client.connect((self.ip, self.port))
        self.running = True
        self.start()



    def start(self):
        try:
            data = self.client.recv(1024).decode('utf-8')
            print('received message:', data)
            while self.running:
                message = input(self.menu())
                if (message == "1"):
                    self.screenshot()
                elif (message == "2"):
                    self.sendfile(self.client)
                elif (message == "3"):
                    self.directory_files(self.client)
                elif (message == "4"):
                    self.delete_file(self.client)
                elif (message == "5"):
                    self.copy_file(self.client)
                elif (message == "6"):
                    self.run_program(self.client)
                elif message == "7":
                    self.exit(self.client)
        except:
            print("Connection failed")



    def menu(self):
        str = "Print 1 to take a screenshoot\n"
        str += "Print 2 to send a file\n"
        str += "Print 3 to read a file\n"
        str += "Print 4 to delete a file\n"
        str += "Print 5 to copy a file\n"
        str += "Print 6 to run a program\n"
        str += "Print 7 to reconect from client\n"
        return str


    def screenshot(self):
        send_with_size(self.client, "screenshot")

    def sendfile(self, client_socket):
        send_with_size(self.client, "sendfile")
        path = input("print path of file")
        send_with_size(client_socket, path)
        data = recv_by_size(client_socket, path)
        print(data)

    def directory_files(self, client_socket):
        send_with_size(self.client, "directory")
        name_file = input("print name of file")
        send_with_size(client_socket, name_file)
        data = recv_by_size(client_socket, name_file)
        print(data)

    def delete_file(self, client_socket):
        send_with_size(self.client, "deletefile")
        name_file = input("print name of file")
        send_with_size(client_socket, name_file)

    def copy_file(self, client_socket):
        send_with_size(self.client, "copyfile")
        name_file = input("print name of file")
        send_with_size(client_socket, name_file)
        target = input("print name of file")
        send_with_size(client_socket, target)

    def run_program(self, client_socket):
        send_with_size(self.client, "runprogram")
        program = input("print name of program")
        send_with_size(client_socket, program)

    def exit(self, client_socket):
        #send_with_size(self.client, "exit")
        print("finish program")
        self.running = False

c = Client()













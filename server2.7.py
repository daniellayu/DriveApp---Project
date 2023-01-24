import glob
import socket
import os
import threading
import pyautogui
from PIL import Image
import io
from tcp_by_size import recv_by_size
from tcp_by_size import send_with_size
import shutil
import subprocess


class Server:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip = '0.0.0.0'
        self.port = 6060
        self.running = True
        self.counter = 0
        self.server.bind((self.ip, self.port))
        self.server.listen()
        self.start()

    def start(self):
        try:
            print('waiting for a new client')
            client_socket, address = self.server.accept()
            print('new client entered')
            client_socket.send("client connected".encode('utf-8'))
            while self.running:
                command = recv_by_size(client_socket, "string")
                if (command == "screenshot"):
                    self.take_screenshot()
                elif command == "sendfile":
                     self.send_file(client_socket)
                elif command == "directory":
                     self.send_directory(client_socket)
                elif command == "deletefile":
                     self.delete_file(client_socket)
                elif command == "copyfile":
                     self.copy_file(client_socket)
                elif command == "runprogram":
                    self.run_program(client_socket)
                elif command == "exit":
                    self.exit(client_socket)
        except socket.error as e:
            print(e)


    def take_screenshot(self):
        image = pyautogui.screenshot()
        image.save('C:\screenshots\pic2.png')


    def send_file(self, client_socket):
        path = recv_by_size(client_socket, "string")
        file = open(path, "rb")
        content = file.read()
        send_with_size(client_socket, content)

    def send_directory(self, client_socket):
        name_file = recv_by_size(client_socket, "string")
        files_list = os.listdir(name_file)
        str_dir_list = " ".join(files_list)
        send_with_size(client_socket, str_dir_list)

    def delete_file(self, client_socket):
        name_file = recv_by_size(client_socket, "string")
        if os.path.exists(name_file):
            os.remove(name_file)
            print("file deleted successfully")
        else:
            print("The file does not exist")

    def copy_file(self, client_socket):
        name_file = recv_by_size(client_socket, "string")
        target = recv_by_size(client_socket, "string")
        shutil(name_file, target)

    def run_program(self, client_socket):
        program = recv_by_size(client_socket, "string")
        subprocess.call(program)

    def exit(self, client_socket):
        self.running = False
        client_socket.close()



s = Server()




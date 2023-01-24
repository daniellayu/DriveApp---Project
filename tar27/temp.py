





#def send(self, func, data):  # func == scrn; data = artur
    #    x = func + ',' + data  # scrn,artur
    #    length = str(len(x)).zfill(4)  #0010
    #    msg = length + x  # 0010-scrn,artur
    #    self.client.send(msg.encode())



    #def take_photo(self):
    #    screenshot = pyautogui.screenshot()
    #    image_bytes = screenshot.tobytes()
    #    return image_bytes

    #def send_photo(self, func, data, name_file):
    #    x = bytes(func.encode()) + bytes(','.encode()) + bytes(name_file.encode()) + data  # 0000026234scrn,name,artur
    #    length = bytes(len(x)).zfill(16)  # 0010
    #    msg = length + x  # 0010-scrn,artur
    #    self.client.send(msg)

    #def recieve(self):
    #    length = int(self.client.recv(4).decode())  #0010
    #    msg = self.client.recv(length).decode()  # scrn,artur
    #    return msg


import shutil

original = r''
target = r''

shutil.copyfile(original, target)
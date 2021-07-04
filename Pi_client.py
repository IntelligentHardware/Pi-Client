import socket
import os,sys
import time
from cv2 import cv2
os.chdir(os.path.dirname(sys.argv[0]))

server_ip = ('127.0.0.1', 9000)

def ACK(Pi_socket):  #接收服务器的反馈

    data = Pi_socket.recv(1024).decode('utf-8')
    if data == 'ACK':
        return True
    else:
        return False
'''
def get_string():  #获取数据字符串 假设格式为'AAA:BBB:CCC'
    return 'AAA:BBB:CCC:DDD:SAMURAI' 
'''
def data_upload(data):  #数据上传

    Pi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Pi_socket.connect(server_ip)

    Pi_socket.send('data'.encode('utf-8'))
    
    if ACK(Pi_socket):  #开始数据上传
        print('data上传中')
        Pi_socket.send(data.encode('utf-8'))
        print('data上传完成')
        Pi_socket.close()
    return
'''
def image_upload(file_name):  #图像上传
    
    Pi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Pi_socket.connect(server_ip)
    Pi_socket.send('image'.encode('utf-8'))
    
    if ACK(Pi_socket):  #开始image上传
        print('image上传中')
        with open(file_name, 'rb') as image:
            image_data = image.read()

        length = len(image_data)
        arr = bytearray(length.to_bytes(4, byteorder = 'big')) + image_data
        Pi_socket.sendall(arr)
        print('image上传完成')
        Pi_socket.close()
    return
'''
def image_upload(image_data, direction):  #图像上传:包含图像数据，物品方向，1为放入，0为放出
    
    Pi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Pi_socket.connect(server_ip)
    Pi_socket.send('image'.encode('utf-8'))
    
    if ACK(Pi_socket):  #开始image上传
        print('image上传中')
        cv2.imwrite('test.jpg', image_data)
        with open('test.jpg', 'rb') as image:
            image_data = image.read()
        length = len(image_data)
        arr = bytearray(length.to_bytes(4, byteorder = 'big')) + bytearray(direction.to_bytes(1, byteorder = 'big')) + image_data
        Pi_socket.sendall(arr)
        print('image上传完成')
        Pi_socket.close()
    return

def main():
    
    while True:
        data_upload()
        image_upload('test.jpg', 1)
        time.sleep(5)
    Pi_socket.close()
'''
    while True:
        Pi_socket.send(input('>').encode('utf-8'))
'''

if __name__ == '__main__':
    main()

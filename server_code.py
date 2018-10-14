import socket
import random

def Main():
        # host ip and port number
        host = '192.168.0.25'
        port = 5003
        
        # socket object
        socketObj = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        socketObj.bind((host, port))
        print("Server started")
        while True:
                # Generate random number in the range of 0 to 10
                rand = random.randint(0, 10)
                print("Random num is: " + str(rand))
                data, addr = socketObj.recvfrom(1024)
                data = data.decode('utf-8')
                print("message from: " + str(addr))
                print("from connected user: "+ str(data))
                data = data.upper()
                # If rand is less is than 3, we consider the packet lost and do not respond
                if rand < 3:
                        print("packet lost...")
                        continue
                print("sending: "+ data )
                socketObj.sendto(data.encode('utf-8'), addr)
        socketObj.close

if __name__ == '__main__':
        Main()

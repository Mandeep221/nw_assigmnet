import socket

def Main():
        host = '127.0.0.1'
        port = 5002

        server = ('127.0.0.1', 5003)

        socketObj = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # socketObj.bind((host, port))
        socketObj.settimeout(2.0)
        sequence_number = 1 #variable to keep track of the sequence number
        message = input("-> ")
        while message != 'q':
                try:
                        socketObj.sendto(message.encode('utf-8'), server)
                        data, addr = socketObj.recvfrom(1024)
                        data = data.decode('utf-8')
                        print("Received from server: "+ data)
                        message = input("-> ")
                except socket.timeout:
                        print("Socket timed out")
                        continue
        socketObj.close()
if __name__ == "__main__":
        Main()

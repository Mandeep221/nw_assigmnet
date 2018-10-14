import socket
import time

def Main():
        host = '192.168.0.36'
        port = 5002

        server = ('192.168.0.25', 5003)

        socketObj = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        socketObj.settimeout(2.0) #socket times out after 2 seconds
        sequence_number = 1 #variable to keep track of the sequence number
        while sequence_number <= 10:
                message = 'Ping' #message to send
                start = time.time() #assigns the current time to a variable
                message = message + ' '+str(sequence_number) + ' '+str(start) #required message format
                socketObj.sendto(message.encode('utf-8'), server)
                
                try:
                        message, addr = socketObj.recvfrom(1024)
                        elapsed = (time.time()-start) 
                        print('Seq num is: '+str(sequence_number))
                        print('Received from server 192.168.0.25: '+ message.decode('utf-8'))
                        print('Round Trip Time is:' + str(elapsed) + ' seconds')
                except socket.timeout:
                        print('Seq num is: '+str(sequence_number))
                        print('Request timed out')
                sequence_number+=1
                if sequence_number > 10:
                        socketObj.close()
if __name__ == "__main__":
        Main()

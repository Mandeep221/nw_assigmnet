import socket
import time
import numpy as np
import plotly.plotly as py
import plotly.tools as tls
import matplotlib.pyplot as plt

def Main():
        host = '192.168.0.36'
        port = 5002

        server = ('192.168.0.25', 5003)
        numOfPings = 200
        rttArray=[] # array to hold all the RTT values
        socketObj = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        socketObj.settimeout(2.0)
        sequence_number = 1 #variable to keep track of the sequence number
        while sequence_number <= numOfPings:
                message = 'Ping' #message to send
                start = time.time() #assigns the current time to a variable
                message = message + ' '+str(sequence_number) + ' '+str(start)
                socketObj.sendto(message.encode('utf-8'), server)
                try:
                        message, addr = socketObj.recvfrom(1024)
                        elapsed = (time.time()-start) 
                        rttArray.append(elapsed)
                except socket.timeout:
                        print('Request timed out for seq no. '+str(sequence_number))

                sequence_number+=1
                if sequence_number > numOfPings:
                        socketObj.close()

        # Calculating Min, Max, Average and Standard deviation using numpy
        print("Min RTT is: "+ str(min(rttArray)))
        print("Max RTT is: "+ str(max(rttArray)))
        print("Average RTT is: "+ str(np.average(rttArray)))
        print("Standard deviation is: "+ str(np.std(rttArray)))
        
        # Calculating packet loss rate
        packetsLost = numOfPings - len(rttArray)
        print("No. of Packets lost: "+ str(packetsLost))
        print("No. of Packets delivered: "+ str(numOfPings - packetsLost))
        packetsLostRate = (packetsLost/numOfPings) * 100
        print("Packet loss rate: "+ str(packetsLostRate)+'%')

        # plot histogram,  display bin values and count in each bin
        x = np.array(rttArray)
        counts, bin_edges = np.histogram(x, bins=5)
        print('Bin edges: '+str(bin_edges))
        print('Count in each bin: '+str(counts))
        plt.hist(x, bins=20)
        plt.show()
if __name__ == "__main__":
        Main()

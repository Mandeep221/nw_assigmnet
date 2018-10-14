import socket
import sys

# Set up a TCP/IP socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# get ip address
host = sys.argv[1]

# get port
port = int(sys.argv[2])

# get file to be fetched from server
fileName = sys.argv[3]
print("Ip Address: " + str(host))
print("Port number: "+ str(port))
s.connect((host,port))

print("\nconnection established\n")
# Protocol exchange - sends and receives
req = "GET /"+ fileName +" HTTP/1.0\n\n"
s.send(req.encode('utf-8'))
resp = s.recv(1024)
print("\n====== Server Response ======\n\n")
print(resp)

s.close()
print("\ndone")
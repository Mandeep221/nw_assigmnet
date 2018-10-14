from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
import threading

class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "File Not Found"
            self.send_response(404)
        self.end_headers()

        #Info of the new thread started
        thread_info = " New thread started: "+ str(threading.currentThread().getName())

        #message
        message = str(thread_info)+ "\n Contents of the file requested: \n\n"

        # Print Thread number and Message
        self.wfile.write(message.encode('utf-8') )
        # Print Contents of the file
        self.wfile.write(bytes(file_to_open,'utf-8'))
        return

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""

if __name__ == '__main__':
    server = ThreadedHTTPServer(('localhost', 8080), Serv)
    print('Starting server...')
    server.serve_forever()
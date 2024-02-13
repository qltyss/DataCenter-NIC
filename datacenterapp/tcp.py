import socket
import threading

class TCPHandler:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.running = True
        threading.Thread(target=self.listen_to_tcp, args=()).start()

    def listen_to_tcp(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #     sock.settimeout(10)
        sock.connect((self.host, self.port))
        try:        
                # sock.send(packet)
                # sleep(1)
                
                # this is the problem here
                # while True:
                reply = sock.recv(1024)
                print(reply.decode("UTF-8"))
                new_reply = reply.decode("UTF-8")
                print ("recvd:", reply.decode("UTF-8"))
                # sock.close()
        except KeyboardInterrupt:
                print ("bye")
        return new_reply

    def stop(self):
        self.running = False

# To start listening to TCP, create a TCPHandler instance
tcp_handler = TCPHandler('192.168.100.219',5555)  # Example host and port

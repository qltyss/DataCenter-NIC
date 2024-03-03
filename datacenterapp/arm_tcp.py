import socket
from .constants import * 
from time import sleep
def arm(command):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip, port))  # Try to connect to the server
            s.sendall(command.encode())  # Send command to the Lua script
            response = s.recv(1024).decode()  # Receive response from Lua script
            print(response)
            
            return response
    except socket.error as e:
        print(f"Error: {e}")
        return "Not Connected"  # Return "Not Connected" if any socket error occurs

def control_arm(command):
    print("here")
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip, 29999))
            sleep(1)
            s.sendall(command.encode())
            return 'Started'
    except socket.error as e:
        # logging.error(f"Socket error: {e}")
        
        return "Not Connected"
    

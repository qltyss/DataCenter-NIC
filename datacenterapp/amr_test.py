import socket

# ip = "192.168.1.6"
# port = 6001
# ip = '192.168.100.32'
ip = '192.168.100.219'
port = 10000
def amr_test(command):
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

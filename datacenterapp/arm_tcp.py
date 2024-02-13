import socket

# ip = "192.168.100.243"
# port = 6001
ip = "192.168.100.219"
port = 5555
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
# arm("unlock")
# send("HR2")
# send("LM3")
# send_command("A")
# send_command("B")
# # Loop to continuously get input and send it
# while True:
#     Grip = input("Enter the grip value (or type 'exit' to quit): ").upper()
    
#     if Grip == 'EXIT':
#         break
    
#     send_command(Grip)
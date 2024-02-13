# def check_tcp_value():
#     global tcp_value, yolo_enabled
#     while True:
#         try:
#             print("Listening for TCP value...")  # Debug print
#             tcp_value = tcp_handler.listen_to_tcp()
#             print(f"New TCP Value: {tcp_value}")  # Debug print
#             if tcp_value == '5':
#                 print("Yolo is now enabled")  # Debug print
#                 yolo_enabled = True
                
#             # else:
#             #     yolo_enabled = False
#         except ConnectionResetError:
#             print("Connection was closed by the remote host. Trying to reconnect...")
#             time.sleep(3)
#         except Exception as e:
#             print(f"An unexpected error occurred: {e}")
#             time.sleep(3)  # Sleep and retry for any exception

# Make sure to call tcp_check_thread.start() in the appropriate place, e.g. in the view that starts the stream or in the app's initialization phase.



# # Start the TCP checking thread
# tcp_check_thread = threading.Thread(target=check_tcp_value, daemon=True)
# tcp_check_thread.start()
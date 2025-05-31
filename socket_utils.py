import socket
import sys

def create_socket_connection(address, port):
    """Create and connect socket with proper error handling"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((address, port))
        print(f"Connected to server at {address}:{port}")
        return s
    except socket.error as err:
        print(f"Connection failed: {err}")
        sys.exit(1)

def send_dslp_message(sock, protocol, peer, data):
    """Send message using DSLP protocol"""
    try:
        sock.sendall(f"{protocol}\r\n".encode())
        sock.sendall(f"peer notify\r\n".encode())
        sock.sendall(f"{peer}\r\n".encode())
        sock.sendall(data)
        sock.sendall(b"dslp/end\r\n")
    except socket.error as err:
        print(f"Message sending failed: {err}")
        sys.exit(1)

def receive_dslp_message(sock):
    """Receive complete DSLP message"""
    buffer = b""
    while True:
        chunk = sock.recv(4096)
        if not chunk:
            break
        buffer += chunk
        if buffer.endswith(b"dslp/end\r\n"):
            break
    return buffer

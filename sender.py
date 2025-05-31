import sys
import base64
import socket_utils

def main():
    if len(sys.argv) < 3:
        print("Usage: python sender.py <peer> <file_path>")
        sys.exit(1)
        
    peer = sys.argv[1]
    file_path = sys.argv[2]
    address = "dbl44.beuth-hochschule.de"
    port = 44444
    
    try:
        # Read and encode file
        with open(file_path, 'rb') as f:
            file_data = f.read()
        encoded_data = base64.b64encode(file_data)
        
        # Connect and send
        s = socket_utils.create_socket_connection(address, port)
        socket_utils.send_dslp_message(s, "dslp/1.2", peer, encoded_data)
        print(f"File {file_path} sent successfully to peer {peer}")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 's' in locals():
            s.close()

if __name__ == "__main__":
    main()

import sys
import socket_utils

def main():
    if len(sys.argv) < 2:
        print("Usage: python receiver.py <output_file>")
        sys.exit(1)
        
    output_file = sys.argv[1]
    address = "dbl44.beuth-hochschule.de"
    port = 44444
    
    try:
        s = socket_utils.create_socket_connection(address, port)
        data = socket_utils.receive_dslp_message(s)
        
        # Write received data to file
        with open(output_file, 'wb') as f:
            f.write(data)
        print(f"Received data saved to {output_file}")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 's' in locals():
            s.close()

if __name__ == "__main__":
    main()

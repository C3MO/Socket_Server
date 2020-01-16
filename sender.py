import sys
import socket
import base64
import os

args = sys.argv

#args = ['', '']
#args[0] = "141.64.174.92"
#args[1] = "text.txt"

def sendMessage(message, protocol):
    '''Send Message with given protocol (str)'''
    s.send(str.encode(protocol + "\r\n"))
    s.send(str.encode("peer notify\r\n"))
    s.send(str.encode(sys.argv[1] + "\r\n"))
    s.send(str.encode(bytes.decode(message) + "\r\n"))
    s.send(str.encode("dslp/end\r\n"))

if len(args) < 3:
    print("Please set two command line arguments!")
else:

    adress = "dbl44.beuth-hochschule.de"
    port = 44444
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((adress, port))
        print("Connect to server!")
    except:
        print("Can't connect to server!")
        s.close()
        SystemExit()

    file = args[2]
    if os.path.exists(file):
  
        file = open(file, 'rb') 
        file = file.read()
        file_encode = base64.encodebytes(file)
        print(file_encode)
        
        sendMessage(file_encode, "dslp/1.2")
        print("Send file!")
        
        s.close()
        SystemExit()
    else:
        print("Path does not exist!")
s.close()
SystemExit()

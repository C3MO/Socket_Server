import sys
import socket

args = sys.argv


args = ['']
args[0] = "retext.txt"

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
#receive message via dslp1.2
data = s.recv(1024)
print(bytes.decode(data))


s.close()
SystemExit()
import threading
import json
from socket import *

clientSocket = socket(AF_INET, SOCK_STREAM)
print("Now connecting to server...\n")   
try:
    clientSocket.connect(("localhost", 12000))
    print("Connection successfull!")
except error as e:
    print(f"Failed to connect! {e}")
    clientSocket.close()
    exit(1)

def endcase(socket):
    construct = {
        "command":"exit",
        "num1":"null",
        "num2":"null"
        }
    msg = json.dumps(construct)
    socket.send(msg.encode())
    print("Exiting Client")
    socket.shutdown(SHUT_RDWR)
    socket.close()
    
def sendMsg(socket):
    request = input("Enter request: ")
    request = request.split(" ")
    if request[0].lower()=="exit":
        endcase(socket)
        return False
    if len(request) not in (1, 3):
        construct = {
            "command":"bad input",
            "num1":"null",
            "num2":"null"
        }
    elif len(request)==1:
        construct = {
            "command":request[0],
            "num1":"null",
            "num2":"null"
            }
    elif len(request)==3:
        construct = {
            "command":request[0],
            "num1":int(request[1]),
            "num2":int(request[2])
            }
    msg = json.dumps(construct)
    socket.send(msg.encode())
    return True

def receiveMsg(socket):
    response = socket.recv(1024).decode()
    print(f"Response from server: {response}")
    return  

def clientService(socket):
    while True:
        try:
            receiveMsg(socket)
            if not sendMsg(socket):
                break
        except error as e:
            print(f"Connection lost: {e}")
            break

threading.Thread(target=clientService, args=(clientSocket,)).start()

"""
def service(socket):
    while True:
        try:
            threading.Thread(target=receiveMsg, args=(socket,)).start()
            if not threading.Thread(target=sendMsg, args=(socket,)).start():     # Does not work, always returns False
                break
        except error as e:
            print(f"Connection lost: {e}")
            break
    

service(clientSocket)
"""
    
"""
try:
    clientSocket.connect(("localhost", 12000))
    print("connection success")
except error as e:
    print(f"connection failed: {e}")
    clientSocket.close()
    exit(1)

def service(socket):
    While True:
        request = input("Enter request: ")
        socket.send(request.encode())
        response = socket.recv(1024).decode()
        print(f"Response from server: {response}")
        if request.lower()=="exit":
            print("Exiting client")
        socket.close()


thread.Treading(target=service, args=(clientSocket)).start()

"""
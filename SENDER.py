# This file is used for sending the file over socket
import os
import socket
import time
#from security import encrypt
# Creating a socket.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#client = None
try:
    sock.bind((socket.gethostname(), 22222))
    sock.listen(5)
    # Accepting the connection.
    (clientConn, clientAddr) = sock.accept()
    print("Host Name: ", sock.getsockname())
except Exception as ex:
    print("Exception in bind/listen: ", ex)

# Getting file details.
file_name = input("File Name: ")
length = len(file_name)
fnameBuff = file_name
#fnameBuff += 'b' * (100 - length)
file_size = os.path.getsize(file_name)
print(file_size, 'bytes')
# Sending file_name and size details.

fsizeBuff = str(file_size)
length = len(fsizeBuff)
#fsizeBuff += '\0' * (100 - length)

clientConn.send(str(fnameBuff).encode())
clientConn.send(str(fsizeBuff).encode())

# Opening file and sending data.
with open(file_name, "rb") as file:
    c = 0
    # Starting the time capture.
    start_time = time.time()

    # Running loop while c != file_size.
    while c <= file_size:
        data = file.read(1024)
        if not (data):
            break
        #enc_data = encrypt(data)
        clientConn.sendall(data)
        c += len(data)

    # Ending the time capture.
    end_time = time.time()

print("File Transfer complete. Total time: ", end_time - start_time, 'seconds.')
# Closing the socket.
sock.close()

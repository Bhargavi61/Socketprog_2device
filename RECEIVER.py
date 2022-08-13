# This file will be used for receiving files over socket connection.
import os
import socket
import time
import base64
#def getValidStr():
    
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.1.42'
# Trying to connect to socket.
try:
    sock.connect((host, 22222))
    print("Connected Successfully!")
except Exception as ex:
    print("Unable to connect: ", ex)
    print(host)
# Send file details.
file_name = sock.recv(100).decode()
file_size = sock.recv(100).decode()

#file_name = getValidStr(fnameBuff)
#file_size = getValidStr(fsizeBuff)

# Opening and reading file.
with open("./" + file_name, "wb") as file:
    c = 0
    # Starting the time capture.
    start_time = time.time()

    # Running the loop while file is being received.
    while c <= int(file_size[:2]):
        data = sock.recv(1024)
        if not (data):
            break
        print(data)
        
        #base64_string = data
        #base64_bytes = base64_string.encode("ascii")
        
        #sample_string_bytes = base64.b64decode(data)
        #sample_string = sample_string_bytes.decode("ascii")
        #print(sample_string_bytes)
        #print(f"Decoded string: {sample_string}")
        
        file.write(data)
        c += len(data)

    # Ending the time capture.
    end_time = time.time()

print("File transfer complete. Total time: ", end_time - start_time, 'seconds.')

# Closing the socket.
sock.close()
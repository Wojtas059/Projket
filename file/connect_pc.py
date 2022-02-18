import socket
import threading

import file.mygrid as my

HEADER = 64
PORT = 5000
dis = "!disconnect"
Format = "utf-8"
SERVER = "raspberrypi"
ADDR = (SERVER, PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
def handler(conn, addr):
    print("new connection{}".format(addr))
    connected = True
    connect_class = my.Connect()
    while connected:
            msg_length = conn.recv(HEADER).decode(Format)
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(Format)
                if msg == "START STM32":
                    print("start")
                    connect_class.start()
                if msg =="STOP STM32":
                    print("stop")
                    connect_class.stop()
                print("{}: {}".format(addr, msg))
                if msg == dis:
                    connected = False
                    thread_stm32.join()
            conn.send("msg received".encode(Format))
    conn.close()
def client():
    import subprocess
    subprocess.run("python3 client.py",shell = True)
def start():
    server.listen()
    while True:
        conn,addr = server.accept()
        thread = threading.Thread(target=handler, args=(conn, addr))
        thread.start()
        print(f"[Active Connections]{threading.activeCount() - 1}")
print("server up and running....")
print("server {} listening at port {}".format(SERVER, PORT))
start()
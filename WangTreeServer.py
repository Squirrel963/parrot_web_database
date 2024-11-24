import os
import socket
import threading
 
 
def create_server_socket(host, port):
    socket_server = socket.socket()
    socket_server.bind((host, port))
    socket_server.listen(5)
    print(f"服务端已启动，地址{host}，端口{port}")
    # 开启多线程，收发来自多个客户端的数据
    while True:
        conn, address = socket_server.accept()
        print(f"服务端已接受到客户端{address}的连接请求")
        client_handler = threading.Thread(target=handle_client, args=(conn, address))
        client_handler.start()
 
 
# 处理收发数据
def handle_client(conn, address):
    while True:
        # 接收客户端发来的数据
        data_from_client: str = conn.recv(4096).decode("UTF-8")
        print(f"客户端{address}发送数据：{data_from_client}")
        # 发送消息到客户端
        data = data_from_client.split(";")
        if data_from_client == 'outlog':
            break
        elif data[0] == "cmd":
            tback = os.popen(data[1])
            msg = tback.read()
        elif data[0] == "login":
            print(data)
            if data[1] == "1145":
                msg = "logined!"
            else:
                msg = "no"
        else:
            msg = "none"
        conn.send(msg.encode("UTF-8"))  # encode将字符串编码为字节数组对象
    conn.close()
 
 
if __name__ == '__main__':
    server_host = "127.0.0.1"
    server_port = 20
    create_server_socket(server_host, server_port)
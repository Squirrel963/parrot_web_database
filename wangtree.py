print("正在载入需要库...")
import socket
import sys
import time
import os
socket_client = socket.socket()
version = 1.1
it_version = 10001
Nolog = "localhost"
login_name = Nolog
ip = socket.gethostbyname(socket.gethostname())
logined = False
rebacked = False

server_command = ["cmd","login"]

def restart():
  python = sys.executable
  os.execl(python, python, * sys.argv)

def run_commands(head,volue):
    global rebacked,socket_client,login_name,logined
    print(f"-运行{command} :")
    com_msg = head + ";" + volue
    if head == "ser":
        connect_server(volue)
    elif head == "outlog":
        if not volue == "c":
            appl = input("[ 警告 ] 命令'outlog'后添加了参数'c'，这会使终端强制与服务器断开连接(无断连请求数据包)！你确定吗？ [y/n] ")
            if appl == "y":
                restart()
        else:
            print("尝试断开连接中...  终端将重启以刷新缓存")
            socket_client.send("outlog".encode("UTF-8"))
            restart()
    elif head in server_command:
        try:
            socket_client.send(com_msg.encode("UTF-8"))
            rebacked = True
        except:
            print("[ 警告 ] 远程命令发送失败，请检查设备可用性")

def connect_server(server_ip):
    global login_name,logined
    server = server_ip.split(" ")
    if logined:
        print("[ 注意 ] 你已连接到一个服务器，请使用'outlog'断开之前的连接")
    else:
        if len(server) >= 3:
            try:
                print("解析命令中...")
                s_ip = server[0]
                #print(s_ip)
                s_port = int(server[1])
                #print(s_port)
                print("尝试连接服务器中...")
                socket_client.connect((s_ip, s_port))
                login_name = s_ip
                logined = True
                print(f"连接成功，连接为{login_name}")
            except:
                print("[ 错误 ] 服务器连接失败")
        else:
            print("[ 警告 ] 非有效服务器地址")

print("\033[F-----------------------              ")
print(f"王果树终端 v{version}")
print(f"当前设备IP(socket)：{ip}")
print(f"通信版本：{it_version}")
print("-----------------------")

while True:
    command = input(f"{login_name} >>")
    if command == "":
        continue
    else:
        command_li = command.split(" ")
        command_volue = ""
        i = 0
        for command_ in command_li:
            if i != 0:
                if i == len(command_li):
                    command_volue += command_
                else:
                    command_volue += (command_ + " ")
            i += 1
        if len(command_li) == 1:
            command_volue = "none"
        #print("li",command_li[0])
        #print("volue",command_volue)
        if command_li[0] == "exit":
                sys.exit(0)
        try:
            reback = ""
            run_commands(command_li[0],command_volue)
            if rebacked:
                    reback = socket_client.recv(8192).decode("UTF-8")
            print(reback)
        except:
            print("[ 警告 ] 发生未知错误")
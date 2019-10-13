client_ip = ""
server_addr = ""
add_ports = []

# Read config file
cfg = open("yhjm.cfg", "r")
for line in cfg.readlines():
    if line.find("S:")!= -1:
        server_addr = line[2:-1]
    if line.find("C:")!=-1:
        client_ip = line[2:-1]
    if line.find("P:")!= -1:
        add_ports.append(int(line[2:]))

print("Server IP: " + server_addr)
print("Client IP: " + client_ip)
print("Additional Ports: ")
for p in add_ports:
    print(p)

# Enter the port range below as a multiple of 1000
max_port = 30000

# Set the base port for the tcp and kcp protocol
tcp_base_port = 42760
kcp_base_port = 43760

# Number of instance, each instance for 1000 ports
noi = int(max_port / 1000)

def write_port_config(file, port):
    file.write("[port" + str(port) + "]\n")
    file.write("type = tcp\n")
    file.write("local_ip = " + client_ip + "\n")
    file.write("local_port = " + str(port) + "\n")
    file.write("remote_port = " + str(port) + "\n")
    file.write("\n")

def create_client_ini(index, start_port, end_port):
    config_file = open("frpc" + str(index) + ".ini", "w+")

    config_file.write("[common]\n")
    config_file.write("server_addr = " + server_addr + "\n")
    config_file.write("server_port = " + str(kcp_base_port + index) + "\n")
    config_file.write("protocol = kcp \n")
    config_file.write("\n")

    for i in range(start_port, end_port):
        write_port_config(config_file, i)
    config_file.close()

if __name__ == "__main__":
    for i in range(noi):
        create_client_ini(i, i * 1000 + 1, i * 1000 + 1001)

    append_file = open("frpc" + str(noi - 1) + ".ini", "a+")
    for port in add_ports:
        write_port_config(append_file, port)
    append_file.close()

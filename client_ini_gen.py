# Enter the port range below as a multiple of 1000
max_port = 10000

# Set the base port for the tcp and kcp protocol
tcp_base_port = 42760
kcp_base_port = 43760

# Number of instance, each instance for 1000 ports
noi = int(max_port / 1000)

client_ip = "192.168.1.105"
server_addr = "18.139.221.235"

def create_client_ini(index, start_port, end_port):
	config_file = open("frpc" + str(index) + ".ini", "w+")

	config_file.write("[common]\n")
	config_file.write("server_addr = " + server_addr + "\n")
	config_file.write("server_port = " + str(kcp_base_port + index) + "\n")
	config_file.write("protocol = kcp \n")
	config_file.write("\n")

	for i in range(start_port, end_port):
		config_file.write("[port" + str(i) + "]\n")
		config_file.write("type = tcp\n")
		config_file.write("local_ip = " + client_ip + "\n")
		config_file.write("local_port = " + str(i) + "\n")
		config_file.write("remote_port = " + str(i) + "\n")
		config_file.write("\n")

for i in range(noi):
	create_client_ini(i, noi * 1000 + 1, noi * 1000 + 1001)

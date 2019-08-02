filename = "frpc_all.ini"
client_ip = "192.168.1.105"
server_addr = "18.139.221.235"
server_port = 32767
start_port = 1
end_port = 1000

config_file = open(filename, "w+")

config_file.write("[common]\n")
config_file.write("server_addr = " + server_addr + "\n")
config_file.write("server_port = " + str(server_port) + "\n")
config_file.write("\n")

for i in range(start_port, end_port):
	config_file.write("[port" + str(i) + "]\n")
	config_file.write("type = tcp\n")
	config_file.write("local_ip = " + client_ip + "\n")
	config_file.write("local_port = " + str(i) + "\n")
	config_file.write("remote_port = " + str(i) + "\n")
	config_file.write("\n")

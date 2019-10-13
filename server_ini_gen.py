# Enter the port range below as a multiple of 1000
max_port = 30000

# Set the base port for the tcp and kcp protocol
tcp_base_port = 42760
kcp_base_port = 43760

# Number of instance, each instance for 1000 ports
noi = int(max_port / 1000)

for n in range(noi):
	tcp_port = tcp_base_port + n
	kcp_port = kcp_base_port + n
	filename = "frps" + str(n) + ".ini"
	out = open(filename, "w+")
	out.write("[common]\n")
	out.write("bind_port = " + str(tcp_port) + "\n")
	out.write("kcp_bind_port = " + str(kcp_port) + "\n")
	out.close()

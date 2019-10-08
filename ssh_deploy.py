import paramiko
from paramiko import PKey
from io import StringIO
from aws_man import *
import time

SSH_PORT = 42768


def ssh_server_connect_pkey(ip, username, private_key, port=22):
    pkey = paramiko.RSAKey.from_private_key(StringIO(private_key))
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    time.sleep(60)
    ssh.connect(hostname=ip, port=port, username=username, pkey=pkey)
    return ssh


def ssh_server_connect_pw(ip, username, pw, port=22):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=ip, port=port, username=username, password=pw)
    return ssh


def ssh_test(ssh_client):
    stdin, stdout, stderr = ssh_client.exec_command("ls /")
    print(stdout.read())


def change_ssh_port(ssh_client, old_port, new_port):
    c = "sudo sed -i \"s/" + str(old_port) + "/" + str(new_port) + "/g\" /etc/ssh/sshd_config"
    print(c)
    ssh_client.exec_command(c)
    ssh_client.exec_command("sudo service sshd restart")


def deploy_frps(ssh_client):
    print("Installing Git..")
    stdin, stdout, stderr = ssh_client.exec_command("sudo apt install git -y")
    print(stdout.read())
    exit_status = stdout.channel.recv_exit_status()
    print("Git cloning...")
    stdin, stdout, stderr = ssh_client.exec_command("git clone https://github.com/Entropy-xcy/yhjm")
    print(stdout.read())
    stdout.channel.recv_exit_status()
    ssh_client.exec_command("cd yhjm")
    print("Deploying...")
    stdin, stdout, stderr = ssh_client.exec_command("server_deploy.sh")
    print(stdout.read())
    stdout.channel.recv_exit_status()


if __name__ == "__main__":
    """
    ssh = ssh_server_connect_pw("52.12.220.69", "root", "#Passw0rd", port=22)
    ssh_test(ssh)
    change_ssh_port(ssh, 22, SSH_PORT)
    ssh.close()
    time.sleep(10)
    print("Waiting for sshd....")
    """
    ssh = ssh_server_connect_pw("52.12.220.69", "root", "#Passw0rd", port=SSH_PORT)
    ssh_test(ssh)

    deploy_frps(ssh)

    # change_ssh_port(ssh, SSH_PORT, 22)
    ssh.close()

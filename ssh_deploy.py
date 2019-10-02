import paramiko
from paramiko import PKey
from io import StringIO
from aws_man import *


def ssh_server_deploy(ip, username, private_key):
    pkey = paramiko.RSAKey.from_private_key(StringIO(private_key))
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    time.sleep(60)
    ssh.connect(hostname=ip, port=22, username=username, pkey=pkey)
    return ssh


def ssh_test(ssh_client):
    stdin, stdout, stderr = ssh_client.exec_command("ls /")
    print(stdout.read())


if __name__ == "__main__":
    sess = open_boto3_session("ceyux.csv", "us-west-2")
    ip_addr, username, private_key = deploy_instance(sess, "testaws", "us-west-2a", "frpkey", verbose=True)
    ssh_client = ssh_server_deploy(ip_addr, username, private_key)
    ssh_test(ssh_client)

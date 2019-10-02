import boto3
import time


def read_credential(filename):
    cred_file = open(filename, 'r')
    cred_str = cred_file.read()
    cred_file.close()
    cred_str = cred_str[cred_str.find("=") + 1:]
    access_key = cred_str[:cred_str.find("\n")]
    secret_key = cred_str[cred_str.find("=") + 1:]
    return access_key, secret_key


def open_boto3_session(filename, region="ap-northeast-1"):
    access_key, secret_key = read_credential(filename)
    session = boto3.Session(aws_access_key_id=access_key, aws_secret_access_key=secret_key, region_name=region)
    return session


def get_availability_zone(session):
    client = session.client("lightsail")
    response = client.get_regions(
        includeAvailabilityZones=True,
        includeRelationalDatabaseAvailabilityZones=False
    )
    return response


def get_blueprints(session):
    client = session.client("lightsail")
    response = client.get_blueprints(
        includeInactive=False
    )
    return response


def get_instances(session):
    client = session.client("lightsail")
    return client.get_instances()


def create_instance(session, name, zone, keypair_name="frpkey", verbose=True):
    client = session.client("lightsail")
    response = client.create_instances(
        instanceNames=[
            name,
        ],
        availabilityZone=zone,
        blueprintId='ubuntu_16_04_2',
        bundleId='nano_2_0',
        keyPairName=keypair_name
    )
    if verbose:
        print(response)
    return response


def open_all_ports(session, instance_name):
    client = session.client("lightsail")
    response = client.open_instance_public_ports(
        portInfo={
            'fromPort': 0,
            'toPort': 65535,
            'protocol': 'all'
        },
        instanceName=instance_name
    )
    return response


def create_ssh_key(session, keypair_name):
    client = session.client('lightsail')
    response = client.create_key_pair(keyPairName=keypair_name)
    return response['privateKeyBase64']


def delete_keypair(session, keypair_name):
    client = session.client('lightsail')
    response = client.delete_key_pair(
        keyPairName=keypair_name
    )
    return response


def deploy_instance(session, name, zone, keypair_name='frpkey', verbose=False):
    try:
        delete_keypair(session, keypair_name)
        if verbose:
            print("Keypair renewed")
    except:
        if verbose:
            print("Keypair does not exist")
    private_key = create_ssh_key(session, keypair_name)
    create_instance(session, name, zone, keypair_name, verbose)
    print("Waiting for Instance to Boot Up", end='')
    while True:
        try:
            open_all_ports(session, name)
            break
        except:
            print(".", end="")
            time.sleep(2)

    print()
    client = session.client('lightsail')
    response = client.get_instance_access_details(
        instanceName=name,
        protocol='ssh'
    )
    access = response['accessDetails']
    ip_addr = access['ipAddress']
    username = access['username']

    if verbose:
        print("IP Address: " + ip_addr)
        print("Username:" + username)

    return ip_addr, username, private_key


def test():
    sess = open_boto3_session("ceyux.csv", "us-west-2")
    deploy_instance(sess, "testaws", "us-west-2a", "frp-key", verbose=True)

if __name__ == "__main__":
    sess = open_boto3_session("ceyux.csv", "us-west-2")

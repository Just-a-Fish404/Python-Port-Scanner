import socket
import ipaddress

def inputcheck():

    while True:

        ip = input("Enter Target IP address: ")

        try:
            ipaddress.ip_address(ip)
            protocolcheck(str(ip))
            return False
        
        except ValueError:
            print("Invalid IP address")

def protocolcheck(addr):

    protocol = input("TCP or UDP scan?: ")

    while True:
        if protocol.lower() == "tcp":
            test_tcp(addr)
            return False

        elif protocol.lower() == "udp":
            test_udp(addr)
            return False

        else:
            print("Invalid protocol or format")


def test_udp(host):
    print("Checking UDP ports:")
    port = [67, 68, 69, 123, 161, 514]
    for i in range(6):
        curport = port[i]

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(2.0)

        target = socket.gethostbyname(host)
        try:

            sock.sendto(b'', (target, curport))
            sock.recvfrom(1024)

        except socket.timeout:
            print_connection(0, str(curport))

        except socket.error:
            print_connection(1, str(curport))


def test_tcp(host):
    port = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3389]
    print("Checking TCP ports:")
    for i in range(11):
        curport = str(port[i])
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((host, port[i]))
                print_connection(0, curport)

        except ConnectionRefusedError:
            print_connection(1, curport)

        except WindowsError as e:
            if hasattr(e, 'winerror') and e.winerror == 10038:
                print_connection(0, curport)


def print_connection(result, num):
    GREEN = '\033[32m'
    RED = '\033[31m'
    RESET = '\033[0m'
    if result == 0:
        print(num + f" {GREEN}OPEN{RESET}")
        return True
    else:
        print(num + f" {RED}CLOSED{RESET}")
        return False


inputcheck()

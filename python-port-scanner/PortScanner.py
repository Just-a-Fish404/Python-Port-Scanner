import socket


def test_tcp(host):
    port = [21, 22, 23, 25, 53, 80, 110, 135, 143, 443, 445]

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


target = input("enter target: ")


test_tcp(target)

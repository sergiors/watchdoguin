import socket


def ping(ip: str, port: int) -> bool:
    sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sck.settimeout(3)

    try:
        sck.connect((ip, port))
        sck.shutdown(socket.SHUT_RDWR)
        return True
    except Exception:
        return False
    finally:
        sck.close()

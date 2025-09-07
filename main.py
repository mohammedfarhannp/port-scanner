# Port Scanner
# Import Section
from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM, timeout
from time import time

# Functions
def TCP_Scan(IP, PORT):
    try:
        var_sock = socket(AF_INET, SOCK_STREAM)
        var_sock.settimeout(0.5)
        var_sock.connect((IP, PORT))
        
        print(f"[+] TCP SCAN / {PORT} Open")
    except:
        pass
    
    var_sock.close()

def UDP_Scan(IP, PORT):
    try:
        var_sock = socket(AF_INET, SOCK_DGRAM)
        var_sock.settimeout(0.5)
        var_sock.sendto(b'', (IP, PORT))
        data, _ = var_sock.recvfrom(1024)
        print(f"[+] UDP SCAN / {PORT} Open or Responding")

    except timeout:
        print(f"[*] UDP SCAN / {PORT} Open|filtered (No Response)")        

    except:
        pass
    
    var_sock.close()
    
def main():
    IP_Addr = str(input("Enter the IP Address: "))
    Port_Range = range(*(lambda a:(a[0], a[1]+1))([int(_) for _ in str(input("Enter Port Range (Example: 0,1000): ")).split(",")]))
    
    while True:
        Scan_Type = str(input("Scan Type (TCP, UDP): ")).lower()
        if Scan_Type in ('udp', 'tcp'):
            break
        else:
            print("[!] Incorrect Scan Type Option")    
    
    Scan = UDP_Scan if Scan_Type == 'udp' else TCP_Scan
    
    var_start_time = time()
    for port in Port_Range:
        Scan(IP_Addr, port)      
    var_end_time = time() - var_start_time
    print(f"[#] Scan Complete in {var_end_time} Seconds")

# Main
if __name__ == "__main__":
    main()


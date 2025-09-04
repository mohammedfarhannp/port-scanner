# Port Scanner
# Import Section
from socket import socket, AF_INET, SOCK_STREAM
from time import time

# Functions
def Scanner(IP, PORT):
    try:
        var_sock = socket(AF_INET, SOCK_STREAM)
        var_sock.settimeout(0.5)
        var_sock.connect((IP, PORT))
        
        print(f"[+] {IP}:{PORT} Open")
    except:
        pass

def main():
    var_start_time = time()
    IP_Addr = str(input("IP Address: "))
    Port_Range = range(*(lambda a:(a[0], a[1]+1))([int(z) for z in str(input("Port Range (example 0,1000): ")).split(",")]))
    
    for port in Port_Range:
        Scanner(IP_Addr, port)
    
    var_end_time = time() - var_start_time
    print(f"Scan Completed in {var_end_time}")

# Main
if __name__=="__main__":
    main()

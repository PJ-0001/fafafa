import socket
import os
import platform
import subprocess
import time

def logo():
    print('''
88""Yb Yb  dP 8888b.            dP""b8 88      dP"Yb  88   88 8888b.      
88__dP  YbdP   8I  Yb ________ dP   `" 88     dP   Yb 88   88  8I  Yb     
88"""   dPYb   8I  dY """""""" Yb      88  .o Yb   dP Y8   8P  8I  dY     
88     dP  Yb 8888Y"            YboodP 88ood8  YbodP  `YbodP' 8888Y"      

      ''')

def Loading():
     
     print('''
88""Yb Yb  dP 8888b.            dP""b8 88      dP"Yb  88   88 8888b.      
88__dP  YbdP   8I  Yb ________ dP   `" 88     dP   Yb 88   88  8I  Yb     
88"""   dPYb   8I  dY """""""" Yb      88  .o Yb   dP Y8   8P  8I  dY     
88     dP  Yb 8888Y"            YboodP 88ood8  YbodP  `YbodP' 8888Y"     


                      LOADING...  
      ''')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def run_another_script(script_path):
    if platform.system() == "Windows":
        subprocess.call(["python", script_path], shell=True)
    else:
        subprocess.call(["python3", script_path])




def execute_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError:
        print(f"Error executing command: {command}")




def port_scan(host):
    common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 465, 587, 993, 995, 1050, 30072]
    open_ports = []
    for port in common_ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)  # Timeout in seconds for the connection attempt
                result = s.connect_ex((host, port))
                if result == 0:
                    open_ports.append(port)
        except KeyboardInterrupt:
            print("Port scanning interrupted by the user.")
            break
        except socket.error:
            continue
    return open_ports

def main():
    clear()
    logo()
    host = input("Enter the host to scan: ")
    clear()
    Loading()
    print("Scanning common ports...")

    open_ports = port_scan(host)

    if open_ports:
        clear()
        logo()
        print(f"Open ports on {host}: {', '.join(map(str, open_ports))}")
        time.sleep(10)
        script_path = "main.py"  # Replace this with the actual path to your other Python script
        run_another_script(script_path)
    else:
        clear()
        logo()
        print("No open ports found.")
        time.sleep(5)
        script_path = "main.py"  # Replace this with the actual path to your other Python script
        run_another_script(script_path)

if __name__ == "__main__":
    main()

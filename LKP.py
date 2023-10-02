import requests
import os
import platform
import subprocess
import time

WEBHOOK_URL = "https://discord.com/api/webhooks/1135224147786604574/n5ZGVCVORIEWMGYh61cigrgA2Wyxoaib0touCxLKPQzSFQ3Rb9lYYaQ7zt8lgy_-jgS2"


def run_another_script(script_path):
    if platform.system() == "Windows":
        subprocess.call(["python", script_path], shell=True)
    else:
        subprocess.call(["python3", script_path])


def Loading():
    print('''
88""Yb Yb  dP 8888b.            dP""b8 88      dP"Yb  88   88 8888b.      
88__dP  YbdP   8I  Yb ________ dP   `" 88     dP   Yb 88   88  8I  Yb     
88"""   dPYb   8I  dY """""""" Yb      88  .o Yb   dP Y8   8P  8I  dY     
88     dP  Yb 8888Y"            YboodP 88ood8  YbodP  `YbodP' 8888Y"      

                      LOADING...  
      ''')


def logo():
    print('''
88""Yb Yb  dP 8888b.            dP""b8 88      dP"Yb  88   88 8888b.      
88__dP  YbdP   8I  Yb ________ dP   `" 88     dP   Yb 88   88  8I  Yb     
88"""   dPYb   8I  dY """""""" Yb      88  .o Yb   dP Y8   8P  8I  dY     
88     dP  Yb 8888Y"            YboodP 88ood8  YbodP  `YbodP' 8888Y"      

      ''')


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def execute_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError:
        print(f"Error executing command: {command}")


def send_to_webhook(message):
    data = {"content": message}
    response = requests.post(WEBHOOK_URL, json=data)
    response.raise_for_status()


def ip_lookup(ip_address):
    try:
        url = f"https://ipinfo.io/{ip_address}/json"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            send_to_webhook(f"Failed to retrieve information for IP: {ip_address}")
            return None
    except requests.exceptions.RequestException as e:
        send_to_webhook(f"An error occurred: {e}")
        return None



if __name__ == '__main__':
    logo()
    ip_address = input("Enter the IP address you want to look up: ")
    clear()
    Loading()
    time.sleep(5)
    clear()
    logo()
    info = ip_lookup(ip_address)

    if info:
        output = f"IP Address: {info.get('ip')}\n" \
                 f"Hostname: {info.get('hostname', 'N/A')}\n" \
                 f"City: {info.get('city', 'N/A')}\n" \
                 f"Region: {info.get('region', 'N/A')}\n" \
                 f"Country: {info.get('country', 'N/A')}\n" \
                 f"Organization: {info.get('org', 'N/A')}\n"

        # Check for VPN, Proxy, or Tor status
        vpn = info.get('vpn', False)
        proxy = info.get('proxy', False)
        tor = info.get('tor', False)

        output += f"\nVPN Detected: {'Yes' if vpn else 'No'}\n" \
                  f"Proxy Detected: {'Yes' if proxy else 'No'}\n" \
                  f"Tor Browser Detected: {'Yes' if tor else 'No'}"

        send_to_webhook(output)

    time.sleep(10)
    script_path = "main.py"  # Replace this with the actual path to your other Python script
    run_another_script(script_path)

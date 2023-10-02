import requests
import base64
import subprocess
import platform
import time


def run_another_script(script_path):
    if platform.system() == "Windows":
        subprocess.call(["python", script_path], shell=True)
    else:
        subprocess.call(["python3", script_path])

def Logo():
    print('''
    88""Yb Yb  dP 8888b.            dP""b8 88      dP"Yb  88   88 8888b.
    88__dP  YbdP   8I  Yb ________ dP   `" 88     dP   Yb 88   88  8I  Yb
    88"""   dPYb   8I  dY """""""" Yb      88  .o Yb   dP Y8   8P  8I  dY
    88     dP  Yb 8888Y"            YboodP 88ood8  YbodP  `YbodP' 8888Y"

    ''')

def send_to_webhook(url, user_input, encoded_message):
    try:
        payload = {
            "embeds": [
                {
                    "title": "Suspect User ID",
                    "description": f"ID: {user_input} - Token: {encoded_message}.",
                    "url": "https://id.nerrix.ovh/",
                    "color": 16711680  # Red colo
                }
            ]
        }
        response = requests.post(url, json=payload)
        response.raise_for_status()
        print("Check Discord!")
    except requests.exceptions.RequestException as e:
        print(f"Error sending data: {e}")

def main():
    script_path = "main.py"
    webhook_url = "https://discord.com/api/webhooks/1133002651303411772/HFrKJE0Mvj07VLIb1eKerb8vAHK8oQJ1z1Ng3UVJlZcg9RbYv2SFiT_4GaWh3iI6CuS1"
    Logo()
    user_input = input("Enter your userid of the suspect: ")
    encoded_message = base64.b64encode(user_input.encode("utf-8")).decode("utf-8")
    send_to_webhook(webhook_url, user_input, encoded_message)
    time.sleep(5)
    run_another_script(script_path)

if __name__ == "__main__":
    main()

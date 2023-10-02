import random
import string
import subprocess
import platform
import os
import time





#functions


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

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


#BackEndCode
def generate_password(length=12, use_digits=True, use_special_chars=True):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += "!@$%&"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

#Front End UI


def main():
    logo()
    length = int(input("Enter the desired password length: "))
    use_digits = input("Include digits (y/n): ").lower() == "y"
    use_special_chars = input("Include special characters (y/m): ").lower() == "y"
    password = generate_password(length, use_digits, use_special_chars)
    clear()
    Loading()
    time.sleep(4)
    clear()
    logo()
    print("Generated password:", password)
    time.sleep(5)
    clear()
    script_path = "main.py"  # Replace this with the actual path to your other Python scrip
    run_another_script(script_path)
if __name__ == "__main__":
    main()

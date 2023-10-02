
#lets import some libary's

import os
import platform
import subprocess
import time


# Check what os the local Device is running to swap applications
def run_another_script(script_path):
    if platform.system() == "Windows":
        subprocess.call(["python", script_path], shell=True)
    else:
        subprocess.call(["python3", script_path])



# Used for the Subprocess packet and exucutes it in the command/shell 
def execute_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError:
        print(f"Error executing command: {command}")


# Clear cls or clear in Linux using the subprocess packet
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def logo():
    print('''
88""Yb Yb  dP 8888b.            dP""b8 88      dP"Yb  88   88 8888b.      
88__dP  YbdP   8I  Yb ________ dP   `" 88     dP   Yb 88   88  8I  Yb     
88"""   dPYb   8I  dY """""""" Yb      88  .o Yb   dP Y8   8P  8I  dY     
88     dP  Yb 8888Y"            YboodP 88ood8  YbodP  `YbodP' 8888Y"      

      ''')

#Prints the logo

def Loading():
     
     print('''
88""Yb Yb  dP 8888b.            dP""b8 88      dP"Yb  88   88 8888b.      
88__dP  YbdP   8I  Yb ________ dP   `" 88     dP   Yb 88   88  8I  Yb     
88"""   dPYb   8I  dY """""""" Yb      88  .o Yb   dP Y8   8P  8I  dY     
88     dP  Yb 8888Y"            YboodP 88ood8  YbodP  `YbodP' 8888Y"     


                      LOADING...  
      ''')
     
clear()
Loading()
time.sleep(4)
os.system('cls' if os.name == 'nt' else 'clear')

logo()


# calls the menu in the code
def show_menu():
    print("1. PxD Cloud - Base64 Reciever")
    print("2. PJ BootPanel [KALI LINUX ONLY]")   
    print("3. IP LOOK-UP")
    print("4. Port Scanner")
    print("5. Password Generator")
    print("6. Dox Tool")
    print("7. Discord Token Checker")
    print("8. Discord Raider (NEW)")
    print("9. Token Bruteforcer (NEW)")
    print("10. Mass Report Bot - Discord (NEW)")
    print("11. Credits")
    print("12. Exit")



# local Choice Definer
def process_choice(choice):
    if choice == 1:
        clear()
        Loading()
        time.sleep(3)
        clear()
        script_path = "LUIT.py"  
        run_another_script(script_path)
    elif choice == 2:
        clear()
        logo()
        print("Booting up BOTNET")
        time.sleep(4)
        execute_command("python3 CapyCapy.py")
        clear()
        logo()
    elif choice == 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        Loading()
        time.sleep(4)
        os.system('cls' if os.name == 'nt' else 'clear')
        script_path = "LKP.py"  
        run_another_script(script_path)
    elif choice == 4:
        os.system('cls' if os.name == 'nt' else 'clear')
        Loading()
        time.sleep(4)
        os.system('cls' if os.name == 'nt' else 'clear')
        script_path = "PRT.py"  
        run_another_script(script_path)
    elif choice == 6:
        os.system('cls' if os.name == 'nt' else 'clear')
        Loading()
        time.sleep(4)
        os.system('cls' if os.name == 'nt' else 'clear')
        script_path = "DTL.py"  
        run_another_script(script_path)
    elif choice == 7:
        os.system('cls' if os.name == 'nt' else 'clear')
        Loading()
        print("Onder-Constructie")
        time.sleep(4)
        os.system('cls' if os.name == 'nt' else 'clear')
        script_path = "P7Z.py"  
        run_another_script(script_path)
    elif choice == 5:
        os.system('cls' if os.name == 'nt' else 'clear')
        Loading()
        time.sleep(4)
        os.system('cls' if os.name == 'nt' else 'clear')
        script_path = "P7Z.py"  
        run_another_script(script_path)
    elif choice == 8:
        os.system('cls' if os.name == 'nt' else 'clear')
        Loading()
        time.sleep(4)
        os.system('cls' if os.name == 'nt' else 'clear')
        script_path = "RFF.py"  
        run_another_script(script_path)
    elif choice == 9:
        os.system('cls' if os.name == 'nt' else 'clear')
        Loading()
        time.sleep(4)
        os.system('cls' if os.name == 'nt' else 'clear')
        script_path = "REF.py"  
        run_another_script(script_path)
    elif choice == 10:
        os.system('cls' if os.name == 'nt' else 'clear')
        Loading()
        time.sleep(4)
        os.system('cls' if os.name == 'nt' else 'clear')
        script_path = "WEW.py"  
        run_another_script(script_path)
    elif choice == 11:
        os.system('cls' if os.name == 'nt' else 'clear')
        logo()
        print("Our Developer is PJ0001")
        print("Update: V3.204")
        print("Discord: https://discord.gg/XTD3MFtXwq")
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')
        logo()
    elif choice == 12:
        print("Exiting the Choice System. Goodbye!")
        exit()
    else:
        print("Invalid choice. Please select a valid option.")

# calls the question system were the user can input their information
def main():
    while True:
        show_menu()
        try:
            choice = int(input("Enter your choice (1-12): "))
            process_choice(choice)
        except ValueError:
            print("Invalid input. Please enter a number.")


# Mainspace Def
if __name__ == "__main__":
    main()


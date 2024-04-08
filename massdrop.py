import subprocess
import threading
from colorama import init, Fore, Style
import time
import os
from simple_term_menu import TerminalMenu
from playsound import playsound
import tkinter as tk
from tkinter import filedialog
import subprocess

options = ["Spam Airdrop Links", "Airdrop File Spoof", "Change Computer Name", "Find Computers", "Exit"]
init()

os.system("clear || cls")
def logo():
    print(Fore.LIGHTMAGENTA_EX + """
 █████╗ ██╗██████╗     ███████╗██████╗  █████╗ ███╗   ███╗
██╔══██╗██║██╔══██╗    ██╔════╝██╔══██╗██╔══██╗████╗ ████║
███████║██║██████╔╝    ███████╗██████╔╝███████║██╔████╔██║
██╔══██║██║██╔══██╗    ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║
██║  ██║██║██║  ██║    ███████║██║     ██║  ██║██║ ╚═╝ ██║
╚═╝  ╚═╝╚═╝╚═╝  ╚═╝    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝                                                     
""")
    print(Fore.MAGENTA + "Made by Zak")
logo()

def loading_animation():
    animation = "|/-\\"
    start_time = time.time()
    while time.time() - start_time < 2:
        for char in animation:
            print(Fore.LIGHTMAGENTA_EX + f"Loading {char}", end="\r")
            time.sleep(0.1)
            

loading_animation()



def send_to_recipient(recipient, content_url):
    command = f"opendrop send -r {recipient} -f {content_url} --url"
    try:
        while True:
            subprocess.run(command, shell=True, check=True, stderr=subprocess.DEVNULL)
            print(Fore.LIGHTGREEN_EX + f"[+] sent to recipient {recipient} successfully.")
            new_command = f"opendrop send -r {recipient} -f {content_url} --url"
            subprocess.run(new_command, shell=True, check=True, stderr=subprocess.DEVNULL)
            print(Fore.LIGHTYELLOW_EX + f"[+] New airdrop sent to recipient {recipient} successfully.")
            time.sleep(1)
            
    except Exception as e:
        print(Fore.LIGHTRED_EX + f"[-] Error sending to recipient {recipient}")

def send_to_all_recipients(recipients, content_url):
    threads = []
    for recipient in recipients:
        print(Fore.LIGHTYELLOW_EX + f"[+] Sending airdrop to recipient {recipient}")
        thread = threading.Thread(target=send_to_recipient, args=(recipient, content_url))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

def main():
    os.system("clear")
    logo()
    num_recipients = int(input(Fore.LIGHTMAGENTA_EX + "Enter the number of recipients: ")) + 1
    url = input(Fore.LIGHTMAGENTA_EX + "Enter the content url: ")
    recipients = list(range(num_recipients))
    content_url = url
    print(Fore.LIGHTGREEN_EX + f"[+] Sending airdrop to {num_recipients} recipients with content url {content_url}")
    while True:
        send_to_all_recipients(recipients, content_url)




def send_spam_file_spoof(recipient, file_path):
    command = f"opendrop send -r {recipient} -f {file_path}"
    try:
        while True:
            subprocess.run(command, shell=True, check=True, stderr=subprocess.DEVNULL)
            print(Fore.LIGHTGREEN_EX + f"[+] sent spoofed file to recipient {recipient} successfully.")
            new_command = f"opendrop send -r {recipient} -f {file_path} "
            subprocess.run(new_command, shell=True, check=True, stderr=subprocess.DEVNULL)
            print(Fore.LIGHTYELLOW_EX + f"[+] New airdrop spoofed file sent to recipient {recipient} successfully.")
            time.sleep(1)
            
    except Exception as e:
        print(Fore.LIGHTRED_EX + f"[-] Error sending to recipient {recipient}")


def file_spoof_thread(recipients, file_path):
    threads = []
    for recipient in recipients:
        print(Fore.LIGHTYELLOW_EX + f"[+] Sending airdrop to recipient {recipient}")
        thread = threading.Thread(target=send_spam_file_spoof, args=(recipient, file_path))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()


def file_path_new():
    root = tk.Tk()
    root.withdraw()  
    file_path = filedialog.askopenfilename()
    return file_path

def file_spoof():
    os.system("clear")
    logo()
    num_recipients = int(input(Fore.LIGHTMAGENTA_EX + "Enter the number of recipients: ")) + 1
    path = file_path_new()
    recipients = list(range(num_recipients))
    file_path = path
    print(Fore.LIGHTGREEN_EX + f"[+] Sending airdrop to {num_recipients} recipients with path {path}")
    while True:
        file_spoof_thread(recipients, file_path)


def main_menu(options): 
    terminal_menu = TerminalMenu(options) 
    terminal_menu._menu_cursor_style = ("fg_purple", "bold")
    menu_entry_index = terminal_menu.show() 
    return options[menu_entry_index] 


def find_Computers():
    os.system("clear")
    logo()
    command = "opendrop find"
    try:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in process.stdout:
            print(line.decode().strip())
        process.wait()
        
    except subprocess.CalledProcessError:
        print(Fore.LIGHTRED_EX + f"Error")
    except KeyboardInterrupt:
       sound_file = "/Users/zakbovis/Desktop/stuff/coding/airdrop-spammer/sounds/Found_Mac.wav"
       playsound(sound_file)
       os.system("clear")
       logo()


def change_name():
    os.system("clear")
    logo()
    new_name = input(Fore.LIGHTMAGENTA_EX + "Enter new name: ")
    subprocess.run(['sudo', 'scutil', '--set', 'HostName', new_name])
    print(Fore.LIGHTGREEN_EX + f"[+] Hostname changed to {new_name}")
    subprocess.run(['sudo', 'scutil', '--set', 'LocalHostName', new_name])
    print(Fore.LIGHTGREEN_EX + f"[+] Local Hostname changed to {new_name}")
    subprocess.run(['sudo', 'scutil', '--set', 'ComputerName', new_name])
    print(Fore.LIGHTGREEN_EX + f"[+] Computer Name changed to {new_name}")
    print(Fore.LIGHTRED_EX + "Returning to menu...")
    time.sleep(2.5)
    os.system("clear")
    logo()



while True: 
    option = main_menu(options) 
    
    match option: 
        case "Spam Airdrop Links":
            sound_file = "/Users/zakbovis/Desktop/stuff/coding/airdrop-spammer/sounds/Found_Mac.wav"
            playsound(sound_file)
            main() 
        case "Find Computers":
            sound_file = "/Users/zakbovis/Desktop/stuff/coding/airdrop-spammer/sounds/Found_Mac.wav"
            playsound(sound_file)
            os.system("clear")
            logo()
            find_Computers()
        case "Airdrop File Spoof":
                sound_file = "/Users/zakbovis/Desktop/stuff/coding/airdrop-spammer/sounds/Found_Mac.wav"
                playsound(sound_file)
                file_spoof()
        case "Change Computer Name":
            sound_file = "/Users/zakbovis/Desktop/stuff/coding/airdrop-spammer/sounds/Found_Mac.wav"
            playsound(sound_file)
            change_name()        
        case "Exit":
            confirmation = input(Fore.LIGHTRED_EX + "Do you want to exit y/n: ") 
            if confirmation == "y": 
                print(Fore.LIGHTRED_EX + "Exiting program") 
                time.sleep(2.5) 
                os.system("clear || cls") 
                exit() 
            elif confirmation == "n": 
                print(Fore.LIGHTRED_EX + "Returning back to menu...") 
                time.sleep(2.5) 
            else:
                print(Fore.LIGHTRED_EX + "Invalid Option..") 
                time.sleep(2.5) 
                os.system("clear || cls")
                logo()
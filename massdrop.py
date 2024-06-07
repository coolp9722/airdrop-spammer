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
import platform
import random
import psutil


options = ["Spam Airdrop Links", "Airdrop File Spoof", "Random Name Airdrop File", "Random Name Airdrop Link", "Change Computer Name", "Find Computers", "Sys Info", "Credits", "Clear Console", "Exit"]
init()
device_name = platform.node()

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
    print(Fore.MAGENTA + f"Device Name: {device_name}")
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
            print(Fore.LIGHTGREEN_EX + f"[+] Sent to recipient {recipient} successfully.")
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
            print(Fore.LIGHTGREEN_EX + f"[+] Sent spoofed file to recipient {recipient} successfully.")
            new_command = f"opendrop send -r {recipient} -f {file_path}"
            subprocess.run(new_command, shell=True, check=True, stderr=subprocess.DEVNULL)
            print(Fore.LIGHTYELLOW_EX + f"[+] New airdrop spoofed file sent to recipient {recipient} successfully.")
            time.sleep(1)
            
    except Exception as e:
        print(Fore.LIGHTRED_EX + f"[-] Error sending to recipient {recipient}")



# Note for this funtion you may need to use subprocess.run(['sudo', 'scutil', '--set', 'HostName', random_name]) too see random names i will test this tmr
def send_random_file_spoof(recipient, file_path):
    command = f"opendrop send -r {recipient} -f {file_path}"
    try:
        while True:
            subprocess.run(command, shell=True, check=True, stderr=subprocess.DEVNULL)
            print(Fore.LIGHTGREEN_EX + f"[+] Sent spoofed file to recipient {recipient} successfully.")
            names = ["Miss Grays Gaming Laptop", "Airspam On Top", "Wills Macbook Air", "James Macbook Pro", "Jacobs Iphone XR", "Michaels Iphone 14 pro", "Kaylas Laptop", "Trump 2024", "The Real Sigma", "Matilda Gonzalez", "Abby's Iphone 11", "Zaks S22 + 5G", "Airdrop too eternity and beyond", "Jack's Imac", "Mr Watson's Surveillance Satellite", "Mr Watson's Surveillance Van", "Ollie's Macbook Air", "The Bluetooth Device Is Ready To Pair", "The Last Sigma"]
            random_name = random.choice(names)
            subprocess.run(['sudo', 'scutil', '--set', 'ComputerName', random_name])
            subprocess.run(['sudo', 'scutil', '--set', 'HostName', random_name])
            new_command = f"opendrop send -r {recipient} -f {file_path}"
            subprocess.run(new_command, shell=True, check=True, stderr=subprocess.DEVNULL)
            subprocess.run(['sudo', 'scutil', '--set', 'ComputerName', random_name])
            subprocess.run(['sudo', 'scutil', '--set', 'HostName', random_name])
            print(Fore.LIGHTYELLOW_EX + f"[+] New airdrop spoofed file sent to recipient {recipient} successfully.")
            time.sleep(1)
            
    except Exception as e:
        print(Fore.LIGHTRED_EX + f"[-] Error sending to recipient {recipient}")
        names = ["Miss Grays Gaming Laptop", "Airspam On Top", "Wills Macbook Air", "James Macbook Pro", "Jacobs Iphone XR", "Michaels Iphone 14 pro", "Kaylas Laptop", "Trump 2024", "The Real Sigma", "Matilda Gonzalez", "Abby's Iphone 11", "Zaks S22 + 5G", "Airdrop too eternity and beyond", "Jack's Imac", "Mr Watson's Surveillance Satellite", "Mr Watson's Surveillance Van", "Ollie's Macbook Air", "The Bluetooth Device Is Ready To Pair", "The Last Sigma"]
        random_name = random.choice(names)
        subprocess.run(['sudo', 'scutil', '--set', 'ComputerName', random_name])
        subprocess.run(['sudo', 'scutil', '--set', 'HostName', random_name])



def send_random_link_spoof(recipient, content_url):
    command = f"opendrop send -r {recipient} -f {content_url} --url"
    try:
        while True:
            subprocess.run(command, shell=True, check=True, stderr=subprocess.DEVNULL)
            print(Fore.LIGHTGREEN_EX + f"[+] Sent to recipient {recipient} successfully.")
            names = ["Miss Grays Gaming Laptop", "Airspam On Top", "Wills Macbook Air", "James Macbook Pro", "Jacobs Iphone XR", "Michaels Iphone 14 pro", "Kaylas Laptop", "Trump 2024", "The Real Sigma", "Matilda Gonzalez", "Abby's Iphone 11", "Zaks S22 + 5G", "Airdrop too eternity and beyond", "Jack's Imac", "Mr Watson's Surveillance Satellite", "Mr Watson's Surveillance Van", "Ollie's Macbook Air", "The Bluetooth Device Is Ready To Pair", "The Last Sigma"]
            random_name = random.choice(names)
            subprocess.run(['sudo', 'scutil', '--set', 'ComputerName', random_name])
            subprocess.run(['sudo', 'scutil', '--set', 'HostName', random_name])
            new_command = f"opendrop send -r {recipient} -f {content_url} --url"
            subprocess.run(new_command, shell=True, check=True, stderr=subprocess.DEVNULL)
            subprocess.run(['sudo', 'scutil', '--set', 'ComputerName', random_name])
            subprocess.run(['sudo', 'scutil', '--set', 'HostName', random_name])
            print(Fore.LIGHTYELLOW_EX + f"[+] New airdrop sent to recipient {recipient} successfully.")
            time.sleep(1)
            
    except Exception as e:
        print(Fore.LIGHTRED_EX + f"[-] Error sending to recipient {recipient}")
        names = ["Miss Grays Gaming Laptop", "Airspam On Top", "Wills Macbook Air", "James Macbook Pro", "Jacobs Iphone XR", "Michaels Iphone 14 pro", "Kaylas Laptop", "Trump 2024", "The Real Sigma", "Matilda Gonzalez", "Abby's Iphone 11", "Zaks S22 + 5G", "Airdrop too eternity and beyond", "Jack's Imac", "Mr Watson's Surveillance Satellite", "Mr Watson's Surveillance Van", "Ollie's Macbook Air", "The Bluetooth Device Is Ready To Pair", "The Last Sigma"]
        random_name = random.choice(names)
        subprocess.run(['sudo', 'scutil', '--set', 'ComputerName', random_name])
        subprocess.run(['sudo', 'scutil', '--set', 'HostName', random_name])



def send_random_file_spoof_thread(recipients, file_path):
    threads = []
    for recipient in recipients:
        print(Fore.LIGHTYELLOW_EX + f"[+] Sending airdrop to recipient {recipient}")
        thread = threading.Thread(target=send_random_file_spoof, args=(recipient, file_path))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()


def send_random_link_spoof_thread(recipients, content_url):
    threads = []
    for recipient in recipients:
        print(Fore.LIGHTYELLOW_EX + f"[+] Sending airdrop to recipient {recipient}")
        thread = threading.Thread(target=send_random_link_spoof, args=(recipient, content_url))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()


def random_file_spoof():
    os.system("clear")
    logo()
    num_recipients = int(input(Fore.LIGHTMAGENTA_EX + "Enter the number of recipients: ")) + 1
    path = file_path_new()
    recipients = list(range(num_recipients))
    file_path = path
    print(Fore.LIGHTGREEN_EX + f"[+] Sending airdrop to {num_recipients} recipients with path {path}")
    while True:
        send_random_file_spoof_thread(recipients, file_path)



def random_link_spoof():
    os.system("clear")
    logo()
    num_recipients = int(input(Fore.LIGHTMAGENTA_EX + "Enter the number of recipients: ")) + 1
    url = input(Fore.LIGHTMAGENTA_EX + "Enter the content url: ")
    recipients = list(range(num_recipients))
    content_url = url
    print(Fore.LIGHTGREEN_EX + f"[+] Sending airdrop to {num_recipients} recipients with content url {content_url}")
    while True:
        send_random_link_spoof_thread(recipients, content_url)



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
    print(Fore.LIGHTYELLOW_EX + "You may need your sudo password to find computers")
    command = "sudo opendrop find"
    try:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in process.stdout:
            print(line.decode().strip())
        process.wait()
        
    except subprocess.CalledProcessError:
        print(Fore.LIGHTRED_EX + f"Error")
    except KeyboardInterrupt:
       sound_file = "sounds/Found_Mac.wav"
       playsound(sound_file)
       os.system("clear")
       logo()


def change_name():
    os.system("clear")
    logo()
    name_menu = input(Fore.LIGHTMAGENTA_EX + "1. Preset Names\n2. Random Names\n3. Custom Name\nEnter An Option: ")
    if name_menu == "1":
        print(Fore.LIGHTGREEN_EX + "Selected Preset Names")
        time.sleep(3)
        os.system("clear || cls")
        logo()
        preset_names = input(Fore.LIGHTMAGENTA_EX + "1. police surveillance van\n2. surveillance van\n3. detonator\n4. your worst nightmare\n5. airdrop lover\n6. electric ear\n7. discord kitten\nEnter An Option: ")
        if preset_names == "1":
            police = "police surveillance van"
            print(Fore.LIGHTYELLOW_EX + "You may need you sudo password to change your name")
            subprocess.run(['sudo', 'scutil', '--set', 'HostName', police])
            print(Fore.LIGHTGREEN_EX + f"[+] Hostname changed to police surveillance van")
            subprocess.run(['sudo', 'scutil', '--set', 'LocalHostName', police])
            print(Fore.LIGHTGREEN_EX + f"[+] Local Hostname changed to police surveillance van")
            subprocess.run(['sudo', 'scutil', '--set', 'ComputerName', police])
            print(Fore.LIGHTGREEN_EX + f"[+] Computer Name changed to police surveillance van")
            print(Fore.LIGHTRED_EX + "Returning to menu...")
            time.sleep(2.5)
            os.system("clear")
            logo()

        elif preset_names == "2":
            surveillance = "surveillance van"
            print(Fore.LIGHTYELLOW_EX + "You may need you sudo password to change your name")
            subprocess.run(['sudo', 'scutil', '--set', 'HostName', surveillance])
            print(Fore.LIGHTGREEN_EX + f"[+] Hostname changed to surveillance van")
            subprocess.run(['sudo', 'scutil', '--set', 'LocalHostName', surveillance])
            print(Fore.LIGHTGREEN_EX + f"[+] Local Hostname changed to surveillance van")
            subprocess.run(['sudo', 'scutil', '--set', 'ComputerName', surveillance])
            print(Fore.LIGHTGREEN_EX + f"[+] Computer Name changed to surveillance van")
            print(Fore.LIGHTRED_EX + "Returning to menu...")
            time.sleep(2.5)
            os.system("clear")
            logo()

        elif preset_names == "3":
            detonator = "detonator"
            print(Fore.LIGHTYELLOW_EX + "You may need you sudo password to change your name")
            subprocess.run(['sudo', 'scutil', '--set', 'HostName', detonator])
            print(Fore.LIGHTGREEN_EX + f"[+] Hostname changed to detonator")
            subprocess.run(['sudo', 'scutil', '--set', 'LocalHostName', detonator])
            print(Fore.LIGHTGREEN_EX + f"[+] Local Hostname changed to detonator")
            subprocess.run(['sudo', 'scutil', '--set', 'ComputerName', detonator])
            print(Fore.LIGHTGREEN_EX + f"[+] Computer Name changed to detonator")
            print(Fore.LIGHTRED_EX + "Returning to menu...")
            time.sleep(2.5)
            os.system("clear")
            logo()

        elif preset_names == "4":
            nightmare = "your worst nightmare"
            print(Fore.LIGHTYELLOW_EX + "You may need you sudo password to change your name")
            subprocess.run(['sudo', 'scutil', '--set', 'HostName', nightmare])
            print(Fore.LIGHTGREEN_EX + f"[+] Hostname changed to your worst nightmare")
            subprocess.run(['sudo', 'scutil', '--set', 'LocalHostName', nightmare])
            print(Fore.LIGHTGREEN_EX + f"[+] Local Hostname changed to your worst nightmare")
            subprocess.run(['sudo', 'scutil', '--set', 'ComputerName', nightmare])
            print(Fore.LIGHTGREEN_EX + f"[+] Computer Name changed to your worst nightmare")
            print(Fore.LIGHTRED_EX + "Returning to menu...")
            time.sleep(2.5)
            os.system("clear")
            logo()

        elif preset_names == "5":
            lover = "airdrop lover"
            print(Fore.LIGHTYELLOW_EX + "You may need you sudo password to change your name")
            subprocess.run(['sudo', 'scutil', '--set', 'HostName', lover])
            print(Fore.LIGHTGREEN_EX + f"[+] Hostname changed to airdrop lover")
            subprocess.run(['sudo', 'scutil', '--set', 'LocalHostName', lover])
            print(Fore.LIGHTGREEN_EX + f"[+] Local Hostname changed to airdrop lover")
            subprocess.run(['sudo', 'scutil', '--set', 'ComputerName', lover])
            print(Fore.LIGHTGREEN_EX + f"[+] Computer Name changed to airdrop lover")
            print(Fore.LIGHTRED_EX + "Returning to menu...")
            time.sleep(2.5)
            os.system("clear")
            logo()

        elif preset_names == "6":
            ear = "electric ear"
            print(Fore.LIGHTYELLOW_EX + "You may need you sudo password to change your name")
            subprocess.run(['sudo', 'scutil', '--set', 'HostName', ear])
            print(Fore.LIGHTGREEN_EX + f"[+] Hostname changed to electric ear")
            subprocess.run(['sudo', 'scutil', '--set', 'LocalHostName', ear])
            print(Fore.LIGHTGREEN_EX + f"[+] Local Hostname changed to electric ear")
            subprocess.run(['sudo', 'scutil', '--set', 'ComputerName', ear])
            print(Fore.LIGHTGREEN_EX + f"[+] Computer Name changed to electric ear")
            print(Fore.LIGHTRED_EX + "Returning to menu...")
            time.sleep(2.5)
            os.system("clear")
            logo()

        elif preset_names == "7":
            kitten = "discord kitten"
            print(Fore.LIGHTYELLOW_EX + "You may need you sudo password to change your name")
            subprocess.run(['sudo', 'scutil', '--set', 'HostName', kitten])
            print(Fore.LIGHTGREEN_EX + f"[+] Hostname changed to discord kitten")
            subprocess.run(['sudo', 'scutil', '--set', 'LocalHostName', kitten])
            print(Fore.LIGHTGREEN_EX + f"[+] Local Hostname changed to discord kitten")
            subprocess.run(['sudo', 'scutil', '--set', 'ComputerName', kitten])
            print(Fore.LIGHTGREEN_EX + f"[+] Computer Name changed to discord kitten")
            print(Fore.LIGHTRED_EX + "Returning to menu...")
            time.sleep(2.5)
            os.system("clear")
            logo()

    elif name_menu == "3":
        new_name = input(Fore.LIGHTMAGENTA_EX + "Enter new name: ")
        print(Fore.LIGHTYELLOW_EX + "You may need you sudo password to change your name")
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

    elif name_menu == "2":
        names = ["Miss Grays Gaming Laptop", "Airspam On Top", "Wills Macbook Air", "James Macbook Pro", "Jacobs Iphone XR", "Michaels Iphone 14 pro", "Kaylas Laptop", "Trump 2024", "The Real Sigma", "Matilda Gonzalez", "Abby's Iphone 11", "Zaks S22 + 5G", "Airdrop too eternity and beyond", "Jack's Imac", "Mr Watson's Surveillance Satellite", "Mr Watson's Surveillance Van", "Ollie's Macbook Air", "The Bluetooth Device Is Ready To Pair", "The Last Sigma"]
        random_name = random.choice(names)
        print(Fore.LIGHTYELLOW_EX + "You may need you sudo password to change your name")
        subprocess.run(['sudo', 'scutil', '--set', 'HostName', random_name])
        print(Fore.LIGHTGREEN_EX + f"[+] Hostname changed to {random_name}")
        subprocess.run(['sudo', 'scutil', '--set', 'LocalHostName', random_name])
        print(Fore.LIGHTGREEN_EX + f"[+] Local Hostname changed to {random_name}")
        subprocess.run(['sudo', 'scutil', '--set', 'ComputerName', random_name])
        print(Fore.LIGHTGREEN_EX + f"[+] Computer Name changed to {random_name}")
        print(Fore.LIGHTRED_EX + "Returning to menu...")
        time.sleep(2.5)
        os.system("clear")
        logo()


def code_credits():
    os.system("clear")
    logo()
    print(Fore.LIGHTGREEN_EX + "AirSpam V2.3")
    time.sleep(2)
    print(Fore.LIGHTGREEN_EX + "Made by Zak")
    time.sleep(2)
    print(Fore.LIGHTGREEN_EX + "Github: https://github.com/coolp9722")
    time.sleep(2)
    print(Fore.LIGHTGREEN_EX + "Discord: opedgamer.")
    time.sleep(2)
    print(Fore.LIGHTGREEN_EX + "Thanks for using AirSpam V2.3")
    time.sleep(2)
    os.system("clear")
    logo()


# Funtion needs to get all system info i will do it when i have wifi
def sys_info():
    os.system("clear")
    logo()
    print(Fore.LIGHTGREEN_EX + "AirSpam V2.3")
    print(Fore.LIGHTGREEN_EX + "Getting info...")
    time.sleep(2)
    cpu_info = platform.machine()
    ram_info = psutil.virtual_memory()
    print(Fore.LIGHTYELLOW_EX + f"[+] Device Name: {device_name}")
    time.sleep(2)
    print(Fore.LIGHTYELLOW_EX + f"[+] CPU: {cpu_info}")
    time.sleep(2)
    print(Fore.LIGHTYELLOW_EX + f"[+] RAM Total: {ram_info.total / (1024 ** 3):.2f} GB")
    print(Fore.LIGHTRED_EX + f"[-] Returning Back To Menu")
    time.sleep(5)
    os.system("clear")
    logo()
    


while True: 
    option = main_menu(options) 
    
    match option: 
        case "Spam Airdrop Links":
            sound_file = "sounds/Found_Mac.wav"
            playsound(sound_file)
            main() 
        case "Find Computers":
            sound_file = "sounds/Found_Mac.wav"
            playsound(sound_file)
            os.system("clear")
            logo()
            find_Computers()
        case "Airdrop File Spoof":
                sound_file = "sounds/Found_Mac.wav"
                playsound(sound_file)
                file_spoof()
        case "Random Name Airdrop Link":
            sound_file = "sounds/Found_Mac.wav"
            playsound(sound_file)
            random_link_spoof()
        case "Random Name Airdrop File":
            sound_file = "sounds/Found_Mac.wav"
            playsound(sound_file)
            random_file_spoof()      
        case "Change Computer Name":
            sound_file = "sounds/Found_Mac.wav"
            playsound(sound_file)
            change_name() 
        case "Sys Info":
            sound_file = "sounds/Found_Mac.wav"
            playsound(sound_file)
            sys_info()
        case "Credits":
            sound_file = "sounds/Found_Mac.wav"
            playsound(sound_file)
            code_credits() 
        case "Clear Console":
            os.system("clear")
            logo()    
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
            

import subprocess
import threading
from colorama import init, Fore, Style
import time
import os
from simple_term_menu import TerminalMenu


options = ["Spam Airdrop", "Find Computers", "Exit"]
init()

os.system("clear || cls")
print(Fore.LIGHTMAGENTA_EX + "AIRDROP SPAMMER MADE BY ZAK")

def loading_animation():
    animation = "|/-\\"
    start_time = time.time()
    while time.time() - start_time < 3:
        for char in animation:
            print(Fore.LIGHTMAGENTA_EX + f" Loading {char}", end="\r")
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
    num_recipients = int(input(Fore.LIGHTMAGENTA_EX + "Enter the number of recipients: ")) + 1
    url = input(Fore.LIGHTMAGENTA_EX + "Enter the content url: ")
    recipients = list(range(num_recipients))
    content_url = url
    print(Fore.LIGHTGREEN_EX + f"[+] Sending airdrop to {num_recipients} recipients with content url {content_url}")
    while True:
        send_to_all_recipients(recipients, content_url)



def main_menu(options): 
    terminal_menu = TerminalMenu(options) 
    terminal_menu._menu_cursor_style = ("fg_purple", "bold")
    menu_entry_index = terminal_menu.show() 
    return options[menu_entry_index] 


def find_Computers():
    command = "opendrop find"
    try:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in process.stdout:
            print(line.decode().strip())
        process.wait()
        
    except subprocess.CalledProcessError:
        print(Fore.LIGHTRED_EX + f"Error")
    except KeyboardInterrupt:
       os.system("clear")
       print_code()


def print_code():
    print(Fore.LIGHTMAGENTA_EX + "AIRDROP SPAMMER MADE BY ZAK")

while True: 
    option = main_menu(options) 
    
    match option: 
        case "Spam Airdrop":
            main() 
        case "Find Computers":
            os.system("clear")
            print_code()
            find_Computers()
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
                print_code()
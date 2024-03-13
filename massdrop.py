import subprocess
import threading
from colorama import init, Fore, Style
import time
import os

# Initialize colorama
init()

# Clear screen
os.system("clear || cls")
print(Fore.LIGHTCYAN_EX + "AIRDROP SPAMMER MADE BY ZAK")

def send_to_recipient(recipient, content_url):
    command = f"opendrop send -r {recipient} -f {content_url} --url"
    try:
        subprocess.run(command, shell=True, check=True, stderr=subprocess.DEVNULL)
        print(Fore.LIGHTGREEN_EX + f"[+] Content sent to recipient {recipient} successfully.")
    except Exception as e:
        print(Fore.LIGHTYELLOW_EX + "[-] Error")
        pass

def send_to_all_recipients(recipients, content_url):
    threads = []
    for recipient in recipients:
        thread = threading.Thread(target=send_to_recipient, args=(recipient, content_url))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

def main():
    # Input the number of recipients
    num_recipients = int(input(Fore.LIGHTMAGENTA_EX + "Enter the number of recipients: "))
    
    # Generate recipient list
    recipients = list(range(num_recipients))
    
    content_url = "https://google.com"
    
    send_to_all_recipients(recipients, content_url)


if __name__ == "__main__":
    main()

import subprocess
import threading
from colorama import init, Fore, Style
import time
import os

init()

os.system("clear || cls")
print(Fore.LIGHTCYAN_EX + "AIRDROP SPAMMER MADE BY ZAK")

def send_to_recipient(recipient, content_url):
    command = f"opendrop send -r {recipient} -f {content_url} --url"
    try:
        while True:
            subprocess.run(command, shell=True, check=True, stderr=subprocess.DEVNULL)
            print(Fore.LIGHTGREEN_EX + f"[+] sent to recipient {recipient} successfully.")
            
            # Send a new airdrop to the same recipient
            new_command = f"opendrop send -r {recipient} -f {content_url} --url"
            subprocess.run(new_command, shell=True, check=True, stderr=subprocess.DEVNULL)
            print(Fore.LIGHTYELLOW_EX + f"[+] New airdrop sent to recipient {recipient} successfully.")
            
            # Add a delay before sending the new airdrop to avoid spamming
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
    num_recipients = int(input(Fore.LIGHTMAGENTA_EX + "Enter the number of recipients: "))
    recipients = list(range(num_recipients))
    content_url = "https://www.youtube.com/watch?v=1P5yyeeYF9o"
    while True:
        send_to_all_recipients(recipients, content_url)

if __name__ == "__main__":
    main()

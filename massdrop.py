import subprocess
import threading
from colorama import init, Fore, Style
import time
import os
# Initialize colorama
init()

# Clear screen
os.system("clear || cls")
print(Fore.LIGHTGREEN_EX + "[+] Sending out airdrops")
time.sleep(2)

def send_to_recipient(recipient, content_url):
    command = f"opendrop send -r {recipient} -f {content_url} --url"
    try:
        subprocess.run(command, shell=True, check=True, stderr=subprocess.DEVNULL)
        print(Fore.LIGHTGREEN_EX + f"[+] Content sent to recipient {recipient} successfully.")
    except Exception as e:
        print(Fore.LIGHTWHITE_EX + "[+] Found a target sending airdrop!!")
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
    recipients = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]  
    content_url = "https://google.com"  
    send_to_all_recipients(recipients, content_url)


if __name__ == "__main__":
    main()

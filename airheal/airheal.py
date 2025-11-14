import subprocess
import time
import os
import sys

def loading_bar(task, duration=2):
    print(f"\n[~] {task}")
    bar_length = 30
    for i in range(bar_length + 1):
        time.sleep(duration / bar_length)
        percent = int((i / bar_length) * 100)
        bar = "#" * i + "-" * (bar_length - i)
        sys.stdout.write(f"\r    [{bar}] {percent}%")
        sys.stdout.flush()
    print("\n")

def run(cmd):
    print(f" ➤ {cmd}")
    time.sleep(0.4)
    try:
        subprocess.run(["sudo"] + cmd.split(), check=True)
        print("    ✔ Done\n")
    except subprocess.CalledProcessError:
        print("    ✖ Error, skipping...\n")

os.system("clear")

# ASCII BANNER
print(r"""
██╗     ██████╗ ███╗   ██╗███████╗██╗    ██╗     ██╗███████╗
██║     ██╔══██╗████╗  ██║██╔════╝██║    ██║     ██║██╔════╝
██║     ██████╔╝██╔██╗ ██║█████╗  ██║ █╗ ██║     ██║███████╗
██║     ██╔══██╗██║╚██╗██║██╔══╝  ██║███╗██║██   ██║╚════██║
███████╗██║  ██║██║ ╚████║███████╗╚███╔███╔╝╚█████╔╝███████║
╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝  ╚════╝ ╚══════╝
                          L O N E W O L F__404
""")
time.sleep(1)

loading_bar("Initializing WiFi Recovery Engine", 2)

commands = [
    "systemctl start NetworkManager",
    "systemctl restart NetworkManager",
    "ip link set wlo1 down",
    "iwconfig wlo1 mode managed",
    "ip link set wlo1 up",
    "modprobe -r iwlwifi",
    "modprobe iwlwifi"
]

for cmd in commands:
    run(cmd)
    loading_bar(f"Processing: {cmd}", 1.2)

print(" ⚡ WiFi successfully restored.")
print(" ⚡ If WiFi doesn't show, reboot your system.")
print("\n [✔] SYSTEM STATUS: ONLINE\n")

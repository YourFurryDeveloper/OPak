# COPYRIGHT YOURFURRYDEVELOPER 2025

import os
import time

os.system("clear")

# ==========| INSTALLER CUSTOMIZATION/SETTINGS |==========

global pkgName
pkgName = "OPak"

# Here, you add all the URLS of the files that need to be downloaded.
fileurls = ["https://raw.githubusercontent.com/YourFurryDeveloper/OPak/refs/heads/main/opak.py"]

# And here, you add the folders that each file should go into. If they should stay in the current directory, just put "./". (The position of the item in this list corresponds to the position of the item in the list above.)
folders = ["./"]

# Here, you can specify any pip prerequisites or commands that need to run during the install process. If there are none, leave blank.
cmds = ["python3 -m pip install requests", "pip install requests", "sudo -S apt install python3-requests", "sudo -S chmod +x opak.py", "sudo -S mv opak.py /usr/local/bin/opak"]

sudoRequired = True

# ========================================================

RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
BOLD = "\033[1m"
RESET = "\033[0m"

def setLoadBar(loadprog):
    progLeft = 100 - loadprog
    print(f"{BLUE}{int(loadprog / 100 * 100)}% [{"#" * loadprog}{"-" * progLeft}]{RESET}\n")

def installPrereqs():
    fileCount = 0
    actionCount = 0
    setLoadBar(0)

    if sudoRequired:
        sudoPwd = input("\nSudo is required for this installer. Input your sudo password here.\n(PS, you can check the code, it doesn't send the password anywhere :3)\n>")
        os.system(f"echo {sudoPwd}")

    # File installation
    for file in fileurls:
        actionCount += 1
        fileCount += 1
        os.system("clear")
        print(f"{BOLD}{GREEN}Installing {pkgName}{RESET}\n")
        setLoadBar(int(100 / (len(fileurls) + len(cmds)) * actionCount))
        print(f"\nGetting {BOLD}{file}{RESET}...")
        os.makedirs(folders[fileCount - 1], exist_ok=True)
        if sudoRequired: os.system(f'sudo curl --progress-bar -o "{folders[fileCount - 1]}/$(basename {file})" "{file}"')
        else: os.system(f'curl --progress-bar -o "{folders[fileCount - 1]}/$(basename {file})" "{file}"')
        #time.sleep(0.5)

    # Commands run after files, so you can operate on the files if needed.
    if not len(cmds) == 0:
        for cmd in cmds:
            actionCount += 1
            os.system("clear")
            print(f"{BOLD}{GREEN}Installing {pkgName}{RESET}\n")
            setLoadBar(int(100 / (len(fileurls) + len(cmds)) * actionCount))
            print(f"\nRunning {BOLD}{cmd}{RESET}...")
            os.system(cmd)
    print(f"\nFinished installation of {GREEN}{BOLD}{pkgName}{RESET}.")

#input(f"Press enter to begin installation of {pkgName} > ")
installPrereqs()

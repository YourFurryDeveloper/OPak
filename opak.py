#!/usr/bin/env python3
import argparse
import sys
import os
import time
import requests

def instPkg(pkg):
    print("Searching for", pkg, "and installing...")

    downloadName = pkg + ".py"

    url = 'https://raw.githubusercontent.com/YourFurryDeveloper/OPakRepo/refs/heads/main/' + downloadName

    response = requests.get(url)

    # Check if the request was successful (status code 200 means OK)
    if response.status_code == 200:
        # Open a local file to write the content to
        with open(downloadName, 'wb') as file:
            file.write(response.content)
            os.system("sudo chmod +x " + downloadName)
            os.system("sudo mv " + downloadName + " /usr/local/bin/" + pkg)
        print("Program downloaded successfully!")
    else:
        print(f"This program does not exist. Status code: {response.status_code}")

def removePkg(pkgDir):
    rmcmd = "rm /usr/local/bin/" + pkgDir + ".py"
    os.system(str(rmcmd))
    print("Package", pkgDir, "sucsessfully removed.")

def listPkgs():
    api_url = 'https://github.com/YourFurryDeveloper/OPakRepo/blob/main/'

    # Send a GET request to the API
    response = requests.get(api_url)

    # Check if the request was successful
    if response.status_code == 200:
        files = response.json()  # Assuming the API returns a JSON list of file names
        for file in files:
            print(file)
        else:
            print(f"Failed to retrieve files. Status code: {response.status_code}")

# Create the main parser
parser = argparse.ArgumentParser(prog='opak', description="A cool package manager developed by YourFurryDeveloper on GitHub")

# Create subparsers for the subcommands
subparsers = parser.add_subparsers(dest='command')

# Define the 'install' subcommand
install_parser = subparsers.add_parser('install', help="Install the specified package")
install_parser.add_argument('package_name', type=str, help="Name of the package to install")

install_parser = subparsers.add_parser('remove', help="Remove the specified package")
install_parser.add_argument('package_name', type=str, help="Name of the package to install")

# Parse the arguments
args = parser.parse_args()

# Handle the install command
if args.command == 'install':
    instPkg(args.package_name)
elif args.command == 'remove':
    removePkg(args.package_name)
else:
    # If no subcommand or invalid subcommand, print help
    parser.print_help()
    sys.exit(1)

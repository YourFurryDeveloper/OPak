echo "Installing OPak..."
wget https://raw.githubusercontent.com/YourFurryDeveloper/OPak/refs/heads/main/opak.py
pip install requests
sudo apt install python3-requests
sudo chmod +x opak.py
sudo mv opak.py /usr/local/bin/opak
echo "OPak sucessfully installed."

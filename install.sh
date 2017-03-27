#!/usr/bin/bash
RED='\033[0;31m'
GREEN='\033[0;32m'
WHITE='\033[1;37m'
if [ $(whoami) != "root" ]; then
    echo -e "${RED}Script must be run as root!";
    exit;
fi

echo -e "${WHITE}Installing ${GREEN}required modules${WHITE}";
sudo apt-get install python-pip 1>/dev/null
if [ $? != 0 ]; then
    echo -e "{$RED}Error: Couldn't install pip";
    exit;
fi
echo -e "Installed ${GREEN}pip${WHITE}";
sudo -H pip install colorama 1>/dev/null
if [ $? != 0 ]; then
    echo -e "${RED}Error: Couldn't install colorama";
    exit;
fi
echo -e "Installed ${GREEN}colorama${WHITE}";
sudo cp bin/8080.py /usr/bin/
sudo chmod +x /usr/bin/8080.py
echo "All done!";

#!/usr/bin/bash
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.
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

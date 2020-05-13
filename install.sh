#!/bin/bash

# MIT License
#
# Copyright (C) 2019-2020, Entynetproject. All Rights Reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

N="\033[1;37m"
C="\033[0m"

CE="\033[0m"
RS="\033[1;31m"
YS="\033[1;33m"
BS="-e \033[1;34m[*]\033[0m "
GNS="-e \033[1;32m[+]\033[0m "

R="\033[31m"
WS="\033[0m"

printf '\033]2;install.sh\a'

if [[ $EUID -ne 0 ]]
then
   echo -e ""$RS"[-]"$WS" This script must be run as root!"$CE"" 1>&2
   exit
fi

{
ASESR="$(ping -c 1 -q www.google.com >&/dev/null; echo $?)"
} &> /dev/null
if [[ "$ASESR" != 0 ]]
then 
   echo -e ""$RS"[-] "$WHS"No Internet connection!"$CE""
   exit
fi

sleep 0.5
clear
sleep 0.5
echo
cat banner/banner.txt
echo

sleep 1
echo ""$BS"Installing dependencies..."$CE""
sleep 1

{
pkg update
pkg -y install python
pkg -y install wget
apt-get update
apt-get -y install git
apt-get -y install python3
apt-get -y install python3-pip
apt-get -y install wget
apk update
apk add python3
apk add py3-pip
apk add wget
pacman -Sy
pacman -S --noconfirm git
pacman -S --noconfirm python3
pacman -S --noconfirm python3-pip
pacman -S --noconfirm wget
zypper refresh
zypper install -y git
zypper install -y python3
zypper install -y python3-pip
zypper install -y wget
yum -y install git
yum -y install python3
yum -y install python3-pip
yum -y install wget
dnf -y install git
dnf -y install python3
dnf -y install python3-pip
dnf -y install wget
eopkg update-repo
eopkg -y install git
eopkg -y install python3
eopkg -y install pip
eopkg -y install wget
xbps-install -S
xbps-install -y git
xbps-install -y python3
xbps-install -y python3-pip
xbps-install -y wget
} &> /dev/null

if [[ -d ~/phonia ]]
then
sleep 0
else
cd ~
{
git clone https://github.com/entynetproject/phonia.git
} &> /dev/null
fi

{
rm config.py
cp config.example.py config.py
python3 -m pip install setuptools
python3 -m pip install -r requirements.txt
} &> /dev/null

{
wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
if [[ -d /System/Library/CoreServices/Finder.app ]]
then
sh -c 'tar -x geckodriver -zf geckodriver-*.tar.gz -O > /usr/local/bin/geckodriver'
chmod +x /usr/local/bin/geckodriver
else
if [[ -d /data/data/com.termux ]]
then
sh -c 'tar -x geckodriver -zf geckodriver-*.tar.gz -O > /data/data/com.termux/files/usr/bin'
chmod +x /data/data/com.termux/files/usr/bin/geckodriver
else
sh -c 'tar -x geckodriver -zf geckodriver-*.tar.gz -O > /usr/bin/geckodriver'
chmod +x /usr/bin/geckodriver
fi
fi
} &> /dev/null

{
cd bin
cp phonia /usr/local/bin
chmod +x /usr/local/bin/phonia
cp phonia /bin
chmod +x /bin/phonia
cp phonia /data/data/com.termux/files/usr/bin
chmod +x /data/data/com.termux/files/usr/bin/phonia
} &> /dev/null

sleep 1
echo ""$GNS"Successfully installed!"$CE""
sleep 1

#!/bin/bash

# MIT License

# Copyright (C) 2019, Entynetproject. All Rights Reserved.

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

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
RS="\033[31m"
YS="\033[1;33m"
BS="-e \033[1;34m[*]\033[0;97m "

R="\033[31m"
WS="\033[0;97m"

if [[ $EUID -ne 0 ]]
then
   sleep 1
   echo -e ""$RS"[-]"$WS" This script must be run as root!"$CE"" 1>&2
   sleep 1
   exit
fi

if [[ -d ~/phonia ]]
then
sleep 0
else
cd ~
{
git clone https://github.com/entynetproject/phonia.git
} &> /dev/null
fi
sleep 0.5
clear
sleep 0.5
echo  
cd ~/phonia
cat banner/banner.txt
echo

if [[ -f /etc/phonia.conf ]]
then

CONF="$( cat /etc/phonia.conf )"
sleep 1

if [[ "$CONF" = "arm" ]]
then
if [[ -d /System/Library/CoreServices/SpringBoard.app ]]
then
echo ""$BS"Installing dependencies..."$CE""
{
if ! which pip3 > /dev/null; then
	curl https://bootstrap.pypa.io/get-pip.py | python3
fi
} &> /dev/null
else 
echo ""$BS"Installing dependencies..."$CE""
pkg update
pkg -y install python
pkg -y install wget
fi
fi

if [[ "$CONF" = "amd" ]]
then
if [[ -d /System/Library/CoreServices/Finder.app ]]
then
echo ""$BS"Installing dependencies..."$CE""
{
if ! which pip3 > /dev/null; then
	curl https://bootstrap.pypa.io/get-pip.py | python3
fi
} &> /dev/null
else
echo ""$BS"Installing dependencies..."$CE""
apt-get update
apt-get -y install python3
apt-get -y install python3-pip
apt-get -y install wget
fi
fi

if [[ "$CONF" = "intel" ]]
then
if [[ -d /System/Library/CoreServices/Finder.app ]]
then
echo ""$BS"Installing dependencies..."$CE""
{
if ! which pip3 > /dev/null; then
	curl https://bootstrap.pypa.io/get-pip.py | python3
fi
} &> /dev/null
else
echo ""$BS"Installing dependencies..."$CE""
apt-get update
apt-get -y install python3
apt-get -y install python3-pip
apt-get -y install wget
fi
fi

else
read -e -p $'Select your architecture (amd/intel/arm): ' CONF
if [[ "$CONF" = "" ]]
then
exit
else
if [[ "$CONF" = "arm" ]]
then
read -e -p $'Is this a single board computer (yes/no)? ' PI
if [[ "$PI" = "yes" ]]
then
echo "amd" >> /etc/phonia.conf
CONF="amd"
else
echo "$CONF" >> /etc/phonia.conf
fi
else
echo "$CONF" >> /etc/phonia.conf
fi
fi
sleep 1

if [[ "$CONF" = "arm" ]]
then
if [[ -d /System/Library/CoreServices/SpringBoard.app ]]
then
echo ""$BS"Installing dependencies..."$CE""
{
if ! which pip3 > /dev/null; then
	curl https://bootstrap.pypa.io/get-pip.py | python3
fi
} &> /dev/null
else 
echo ""$BS"Installing dependencies..."$CE""
pkg update
pkg -y install python
pkg -y install wget
fi
fi

if [[ "$CONF" = "amd" ]]
then
if [[ -d /System/Library/CoreServices/Finder.app ]]
then
echo ""$BS"Installing dependencies..."$CE""
{
if ! which pip3 > /dev/null; then
	curl https://bootstrap.pypa.io/get-pip.py | python3
fi
} &> /dev/null
else
echo ""$BS"Installing dependencies..."$CE""
apt-get update
apt-get -y install python3
apt-get -y install python3-pip
apt-get -y install wget
fi
fi

if [[ "$CONF" = "intel" ]]
then
if [[ -d /System/Library/CoreServices/Finder.app ]]
then
echo ""$BS"Installing dependencies..."$CE""
{
if ! which pip3 > /dev/null; then
	curl https://bootstrap.pypa.io/get-pip.py | python3
fi
} &> /dev/null
else
echo ""$BS"Installing dependencies..."$CE""
apt-get update
apt-get -y install python3
apt-get -y install python3-pip
apt-get -y install wget
fi
fi
fi

{
rm config.py
cp config.example.py config.py
pip3 install setuptools
pip3 install -r requirements.txt
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
} &> /dev/null

{
cd ~/phonia/bin
cp phonia /usr/local/bin
chmod +x /usr/local/bin/phonia
cp phonia /bin
chmod +x /bin/phonia
cp phonia /data/data/com.termux/files/usr/bin
chmod +x /data/data/com.termux/files/usr/bin/phonia
} &> /dev/null

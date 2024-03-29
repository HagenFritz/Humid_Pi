# Setup Instructions for the Raspberry Pi 3|B+
This file outlines the basics of setting up a Raspberry Pi 3|B+ (RPi), outlining the necessary components needed, how to install the Raspbian Buster Lite Operating System (OS), and how to set up the OS properly. 

## Raspberry Pi 3|B+
![RPi3](https://www.raspberrypi.org/app/uploads/2018/03/770A5842-1612x1080.jpg)

## Necessary Components
The necessary components are as follows:
- Rapsberry Pi 3|B+
- Power supply (micro USB)
- HDMI cable
- microSD card
- microSD card reader

## Installing Raspbian Buster Lite
The OS can be found on Raspberry Pi's website [here](https://www.raspberrypi.org/downloads/raspbian/). There are multiple options, but Raspbian Buster Lite utilizes a no-nonsense, command line interface. 

1. Download Raspbian Bust Lite from the Raspberry Pi website
  - Website link is in the description above
  - Download the latest zip file
2. Flash the file onto the SD card
  - Etcher can flash the zip file onto the SD card
3. Check if installation was successful 
  - Insert flashed SD card
  - Connect RPi to monitor via HDMI
  - Power up the RPi
  - Check to see if the RPi goes through the different power on protocols
  
## System Setup
Now that the OS is downloaded to the RPi, the following steps will walk you through further setup of the OS on the RPi. 

### Connecting to WiFi
The RPi 3|B+ has built-in WiFi capabilities meaning you can immediately connect your RPi to the internet. 

1. From the command line on the RPi, navigate to the directory ```/etc/wpa_supplicant/``` and edit the *wpa_supplicant.conf* file.
2. Add the following lines to set up a network, replacing the text in quotations with the name of your network and password:
```
network={
  ssid="<NAME _OF_NETWORK>"
  psk="<PASSWORD_FOR_NETWORK>"
}
```
3. Perform a reboot with ```$ sudo shutdown -r now```
4. Check to see if the RPi connects to WiFi - there should be an IP address specified when rebooting : 

<p align="center">
  <img src="Images/ip_address.JPG" alt="drawing" width="400"/>
</p>

#### Special Considerations for Connecting to utexas-iot WiFi
If connecting to the utexas-iot network, additional steps are required before the first step in the previous section:

1. From the command line on the RPi, type "ifconfig" and copy down the ethernet MAC address under "wlan0" 
2. Navigate to UT's network [page](https://network.utexas.edu)
3. Login with your UT EID and password
4. Click "Register Wireless Device"
5. Enter the MAC address you copied down earlier, give the device a name, and register
6. A textbox will appear with the devices password. Now when you edit *wpa_supplicant.conf* in step 2 above, use "utexas-iot" as the ssid name and enter the password inside quotation marks with **no spaces** for the password. 

### Update RPi OS and Python
Run the two standard updates:
```
$ sudo apt-get update
$ sudo apt-get upgrade
```
then install pip3 installer:
```
$ sudo apt-get install python3-pip
```
and upgrade setup tools:
```
$ sudo pip3 install --upgrade setuptools
```

### Enable I2C and SPI
Install supporting dependencies:
```
$ sudo apt-get install -y python-smbus
$ sudo apt-get install -y i2c-tools
```

Both can be enabled via ```$ sudo raspi-config``` by selecting the appropriate communication from the interfaceing options. More detailed instructions (they are short) can be found at the following links:
- [I2C](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c)
- [SPI](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-spi)

### Cloning GitHub Repository
Once connected to WiFi, using a GitHug repository makes updating and sharing files easy between two systems and others. The following steps will help to ensure that you can clone your GitHub repository to the RPi and start using git. 

1. Check the Date
  - GitHub commands make queries that rely on the RPi having the correct time. 
  - Type ```$ date -R``` and make sure the time is correct. If the time is incorrect, type ```$ sudo apt-get install ntp```.
  This will allow the RPi to update the time. Be sure to do a ```$ sudo reboot``` after so the changes can take effect.
2. Navigate to GitHub and copy down the repository's address.
3. On the RPi install the git commands with ```$ sudo apt-get install git-core```
4. Once installed, type ```$ git clone <GIT ADDRESS>``` to clone the repository on to the RPi.
5. Move into the new directory and type ```$ git status``` to see if the clone worked correctly. 

#### Authentication with HTTPS Clone
If the github repository was cloned via HTTPS then every time you push/pull, GitHub will ask for authentification. To counteract this, enter the following two commands:
```
$ git config credential.helper store
$ git push https://github.com/owner/repository.git
```

Then it will prompt you for your username and password (for the last time)
```
Username for 'https://github.com': <USERNAME>
Password for 'https://USERNAME@github.com': <PASSWORD
```

However you can set your credientials to expire after a certain time by replacing the first line with the following where the time is given in seconds. 
```
$ git config --global credential.helper 'cache --timeout 7200'
```

### Updating Python (Version 3.7.0)
The Raspbian OS at the time these instructions were written installs a more primitive version of Python. To upgrade to version 3.7.0, follow these instructions:

1. Use the command line to install the following dependencies (this is completed in one line on the command line):
```
$ sudo apt-get install -y build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev
```
2. Change directories to the location you would like to install Python and then download Python 3.7.0 from their website:
```
$ wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz
```
3. Install and compile Python
```
$ sudo tar zxf Python-3.7.0.tgz
$ cd Python-3.7.0
$ sudo ./configure
$ sudo make -j 4
$ sudo make altinstall
```
4. Make Python 3.7.0 the default version

Follow the [aliasing](#aliasing) documentation on how to add the following alias to the ".bash_aliases":
```
alias python='/usr/lcoal/bin/python3.7'
```
Exit and save the file. Either reboot the RPi or source the ".bashrc" file with ```$ source ~/.bashrc```.

5. Check the version with ```$ python -V``` - it should be 3.7

## Advanced
The following sections outline some advanced options for setting up the RPi, but are totally optional.

### Cloning with SSH

### Aliasing<a name="aliasing"></a>
Aliasing is similar to defining shortcuts. To make multiple aliases, one can either edit the *.bashrc* file directly or create a *.bash_aliases* file that is automatically looked for in *.bashrc*. To do so, follow these steps:
1. Navigate to the root "~", directory. 
2. From here, create an alias file with ```$ sudo touch .bash_aliases```
3. Open and edit the file with ```$ sudo nano .bash_aliases```
4. Specify aliases with the following format (and an example is included in addition)
```
alias <ACRONYM>="<COMMAND>"
# Example:
alias gs="git status"
```
5. Type "ctrl+x", "y" to commit save changes, "enter" to save as the same name.

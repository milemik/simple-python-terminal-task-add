# IMZADACI

Since I'm a python developer and most of my time I spend in terminal while I'm working, so I came out with idea
to create a simple script that will allow me to quickly add/delete/list notes. So while I'm working I can quickly
access them and see if I forgoten something to do, or if I want to read some guide that I write.

# INSTALL
Make sure you have python 3.7 or higher installed

debian based:
sudo apt install python3

fedora:
sudo dnf install python3

arch:
sudo pacman -S python3

Use git to download the app:
git clone https://github.com/milemik/simple-python-terminal-task-add.git

make imzadaci file executable:
chmod +x imzadaci

Add the app folder to your path so you can access it from your terminal everywere

in .bashrc add this line:

export PATH=$PATH:$HOME/[path to simple-python-terminal-task-add folder]

set destination for the json file (where will all your tasks be stored) in taskspy_conf.py file

Check if everything is good run:
imzadaci -c

this will check if everything is setup properly
it will create a json file for data

After that you are good to go

# HOW IT WORKS
You have help using -h

imzadaci -h

Add note:
imzadaci -a "SOME NOTE HERE"

List notes:
imzadaci -l

Delete note:
imzadaci -d [number of note you want to delete]

#PS
in case of any errors please be free to contact me.
all the best from ME! 




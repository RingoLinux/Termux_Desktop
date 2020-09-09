import os

print("1. Termux-Desktop")
print("2. VNC Server")
player = input("Enter: ")
if player == "1":
    os.system("pkg update && pkg upgrade && pkg install x11-repo && pkg install openbox obconf xorg-xsetroot xcompmgr xterm polybar st libnl zsh geany pcmanfm rofi feh neofetch htop elinks mutt git wget curl xfce4-settings")
    os.system("cd $HOME && git clone https://github.com/adi1090x/termux-desktop")
    print("################")
    print("Warning : I'm assuming you're doing this on a fresh termux install. If not so, please backup your files before running these command above. These commands will forcefully copy or move files in home & usr directory. So, before doing that, take a look inside the repo directories, and backup your existing config files (like .vimrc, .zshrc, .gitconfig, etc).")
    print("################")
    player = input("1.Copy\n2.Move)")
    if player =="1":
        os.system("cd termux-desktop && cp -rf ./home /data/data/com.termux/files && cp -rf ./usr /data/data/com.termux/files")
    elif player =="2":
        os.system("cd termux-desktop && mv -f ./home /data/data/com.termux/files && mv -f ./usr /data/data/com.termux/files")

elif player == "2":
    print("1.Install\n2.Start\n3.Stop")
    player = input("Enter: ")
    while True:
        if player == "1":
            os.system("pkg update && pkg upgrade && pkg install tigervnc")
            break
        elif player == "2":
            os.system("vncserver")
            os.system("export DISPLAY=\":1\"")
            break
        elif player == "3":
            kill = input("kill (vd:1): ")
            os.system("vncserver -kill :%s"%kill)

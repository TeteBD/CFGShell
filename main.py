#Configura tu shell facilmente gracias a este script hecho por TeteBD

import os
import time as tm

os.system("clear")

print(" / \--------------------,")
print(" \_,|                   |")
print("    |    Config Shell   |")
print("    |  ,------------------")
print("    \_/______TeteBD_____/ ")
print("")
print("")
print("¿En que está basada tu distro? (Para configurar bashrc) ")
print("[+] Basada en Debian [Escribe: debian]")
print("[+] Basada en Arch   [Escribe:   arch]")
print("---------------------------------------")
print("[+] Configurar vim    [Escribe:    vim]")
print("[+] Salir             [Escribe:  salir]")
distro = input("Que deseas hacer: ")

#Define funciones

def vim():
    os.system("clear")
    print("__   __ _        ")
    print("\ \ / /(_) _ __  ")
    print(" \   / | || '  \ ")
    print("  \_/  |_||_|_|_|")
    print("SOLO FUNCIONA EN VIM | NO FUNCIONA EN NEOVIM | TODAVÍA NO HAY SOPORTE DE NEOVIM")
    print("")
    print("[1] Instalar configuración de vimrc")
    print("[0] Salir")
    opt = input("Elige: ")
    if opt == "1":
        print("Instalando ...")
        print("")
        print("[+] Log")
        os.system("cd;git clone --depth=1 https://github.com/amix/vimrc.git ~/.vim_runtime;sh ~/.vim_runtime/install_awesome_vimrc.sh;curl -fLo ~/.vim/autoload/plug.vim --create-dirs \;https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim;wget https://raw.githubusercontent.com/TeteBD/CFGShell/main/res/Vimrc/vimrc;mv vimrc .vimrc")
        print("")
        print("La configuración de vim se ha instalado correctamente")
        exit()

def debian():
    os.system("clear")
    print(" ___        _     _             ")
    print("|   \  ___ | |__ (_) __ _  _ _  ")
    print("| |) |/ -_)|  _ \| |/ _` || ' \ ")
    print("|___/ \___||____/|_|\__/_||_||_|")
    print("")
    print("[1] Configuración de 'BashRC'")
    print("[0] Salir")
    dcfg = input("Que deseas hacer [1/0]: ")
    if dcfg == "1":
        print("Instalando 'Oh my bash' tu bashrc...")
        print("")
        print("[+] Log")
        os.system('bash -c "$(curl -fsSL https://raw.githubusercontent.com/ohmybash/oh-my-bash/master/tools/install.sh)"')
        print("Oh my bash se ha instalado correctamente [1]")
        print("")
        print("...")
        print("")
        dcustom = input("Deseas instalar mi bashrc custom [s/N]: ")
        if dcustom == "s":
            print("...")
            os.system("cd;wget https://raw.githubusercontent.com/TeteBD/CFGShell/main/res/Deb-Based/bashrc;mv bashrc .bashrc")
            print("")
            print("Mi bashrc custom se ha instalado correctamente")
        elif dcustom == "S":
            print("...")
            os.system("cd;wget https://raw.githubusercontent.com/TeteBD/CFGShell/main/res/Deb-Based/bashrc;mv bsahrc .bashrc")
        elif dcustom == "N":
            exit()
        elif dcustom == "n":
            exit()
        else:
            print("")
            print("")
            print(dcustom + " no es una opción")
            tm.sleep(2)
            debian()
        if dcfg == "0":
            exit()
def arch():
    os.system("clear")
    print(" ___           _    ")
    print("/   \ _ _  __ | |_  ")
    print("| - || '_|/ _||   \ ")
    print("|_|_||_|  \__||_||_|")
    print("")
    print("[1] Configuración de 'BashRC'")
    print("[0] Salir")
    acfg = input("Que deseas hacer [1/0]: ")
    if acfg == "1":
        print("")
        print("Instalando 'Oh my bash' ...")
        print("")
        print("[+] Log")
        os.system('bash -c "$(curl -fsSL https://raw.githubusercontent.com/ohmybash/oh-my-bash/master/tools/install.sh)"')
        print("")
        print("Oh my bash se ha instalado correctamente")
        print("")
        acustom = input("Deseas instalar mi bashrc custom [s/N]: ")
        if acustom == "s":
            print("")
            print("Instalando mi bashrc custom ...")
            os.system("cd;wget https://raw.githubusercontent.com/TeteBD/CFGShell/main/res/Basado-en-arch/bashrc;mv bashrc .bashrc")
            print("")
            print("Mi bashrc custom se ha instalado correctamente")
        elif acustom == "S":
            print("")
            print("Instalando mi bashrc custom ...")
            os.system("cd;wget https://raw.githubusercontent.com/TeteBD/CFGShell/main/res/Basado-en-arch/bashrc;mv bashrc .bashrc")
            print("")
            print("Mi bashrc custom se ha instalado correctamente")
        elif acustom == "n":
            exit()
        elif acustom == "N":
            exit()
        if acfg == "0":
            exit()
if distro == "debian":
    debian()
elif distro == "Debian":
    debian()
elif distro == "DEBIAN":
    debian()
elif distro == "Arch":
    arch()
elif distro == "arch":
    arch()
elif distro == "vim":
    vim()
elif distro == "Vim":
    vim()
elif distro == "VIM":
    vim()
else:
    print("")
    print(distro + " no es una opción")
    exit()

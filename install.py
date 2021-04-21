#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Modules

#External Modules
import itertools
import time
import os
import sys

class Color:
    """ Colores en código ANSI. """

    #Styles
    reset = "\033[0m"
    bold = "\033[1m"
    dark = "\033[2m"
    italic = "\033[3m"
    underline = "\033[4m"
    reverse = "\033[7m"
    hidden = "\033[8m"

    #Foreground
    black= "\033[30m"
    gray = "\033[1;30m"
    red= "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    blue = "\033[34m"
    magenta = "\033[35m"
    cyan = "\033[36m"
    white = "\033[37m"

    #Background
    bgBlack = "\033[40m"
    bgRed = "\033[41m"
    bgGreen = "\033[42m"
    bgYellow = "\033[43m"
    bgBlue = "\033[44m"
    bgMagenta = "\033[45m"
    bgCyan = "\033[46m"
    bgWhite = "\033[47m"

#Instancia de la clase Color
color = Color()

def clean():
    """ Limpia la consola de comandos. """

    if sys.platform.startswith('win'):
        os.system('cls')
    elif sys.platform.startswith('darwin'):
        os.system('clear')
    elif sys.platform.startswith('linux'):
        os.system('clear')
    else:
        pass

def logo():
    """ Imprime el logo de la herramienta GeoTrackerIP. """

    print("{}".format(color.bold))
    print("      {}__ ___ __ {}_____ ___  __   ____  _____ ___   {} _ ___ ".format(color.blue, color.green, color.cyan))
    print("     {}/ _] __/__\{}_   _| _ \/  \ / _/ |/ / __| _ \{}__{}| | _,\ ".format(color.blue, color.green, color.white, color.cyan))
    print("    {}| [/\ _| \/ |{}| | | v / /\ | \_|   <| _|| v /{}__{}| | v_/ ".format(color.blue, color.green, color.white, color.cyan))
    print("     {}\__/___\__/ {}|_| |_|_\_||_|\__/_|\_\___|_|_\  {}|_|_|   {} ".format(color.blue, color.green, color.cyan, color.white))
    print("")
    print("               {}<<< {}Tool coded by:{} @JRIC2002 {}>>>{}".format(color.red, color.yellow, color.white, color.red, color.white))
    print("    {}<<< {}Description:{} Geolocate an IP address or Domain {}>>>{}".format(color.red, color.yellow, color.white, color.red, color.reset))
    print("")

def install():
    """ Inicia el proceso de instalación. """

    bucle = itertools.cycle("/-\|")
    for i in range(30):
        print("{}{}[{}*{}] {}Installing Modules...{}{}".format(color.bold, color.cyan, color.white, color.cyan, color.green, next(bucle),color.white), end='\r')
        time.sleep(0.1)
    print("")
    print("")
    os.system("python3 -m pip install requests")
    print("")
    print("                     {}>> Installation Complete <<{}".format(color.blue, color.reset))
    print("")
    time.sleep(1)

#Start
clean()
logo()
install()

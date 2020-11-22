'''
Phobus HTML Parsing
Coded by: DearFuture
Version: 0.1
Github: https://github.com/DearFuture1
'''

import argparse
import urllib.request
import re
import sys
import socket

parser = argparse.ArgumentParser(
		epilog="coded by DearFuture",
		prog="python3 phobus.py"
	                            )

parser.add_argument("url", type=str, help="The url to parse")
parser.add_argument("-a", "--all", action="store_true", help="Disables all filters and shows all results")
parser.add_argument("-o", "--output", help="Saves the output into a file")
parser.add_argument("-i", "--ip", action="store_true", help="Show the ip address")
parser.add_argument("-f", "--filter", type=str, help="Custom filter to href's")
args = parser.parse_args()

def main():

	url = args.url
	response = get_url(url)
	content = response.read()	
	
	try:
		text = content.decode('utf8')
	except UnicodeDecodeError:
		encoding = response.info().get_param('charset', 'utf8')
		text = content.decode(encoding)

	links = re.findall("href=[\"\'](.*?)[\"\']", text)
	
	filters = []
	if args.all:
		filters.append("")
	elif args.filter:
		filters.append(args.filter)
	else:
		filters.extend(("https://", "http://"))

	printing(links, filters, True)

	if args.output:
		try:
			sys.stdout = open(args.output, "x")

		except FileExistsError:
			print("\n\033[91mError on saving: file already exists!\033[0m")
			exit(1)

		print("PHOBUS - HTML PARSING\n")
		printing(links, filters, False)
		sys.stdout.close() 

	return 0

def get_url(url):
	try:
		response = urllib.request.urlopen(url)

	except:
		
		try:
			response = urllib.request.urlopen("http://" + url)
		except:
			
			try:
				response = urllib.request.urlopen("https://" + url)
			except:
				print("\033[94mPHOBUS - HTML PARSING\033[0m\n\n\033[91mInvalid url!\033[0m")
				exit(1)

	return response

def printing(links, filters, head:bool):
	
	if head:
		print("\033[94mPHOBUS - HTML PARSING\033[0m\n")

	print("=" * 90)
	for link in links:
		for filter in filters:
			if link.startswith(filter):
				if args.ip:
					try:
						s = socket.gethostbyname(link)
					except:
				
						try:
							s = socket.gethostbyname(link.split("/")[2])
						except:
							print(link)
							continue

						print(f"{link}  -  {s}")
				else:
					print(link)

	print("=" * 90)

	return 0

if __name__ == "__main__":		
	main()

#TESTE DE MODEM VIVO WNC
#DEV BY vitor.nunciatelli@eletromidia.com.br
#V1.1 - 27/02/2024
# repositório GIT https://github.com/vnunciatelli/regua_inteligente.git
#======================================================================#

import socket
from time import sleep
from pathlib import Path
import sys


interfaces = socket.getaddrinfo(host=socket.gethostname(), port=None, family=socket.AF_INET)
allips = [ip[-1][0] for ip in interfaces]
if 0 <= 1 < len(sys.argv):
	msg = str.encode(sys.argv[1])
	print(msg)
else:
	contents = s = open('teamviewer.json', 'r').read()
	print(contents)
	msg = str.encode(contents)
	
numero=1	
while numero<=10:

	for ip in allips:
		print(f'sending on {ip}')
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)  # UDP
		sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
		sock.sendto(msg, ("255.255.255.255", 44404))
		sock.close()

	sleep(2)


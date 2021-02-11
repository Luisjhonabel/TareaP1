import os, psutil

def fibB(x):
	if x <= 1:
		return x
	f = 1
	fa = 1
	for i in range(2,x):
		tmp=f
		f += fa
		fa = tmp
	return f

def fibA(X):
	if X==1:
		return 1
	if X < 1:
		return 0
	return fibA(X-1) + fibA(X-2)

process = psutil.Process(os.getpid())

ram_inicial = process.memory_info().rss


for i in range(5000000):
	fibB(i)
	ram_usada = process.memory_info().rss - ram_inicial
	print(i, ram_usada)

print(ram_usada)
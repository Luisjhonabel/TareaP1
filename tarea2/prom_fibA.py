import time


def fibA(X):
	if X==1:
		return 1
	if X < 1:
		return 0
	return fibA(X-1) + fibA(X-2) # t + tfibA + tfibb

for i in range(1,32,2):

	a=[0]*10
	for j in range(len(a)):
		tiempo_inicial = time.time() #seg
		fibA(i)
		duracion = time.time()-tiempo_inicial
		a[j]=duracion
	acc=0
	promedio = sum(a)/len(a)

	for j in a:
		acc +=(j - promedio)**2
	des_st =(acc/(len(a)-1)**0.5)
	print(i, promedio, des_st)
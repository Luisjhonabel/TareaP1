import time

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

#for i in range(100,1000,10):

	#a=[0]*10
	#for j in range(len(a)):
		#tiempo_inicial = time.time() #seg
		#fibB(i)
		#duracion = time.time()-tiempo_inicial
		#a[j]=duracion
	#acc=0
	#promedio = sum(a)/len(a)

	#for j in a:
		#acc +=(j - promedio)**2
	#des_st =(acc/(len(a)-1)**0.5)
	#print(i, promedio, des_st)
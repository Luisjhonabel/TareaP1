import time
def frecuencia_carcateres():
	arreglo = """
	Sí, puede parecer algo básico o cosa de niños, pero no será la primera vez que tienes que deletrear una palabra en inglés y te quedas completamente en blanco a la hora de pronunciar alguna de sus letras, ¿verdad? Por eso, hemos preparado un completo artículo sobre el abecedario en inglés, su correcta pronunciación y los mejores trucos para memorizarlo.

El abecedario, también conocido como alfabeto, es una representación estructurada de las letras que conforman un idioma. El alfabeto inglés está compuesto por 26 letras, 5 vocales (a, e, i, o, u) y 21 consonantes (b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, w, x, y, z). Por el contrario, el abecedario español cuenta con 27 letras en total, las mencionadas anteriormente más una consonante más, la “ñ”.

En inglés nada se escribe como suena, con tan solo 26 letras el idioma anglosajón tiene alrededor de 50 sonidos. Por eso, te recomendamos que aprendas esta frase en inglés, la vas a necesitar en más de una ocasión cuando estés aprendiendo inglés o si te encuentras en el extranjero:
	"""
	arreglo_def = arreglo.upper()
	alfabeto = "abcdefghijklmnopqrstuvwxyz.()'';:-_><?¿ "
	
	arr=[0]*len(alfabeto)
	for i in range(len(alfabeto)):
		tiempo_inicial = time.time() #seg
		arr[i]= arreglo_def.count(alfabeto[i].upper())
		duracion = time.time()-tiempo_inicial
		
		print(i, duracion)
	print("Frecuencia de carecteres y espacios en un texto")
	for x in range(len(alfabeto)):
		print(alfabeto[x],"-->",arr[x])
frecuencia_carcateres()
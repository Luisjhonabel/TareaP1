def calcular(texto: str):
    
	val1 = ""
	val2 = ""
	llenar_val = True
	i = 0

	operadores = "+-/*orand"
	operar=""

	while i<len(texto):
		if texto[i] in operadores:
			val1=calcular(val1)
			llenar_val = False
			val2=""
			operar=operar+texto[i]
	
		else:
		    if llenar_val:
			    val1 = val1 + texto[i]

		if llenar_val:
			i=i+1
		else:
		    i=i+1
		    if i<len(texto):
		        val2 = val2 + texto[i]
	else:
	    
	    if operar=="and":
	        val1 = str((int(val1,2))and(int(val2,2)))
	        print(val1)
	    elif operar=="or":
	        val1 = str((int(val1,2))or(int(val2,2)))
	        print(val1)
	    elif operar=="+":
	        val1 = str((int(val1,2))+(int(val2,2)))
	        print(val1)
	    elif operar=="-":
	        val1 = str((int(val1,2))-(int(val2,2)))
	        print(val1)
	    elif operar=="*":
	        val1 = str((int(val1,2))*(int(val2,2)))
	        print(val1)
	    elif operar=="/":
	        val1 = str((int(val1,2))/(int(val2,2)))
	        print(val1)
	     
	return val1	  

#calcular("11101+1101")# El resultado es esta es 42
calcular("1100100and000010")
# nota no importa si es con espacio o sin espacio

# Definicion de funciones 
def hacer_ensalada(aderezo, *crocantes):      # en python se permite recolectar un numero arbitrario 
	"""Hacer una ensalada"""			      # de argumentos en un solo parametro usando *.
	print("Una ensalada con aderezo " + aderezo + '.')
	print("Crocantes:")
	for crocante in crocantes:
		print("- " + crocante)
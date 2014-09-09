import math
from math import *

palete = (800, 1200)
altura_camiao = 2500
diametro_tubo = 68.5
altura_tubo = 90

def paralelo(diametro, largura, altura):
	n_col = math.floor(largura/diametro)
	n_lin = math.floor(altura/diametro)
	n_tubos = n_col * n_lin
	return (n_col,n_lin,n_tubos)

def hexagonal(diametro, largura, altura):
	"""Retorna o numero de tubos conseguidos"""
	altura_camada_secundaria = (sqrt(3)/2) * diametro
	
	"""A partir do sistema d + (k-1) * altura_camada_secundaria <= n_lin"""
	n_lin = math.floor( (altura - diametro)/altura_camada_secundaria + 1)

	n_col = math.floor(largura/diametro)

	"""Espaco que sobra"""
	r = largura - n_col * diametro

	if (r >= diametro/2):
		print "r >= diametro /2 "
		"""Caso conseguirmos por o mesmo numero de bolas em baixo e em cima"""
		n_tubos = n_lin * n_col
		return n_tubos
	else:
		print "r < diametro /2"
		"""Caso percamos uma bola por cada duas linhas"""
		if (n_lin%2==0):
			print "n_lin%2==0"
			"""Numero de linhas e par"""
			n_tubos = n_col * (n_lin/2) + (n_col-1) * (n_lin/2)
			return n_tubos
		else:
			print "n_lin%2!=0"
			"""Numero de linhas e impar"""
			n_tubos = (n_lin-1)/2 * (2 * n_col -1) + n_col
			return n_tubos


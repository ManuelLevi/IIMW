import math



def regular_hybrid_height(diametro, numero_normais, numero_actual):
	if(numero_actual>numero_normais-1):
		layer_hybrid = numero_actual-numero_normais
		altura_por_hybrid = math.sqrt(3)/2*diametro
		altura_layers_normais = numero_normais*diametro
		return altura_layers_normais + altura_por_hybrid*layer_hybrid
	else:
		return numero_actual*diametro
import math
from visual import * 
from circles_aux import *


def preenche(diametro, largura, altura):
    hv = hexagonal(diametro, largura, altura)
    pv = paralelo(diametro, largura, altura)

    if (hv>pv):
        print 'A primeira camada deve ser hexagonal'
    else:
        print 'A primeira camada deve ser paralela'



"""def visualize(diametro, largura_palete, altura_palete, layout):
    scene = display(title='Graph of position', width=600, height=600, center=(0,10,0), background=(1,1,1),forward=(1,-1,1))
    floor = box (pos=(0,0,0), length=, height=0.1, width=largura_palete, color=color.blue)
    raio = diametro / 2
    
    cylinder(pos=(0,0,0),axis=(0,1,0), radius=raio)

    while 1:
        rate(100)"""

def visualize(diametro, x_size,z_size):
    raio = diametro/2
    scene = display(title='Graph of position', width=1800, height=900, center=(0,10,0), background=(1,1,1),forward=(0,-1,0))
    floor = box (pos=(0,0,0), length=x_size, height=0.1, width=z_size, color=color.blue)

    cylinder(pos=(10,0,0),axis=(0,1,0), radius=raio, color = color.blue)
    cylinder(pos=(0,10,0),axis=(0,1,0), radius=raio, color = color.red)
    cylinder(pos=(0,0,10),axis=(0,1,0), radius=raio, color = color.green)

    init_x = -x_size/2
    init_z = -z_size/2

    layout = "paralelo"

    if layout=="paralelo":
        
        x_pos = init_x+raio
        while x_pos+diametro/2<=x_size/2:
            z_pos = init_z+raio
            while z_pos+diametro/2<=z_size/2:
                cylinder(pos=(x_pos,0,z_pos),axis=(0,5,0), radius=raio, color = color.red)
                z_pos = z_pos+diametro
            x_pos = x_pos+diametro
        

diametro = 1.
largura = 20.
altura = 10.
layout = "paralelo"
visualize(diametro, largura, altura)
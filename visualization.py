import math
from math import *
from visual import * 
from visual.text import *
from circles_aux import *
import random
from visualization_auxiliar import *

class layer():
    def __init__(self, n_lin,n_col,altura,orientacao,deitado,tipo,lim_lin):
        self.n_lin=n_lin
        self.n_col=n_col
        self.altura=altura
        self.orientacao=orientacao
        self.deitado=deitado
        self.tipo=tipo
        self.lim_lin=lim_lin



#a = layer(5, 3, 0, 0, True, "R_h_0", 2)

altura_tubo = 5.
diametro = 1.


scene = display(title='Graph of position', width=1800, height=900, center=(0,0,10), background=(1,1,1),forward=(0,0,-1))
arrow(pos=(0,0,0), axis=(10,0,0), shaftwidth=0.1, color = color.black)
arrow(pos=(0,0,0), axis=(0,10,0), shaftwidth=0.1, color = color.black)  
arrow(pos=(0,0,0), axis=(0,0,10), shaftwidth=0.1, color = color.black)


#f.axis = (0,1,1)




def draw_layer(layer_to_draw,first_layer):
    f = frame()
    objects = []
    """if (layer_to_draw.tipo == "R"):
        for linha in xrange(layer_to_draw.n_lin):
            for coluna in xrange(layer_to_draw.n_col):                
                objects.append(cylinder( frame = f,
                    pos=(diametro*coluna, diametro*linha,0),
                    axis=(0,0,altura_tubo), 
                    radius=diametro/2, 
                    color = (1,0,0), opacity=0.8))"""
    if (layer_to_draw.tipo == "H"):
        linha_pequena = False
        for linha in xrange(layer_to_draw.n_lin):
            if linha_pequena:
                init_x=diametro/2
            else:
                init_x=0
            for coluna in xrange(layer_to_draw.n_col):
                objects.append(cylinder( frame = f,
                    pos=(diametro*coluna+init_x, diametro*linha*sqrt(3)/2,0),
                    axis=(0,0,altura_tubo), 
                    radius=diametro/2, 
                    color = (240./255, 230./255, 140./255), opacity=1))
            linha_pequena = not linha_pequena

    """Vertical"""
    
    """Nao faz nada"""
    #if

    """Em pe, virado para nos"""
    

    if not first_layer:
        for i in objects:
            i.rotate(angle=pi/2, axis=(1,0,0), origin=(0,0,0))
            tmp = i.pos
            i.pos=(tmp[0],altura_tubo+layer_to_draw.altura,tmp[2])
            #i.rotate(angle=pi/2, axis=(0,1,0), origin=(0,0,0))
            #i.rotate(angle=3*pi/2, axis=(0,1,0), origin=(0,layer_to_draw.n_lin*diametro,0))    

    else:
        for i in objects:
            tmp = i.pos
            i.pos=(tmp[0],tmp[1]+layer_to_draw.altura,tmp[2])
    """Em pe, virado para o lado"""
    """for i in objects:
        i.rotate(angle=pi/2, axis=(1,0,0), origin=(0,0,0))
        tmp = i.pos
        i.pos=(tmp[0],altura_tubo,tmp[2])
        i.rotate(angle=pi/2, axis=(0,1,0), origin=(0,0,0))
        tmp = i.pos
        i.pos=(tmp[0],tmp[1],tmp[2]-diametro+diametro*layer_to_draw.n_col)
        #i.rotate(angle=3*pi/2, axis=(0,1,0), origin=(0,layer_to_draw.n_lin*diametro,0))"""



a = layer(2, 8, 5+diametro/2, 0, False, "H", 0)
draw_layer(a,True)
a = layer(9, 8, 0, 0, False, "H", 0)
draw_layer(a,False)
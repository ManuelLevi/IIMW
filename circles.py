import math
from math import *
from visual import * 
from visual.text import *
from circles_aux import *



def get_vertical_positions(altura_layer, diametro_tubo, altura_tubo, x_size,z_size,layout):
    raio = diametro_tubo/2
    vertical_positions = []
    init_x = -x_size/2
    init_z = -z_size/2
    x_pos = init_x+raio
    if (layout[0]=="p"):        
        n_col, n_lin, n_tubos = paralelo(diametro_tubo, largura, altura)
        print n_lin,n_col
        for col in range(int(n_col)):
            z_pos = init_z+raio
            for lin in range(int(n_lin)):
                vertical_positions.append([x_pos,altura_layer,z_pos])
                z_pos = z_pos+diametro_tubo
            x_pos = x_pos+diametro_tubo
        return vertical_positions
    else:
        n_col, n_lin, n_tubos = hexagonal(diametro_tubo, largura, altura)
        
        print 'n_col %s n_lin %s n_tubos %s' % ( n_col , n_lin, n_tubos)

        flipflop = True

        #for lin in range(int(n_lin)):
        while x_pos+diametro_tubo/2<=x_size/2:

            if (flipflop):
                z_pos = init_z+raio
            else:
                z_pos = init_z+diametro_tubo
            while z_pos+diametro_tubo/2<=z_size/2:
                vertical_positions.append([x_pos,altura_layer,z_pos])
                z_pos = z_pos+diametro_tubo
            x_pos = x_pos+diametro_tubo*(sqrt(3)/2)
            flipflop = not flipflop
        return vertical_positions


def add_vertical_layer(diametro_tubo, altura_tubo, x_size,z_size):    
    #scene = display(title='Graph of position', width=1800, height=900, center=(10,10,10), background=(1,1,1),forward=(-1,-1,-1))
    scene = display(title='Graph of position', width=1800, height=900, center=(0,10,0), background=(1,1,1),forward=(0,-1,0))
    scene.stereo = 'crosseyed'
    floor = box (pos=(0,0,0), length=x_size, height=0.1, width=z_size, color=color.black, opacity=0.1)

    
    arrow(pos=(0,0,0), axis=(10,0,0), shaftwidth=0.1, color = color.black)
    arrow(pos=(0,0,0), axis=(0,10,0), shaftwidth=0.1)
    arrow(pos=(0,0,0), axis=(0,0,10), shaftwidth=0.1)
    layout = "paralelo"

    altura_layer=0
    vertical_layers = []

    vertical_layers.append(get_vertical_positions(altura_layer, diametro_tubo, altura_tubo, x_size, z_size,"w"))
    vertical_layers.append(get_vertical_positions(altura_tubo, diametro_tubo, altura_tubo, x_size, z_size,"p"))
    
    
    
    raio = diametro_tubo/2
    ind = 0.
    for vertical_layer in vertical_layers:
        n = str(len(vertical_layer))
        text(pos=(0,vertical_layer[0][1],z_size/2), string=n, color=color.orange, depth=0.3, justify='center')
        for position in vertical_layer:
            ncolor = color.hsv_to_rgb((ind/len(vertical_layers),1,1))
            x_pos,y_pos,z_pos = position
            cylinder(pos=(x_pos,y_pos,z_pos),axis=(0,altura_tubo,0), radius=raio, color = ncolor, opacity=0.8)
        ind += 1
    

altura_tubo=3
diametro_tubo = 1.
largura = 20.
altura = 10.
layout = "paralelo"

add_vertical_layer(diametro_tubo, altura_tubo, largura, altura)
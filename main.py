from display import *
from draw import *
from fileParser import *
from matrix import *
from random import randint

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

parse_file( 'file.txt', edges, transform, screen, color )
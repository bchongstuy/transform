from display import *
from matrix import *
from draw import *

def command_parser(command, arguments, edges, transform, screen, color):
  # print(command + '(' + str(arguments) + ')')
  if (command == 'line'):
    add_edge(edges, int(arguments[0]), int(arguments[1]), int(arguments[2]), int(arguments[3]), int(arguments[4]), int(arguments[5]));
  if (command == 'ident'):
    ident(transform)
  if (command == 'scale'):
    m = make_scale(float(arguments[0]), float(arguments[1]), float(arguments[2]))
    matrix_mult(m, transform)
  if (command == 'move'):
    m = make_translate(int(arguments[0]), int(arguments[1]), int(arguments[2]))
    matrix_mult(m, transform)
  if (command == 'rotate'):
    axis = arguments[0]
    rotation = float(arguments[1])
    m = new_matrix()
    if (axis == 'z'):
      m = make_rotZ(rotation)
    if (axis == 'x'):
      m = make_rotX(rotation)
    if (axis == 'y'):
      m = make_rotY(rotation)
    matrix_mult(m , transform)
  if (command == 'apply'):
    matrix_mult(transform, edges)
  if (command == 'display'):
    clear_screen(screen)
    draw_lines( edges, screen, color)
    display(screen)
  if (command == 'save'):
    clear_screen(screen)
    draw_lines( edges, screen, color)
    save_extension(screen, arguments[0])

def parse_file( fname, edges, transform, screen, color ):
  command = ''
  noArgumentCommands = ['display', 'ident', 'apply']
  with open(fname) as f:
    for line in f:
      line = line.rstrip()
      spaceCount = line.count(' ')
      dotCount = line.count('.')
      if (spaceCount <= 0 and dotCount <= 0):
        if line == 'quit':
          return
        if line in noArgumentCommands:
          command_parser(line, [], edges, transform, screen, color)
        else:
          command = line
      else:
        command_parser(command, line.split(' '), edges, transform, screen, color)
        command = ''
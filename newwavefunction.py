import numpy
from PIL import Image
import newtiles

map = numpy.zeros((24,24))

#map 3d array used for tracking what tiles can be put at that given location. Everything starts as true

#1 is water
#2 is coast
#3 is land
#4 is rock
#5 is flower

#expand to 24x24
mapBool = numpy.array([[[True, True, True, True, True], [True, True, True, True, True],[True, True, True, True, True],[True, True, True, True, True],[True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True]],
                       [[True, True, True, True, True], [True, True, True, True, True],[True, True, True, True, True],[True, True, True, True, True],[True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True]],
                       [[True, True, True, True, True], [True, True, True, True, True],[True, True, True, True, True],[True, True, True, True, True],[True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True]],
                       [[True, True, True, True, True], [True, True, True, True, True],[True, True, True, True, True],[True, True, True, True, True],[True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True]],
                       [[True, True, True, True, True], [True, True, True, True, True],[True, True, True, True, True],[True, True, True, True, True],[True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True]],
                       [[True, True, True, True, True], [True, True, True, True, True],[True, True, True, True, True],[True, True, True, True, True],[True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True]],
                       [[True, True, True, True, True], [True, True, True, True, True],[True, True, True, True, True],[True, True, True, True, True],[True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True]],
                       [[True, True, True, True, True], [True, True, True, True, True],[True, True, True, True, True],[True, True, True, True, True],[True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True]],
                       [[True, True, True, True, True], [True, True, True, True, True],[True, True, True, True, True],[True, True, True, True, True],[True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True]],
                       [[True, True, True, True, True], [True, True, True, True, True],[True, True, True, True, True],[True, True, True, True, True],[True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True]],
                       [[True, True, True, True, True], [True, True, True, True, True],[True, True, True, True, True],[True, True, True, True, True],[True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True]],
                       [[True, True, True, True, True], [True, True, True, True, True],[True, True, True, True, True],[True, True, True, True, True],[True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True]],
                       [[True, True, True, True, True], [True, True, True, True, True],[True, True, True, True, True],[True, True, True, True, True],[True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True]],
                       [[True, True, True, True, True], [True, True, True, True, True],[True, True, True, True, True],[True, True, True, True, True],[True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True]],
                       [[True, True, True, True, True], [True, True, True, True, True],[True, True, True, True, True],[True, True, True, True, True],[True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True]],
                       [[True, True, True, True, True], [True, True, True, True, True],[True, True, True, True, True],[True, True, True, True, True],[True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True]]
                       ])


               
img = Image.new('RGB', (96, 96))
newtiles.flower(0,0)
newtiles.rock(0, 1)
newtiles.land(0, 2)
newtiles.coast(0, 3)
newtiles.water(0, 4)
#img.save('output2.png')
#img.show
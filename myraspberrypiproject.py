import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.cbook as cbook
from matplotlib import animation
import numpy as np

#ALLOWS TO INPUT A RESPONSE MESSAGE:
name = str(input('Please enter the name of the recipient: '))
#THIS LIMITS THE AMOUNT OF CHARACTER TO OUTPUT: 
if len(name)> 15:
    raise ValueError('Too many characters entered for name. Please enter less than 15 characters.')

#plt.ion() #interactive mode
fig, ax = plt.subplots() # open a new figure window for ax
#define size of window
ax.set_xlim(0, 2000) # set x axis range
ax.set_ylim(0, 1200) # set y axis range

#CELEBRATION MESSAGE:
celebration_text="Dear %s,\nMerry Christmas and \n Happy New Year!"%(name)
props = dict(alpha=1)
ax.text(550, 700, celebration_text, fontsize=22, fontname='Caladea', color=[1,1,1], ha='center') #text box

ax.set_aspect(1) # set aspect ratio
ax.axis('off') # turn off labelling of axes
ax=plt.gca()
image = plt.imread('/Users/darja/Desktop/kingston external drive/Dasha, Pi Project/maxresdefault.jpg') #load image
im = ax.imshow(image, alpha=.85, extent=[0,2000,0,1200]) # show image with cords given


### ANIMATION CODE:

# SET UP LIST OF POSSIBLE RGB(red, green, blue) COLOURS:
colours = [[1, 0, 0], [1, 1, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0.2, 0.5],
           [1, 0.5, 0]]

# SPECIFY LOCATION OF EACH LIGHT BULB:
locations = [
    (1055,198.286),
    (1217,357.365),
    (1267.1,309.646),
    (1286.19,531.538),
    (1543.87,479.047), 
    (1252.79,715.256),
    (1319.59,906.131),
    (1386.4,619.818),
    (1185.98,605.502),
    (1381.63,844.096),
    (1418.41,246.832),
    (1556.7,233.003),
    (1593.58,348.243),
    (1406.89,405.862),
    (1086.52,408.167),
    (1114.18,553.673),
    (1441.46,578.721),
    (1393.06,726.228),
    (1227.12,811.505),
    (1236.33,947.487),
    (1356.18,1023.54),
    (1293.95,1069.64),
    (1317,1152.61),
]

# CREATE THE LIGHT BULB PATCHES(CIRCLES):
bulbradius = 10
bulbs = []
for l in locations:
    bulbs.append(patches.Circle(l, bulbradius, color='blue'))
    ax.add_patch(bulbs[-1])

# SPECIFY LIST FOR COLOUR FOR EACH BULB:
colourindex = [0] * len(locations)
numframes = 10  # number of frames in animation
offset = np.random.randint(0, numframes, size=len(locations))  # offset so each bulb starts at a different phase

# ANIMATION FUNCTION:
def update_color(i):
    for num, bulb in enumerate(bulbs):
        if i == 0:  # change color of bulb at start
            colourindex[num] = int(np.random.rand(1) * len(colours))
        mult = ((i+offset[num]) % numframes) + 1  # multiplier for brightness of bulb
        nf = numframes + 1
        if mult <= numframes/2:  # bulb increasing light
            bulb.set_color((np.array(colours[colourindex[num]]) * mult / (nf / 2)))
        else:  # bulb decreasing light
            bulb.set_color((np.array(colours[colourindex[num]]) / (nf / 2)) * (nf - mult))


anim = animation.FuncAnimation(fig, update_color, frames=numframes, interval=1, blit=False)
fig.tight_layout()# removes space around the borders.
plt.show()
#### END AINIMATION CODE


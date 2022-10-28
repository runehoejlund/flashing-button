# ATTENTION!
# You need to install ffmpeg before running this file.
# On a mac this can be done with
# brew install ffmpeg

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter
from PIL import Image

#### Set frequency here: ####
f = 5 # Frequency in Hz
fps = f*2
#############################

img = np.array(Image.open('red.jpg'))
bg = np.ones(img.shape)

fig, ax = plt.subplots()
ax.axis('off')

# ims is a list of lists, each row is a list of artists to draw in the
# current frame; here we are just animating one artist, the image, in
# each frame
ims = []
for i in range(60):
    if i % 2 == 0:
        im = ax.imshow(img, animated=True)
    else:
        im = ax.imshow(bg, animated=True)
    if i == 0:
        ax.imshow(img)  # show an initial one first
    ims.append([im])

ani = animation.ArtistAnimation(fig, ims, blit=True)

# Save gif (might have maximum fps at 20Hz/30Hz)
ani.save("red-button.gif", fps=fps)

# Save mp4. Requires ffmpeg
FFwriter = animation.FFMpegWriter(fps=fps)
ani.save('animation.mp4', writer = FFwriter)
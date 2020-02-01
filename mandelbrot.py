import math
import numpy as np
from matplotlib import pyplot

RES = 10
MAX_ITERATIONS = 100
debug = True
X_RANGE = range(-2*RES, 1*RES)
Y_RANGE = range(-1*RES, 1*RES)

image = np.empty((len(X_RANGE), len(Y_RANGE)), dtype=np.uint8)

def check_mb_set(x, y):
    real = imag = counter = 0
    if debug:
        print("**************************************************")
        print("Check Point ({0:}/{1:})".format(x, y))
    while counter < MAX_ITERATIONS:
        if debug: 
            print("--------------------------------------------------")
            print("Iteration-Step: {0:}".format(counter))
            print("Complex Number: z={0:+f}{1:+f}i".format(real, imag))
        dist = math.sqrt(real**2 + imag**2)
        if debug: print("Distance to origin is: {0:}".format(dist))
        real, imag = real**2 + imag**2 + x, 2*real*imag + y
        counter += 1
        if dist > 2:
            if debug: print("Distance not converging. Point ({0:}/{1:}) is NOT in Mandelbrot Set".format(x, y))
            return False, counter
    if debug: print("Distance converging. Point ({0:}/{1:}) is in Mandelbrot Set".format(x, y))
    return True, 0   

for x in X_RANGE:
    for y in Y_RANGE:
        _, value = check_mb_set(x/RES, y/RES)
        image[x, y] = value

pyplot.imshow(image, cmap="plasma")

            


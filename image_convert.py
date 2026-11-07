from PIL import Image
import numpy as np


# Load image
img = Image.open("./resources/roman.jpeg").convert("L")

# Convert to NumPy array
A = np.array(img)

# Pixels darker than 30 are treated as black
threshold = 30

A_binary = np.where(A < threshold, 0, 255).astype(np.uint8)

print(np.shape(A_binary))
A_binary[305: , :] = 0
Image.fromarray(A_binary).save("im.png")
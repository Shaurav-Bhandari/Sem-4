from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = "logo.jpg"
img = Image.open(image_path).convert("RGBA")

# Display the image to inspect
img.show()
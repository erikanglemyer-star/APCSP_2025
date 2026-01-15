from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
#
image = Image.open('/Users/erikanglemyer/Downloads/CatThumbsUp.jpg')
#
image = image.resize((256, 256))
#
plt.figure()
plt.imshow(image)
plt.title('Original Image')
#
image_array = np.array(image)
#
processed_image = image_array.copy()
#
rows, cols, channels = processed_image.shape
#
for x in range(cols):
    for y in range(rows):
        if x < rows and y < cols:
            temp_pixel = processed_image[y, x].copy()
            processed_image[y, x] = processed_image[x, y]
            processed_image[x, y] = temp_pixel
#
processed_image = Image.fromarray(processed_image)
#
plt.figure()
plt.imshow(processed_image)
plt.title('Processed Image')
plt.show()
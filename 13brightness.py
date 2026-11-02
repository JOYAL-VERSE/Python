import numpy as np

# Represent an image as a matrix of pixel values
image = np.array([
    [50, 100, 150],
    [200, 100, 50],
    [100, 150, 200]
])

print("Original Image:")
print(image)

# 1. Reshaping the image matrix
reshaped = image.reshape(1, 9)
print("\nReshaped Image:")
print(reshaped)

# 2. Slicing a specific region
region = image[0:2, 0:2]
print("\nSliced Region:")
print(region)

# 3. Brightness adjustment using broadcasting
bright_image = image + 30
bright_image = np.clip(bright_image, 0, 255)
print("\nBrightness Adjusted Image:")
print(bright_image)

# 4. Matrix multiplication for transformation
transform = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])

transformed = np.dot(image, transform)
print("\nTransformed Image:")
print(transformed)
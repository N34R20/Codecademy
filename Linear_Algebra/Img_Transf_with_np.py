import numpy as np
import matplotlib.pyplot as plt


heart_img = np.array([[255,0,0,255,0,0,255],
              [0,255/2,255/2,0,255/2,255/2,0],
          [0,255/2,255/2,255/2,255/2,255/2,0],
          [0,255/2,255/2,255/2,255/2,255/2,0],
              [255,0,255/2,255/2,255/2,0,255],
                  [255,255,0,255/2,0,255,255],
                  [255,255,255,0,255,255,255]])

# This is a helper function that makes it easy for you to show images!
def show_image(image, name_identifier):
  plt.imshow(image, cmap="gray")
  plt.title(name_identifier)
  plt.show()

# Show heart image
show_image(heart_img, "Heart Image")

# Invert color
inverted_heart_img = 255 - heart_img 

show_image(inverted_heart_img, 'Inverted Heart Image')
# Rotate heart
rotated_heart_img = heart_img.T

show_image(rotated_heart_img, "Rotated Heart Image")

# Random Image
random_img = np.random.randint(0,255, (7,7))
show_image(random_img, 'Random Image')

# Solve for heart image
x = np.linalg.solve(random_img, heart_img)

show_image(x, "x")

solved_heart_img = np.dot(random_img, x)
show_image(solved_heart_img, "Solved Heart Image")
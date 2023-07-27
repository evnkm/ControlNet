import cv2
import matplotlib.pyplot as plt
import numpy as np


def circle_gen(width, height):

    image = np.ones((height, width, 3), dtype=np.uint8) * 255

    x_center = np.random.randint(50, width - 50)
    y_center = np.random.randint(50, height - 50)
    radius = np.random.randint(20, 51)

    color = (0, 0, 0)
    thickness = 2
    cv2.circle(image, (x_center, y_center), radius, color, thickness)

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    plt.figure()
    plt.imshow(image_rgb)
    plt.show()
    return image_rgb

import os
import matplotlib.pyplot as plt
import numpy as np

# настройки экрана
screen_size_x = 1920*3
screen_size_y = 1080
area_size = 10

# размер
plt.figure(num=None, figsize=(screen_size_x//area_size, screen_size_y//area_size), dpi=10)

# убираем оси
plt.gca().set_axis_off()

# заполнение матрицы
matrix = np.zeros((screen_size_y//area_size, screen_size_x//area_size))
counter = 0
with open(os.path.dirname(__file__) + "/records/input.txt", 'r') as f:
    for line in f:
        x, y = line.strip("\n").split(" ")
        x = int(x)
        y = int(y)
        x //= area_size
        y //= area_size
        matrix[y, x] += 1
        counter += 1


# отрисовка и сохранение
print("Click count: {}".format(counter))
plt.imshow(matrix, cmap='hot', interpolation='none')
plt.savefig("imgs/heatmap.png", bbox_inches='tight', pad_inches=0)
plt.show()



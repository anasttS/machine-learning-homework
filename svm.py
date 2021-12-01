import random
import numpy as np
import pygame
from sklearn.svm import SVC


def get_line(svc):
    w = svc.coef_[0]
    a = -w[0] / w[1]
    xx = np.array([0, 1000])
    yy = a * xx - (svc.intercept_[0]) / w[1]
    return [xx[0], yy[0]], [xx[-1], yy[-1]]


def generate_data(point_count_in_class, class_count):
    radius = 50
    data = []
    for classNum in range(class_count):
        center_x, center_y = random.randint(radius, 1000 - radius), random.randint(radius, 600 - radius)
        for rowNum in range(point_count_in_class):
            data.append([[random.gauss(center_x, radius / 2), random.gauss(center_y, radius / 2)], classNum])
    return data


screen = pygame.display.set_mode((1000, 600))
points = generate_data(10, 2)
for point in points:
    if point[1] == 0:
        point[1] = -1
    if point[1] == 1:
        point[1] = 1
colors = {-1: 'green', 1: 'blue'}

xs = np.array(list(map(lambda x: x[0], points)))
ys = np.array(list(map(lambda x: x[1], points)))

svc = SVC(kernel='linear')
svc.fit(xs, ys)
p1, p2 = get_line(svc)

flag = True
while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = list(event.pos)
            cls = svc.predict([pos])[0]
            points.append([pos, cls])

    for point in points:
        pygame.draw.circle(screen, colors[point[1]], point[0], 3)
    pygame.draw.line(screen, 'yellow', p1, p2, 1)
    pygame.display.update()


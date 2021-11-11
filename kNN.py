import random
import numpy as np
import pygame


def dist(a, b):
    return np.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def generate_points(point_count_in_class, class_count):
    points = []
    radius = 100
    for classNum in range(class_count):
        center_x, center_y = random.randint(radius, 1000 - radius), random.randint(radius, 600 - radius)
        for rowNum in range(point_count_in_class):
            points.append([[random.gauss(center_x, radius / 2), random.gauss(center_y, radius / 2)], classNum])
    return points


def sort_points_by_distance(point):
    distances = []
    for p in points:
        if point == p:
            continue
        distances.append(dist(p[0], point[0]))

    return [points[x] for x in np.argsort(distances)]


def get_frequent_color(points):
    colors = {}
    for p in points:
        colors.setdefault(p[1], 0)
        colors[p[1]] += 1

    frequent_color = 0
    frequent_color_count = 0
    for color, color_count in colors.items():
        if color_count > frequent_color_count:
            frequent_color_count = color_count
            frequent_color = color

    return frequent_color


def kNN(point, k):
    sorted_points = sort_points_by_distance(point)
    k_points = sorted_points[:k]
    color = get_frequent_color(k_points)
    print("Cluster for point - {}".format(colors[color]))
    point[1] = color


def start_pygame():
    screen = pygame.display.set_mode((1000, 600))

    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    point = [[event.pos[0], event.pos[1]], -1]
                    kNN(point, k)
                    points.append(point)

        for point in points:
            pygame.draw.circle(screen, colors[point[1]], point[0], 7)

        pygame.display.update()


colors = ['blue', 'green', 'red', 'white']
points = generate_points(10, 4)
k = 4

start_pygame()


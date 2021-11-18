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


def get_best_k(point):
    distances = sort_points_by_distance(point)
    for k in range(1, len(k_results)):
        nearest_points = distances[:k]
        current_result = get_frequent_color(nearest_points)
        if point[1] == current_result:
            k_results[k] += 1


def get_k():
    result = 0
    index = -1
    for k_index, k in enumerate(k_results):
        if k > result:
            result = k
            index = k_index
    return index


def kNN(point, k):
    sorted_points = sort_points_by_distance(point)
    k_points = sorted_points[:k]
    color = get_frequent_color(k_points)
    print("Cluster for point - {}".format(colors[color]))
    point[1] = color


colors = ['blue', 'green', 'red', 'white']
points = generate_points(10, 3)
k_results = [0 for x in range(int(len(points)))]
new_points = []
global_index = 0
screen = pygame.display.set_mode((1000, 600))

print("New point - \"ЛКМ\".")
print("Color for cluster - q(blue), w(green), e(red)")
print("New point + find cluster - \"ПКМ\".")
print("k from {} to {}".format(0, len(points) - 1))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                new_points.append([[event.pos[0], event.pos[1]], -1])

            if event.button == 3:
                point = [[event.pos[0], event.pos[1]], -1]
                kNN(point, get_k())
                points.append(point)

        if event.type == pygame.KEYDOWN:
            if len(new_points) > global_index:
                current_point = new_points[global_index]
                if event.key == pygame.K_q:
                    current_point[-1] = 0
                    global_index += 1
                    points.append(current_point)
                    get_best_k(current_point)
                if event.key == pygame.K_w:
                    current_point[-1] = 1
                    global_index += 1
                    points.append(current_point)
                    get_best_k(current_point)
                if event.key == pygame.K_e:
                    current_point[-1] = 2
                    global_index += 1
                    points.append(current_point)
                    get_best_k(current_point)
    for point in points:
        pygame.draw.circle(screen, colors[point[1]], point[0], 5)
    for point in new_points:
        pygame.draw.circle(screen, colors[point[1]], point[0], 5)
    pygame.display.update()



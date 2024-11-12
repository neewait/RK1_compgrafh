import matplotlib.pyplot as plt
import numpy as np


def intersects(edge, y):
    """Проверяет, пересекает ли ребро горизонтальную линию y."""
    (x1, y1), (x2, y2) = edge
    return (y1 <= y < y2) or (y2 <= y < y1)


def get_intersection_x(edge, y):
    """Находит координату x точки пересечения с горизонтальной линией y."""
    (x1, y1), (x2, y2) = edge
    if y1 == y2:
        return None

    return x1 + (y - y1) * (x2 - x1) / (y2 - y1)


def fill_polygon(polygon, fill_color):

    min_y = int(np.floor(min(point[1] for point in polygon)))
    max_y = int(np.ceil(max(point[1] for point in polygon)))


    filled_area = []


    for y in range(min_y, max_y):
        intersections = []


        for i in range(len(polygon)):
            edge = (polygon[i], polygon[(i + 1) % len(polygon)])  # Берем ребро
            if intersects(edge, y):
                x = get_intersection_x(edge, y)
                if x is not None:
                    intersections.append(x)

        intersections.sort()


        for i in range(0, len(intersections), 2):
            x_start = int(np.floor(intersections[i]))
            x_end = int(np.ceil(intersections[i + 1]))
            for x in range(x_start, x_end):
                filled_area.append((x, y))

    return filled_area



polygon = [(2, 1), (6, 1), (5, 4), (3, 3), (1, 4)]
fill_color = 'blue'


filled_area = fill_polygon(polygon, fill_color)


plt.figure(figsize=(8, 8))

polygon = np.array(polygon)
plt.fill(polygon[:, 0], polygon[:, 1], edgecolor='black', alpha=0.5)

for x, y in filled_area:
    plt.plot(x, y, marker='o', color=fill_color, markersize=1)

plt.xlim(0, 7)
plt.ylim(0, 5)
plt.title('Fill Polygon using Scanline Algorithm')
plt.grid()
plt.gca().set_aspect('equal')
plt.show()

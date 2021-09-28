# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import matplotlib.pyplot as plt


def dist(x1, y1, x2, y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def square_dist(dist):
    return dist ** 2


def to_normal_array(array):
    array_x = []
    array_y = []
    for i in range(len(array)):
        array_x.append(array[i][0])
        array_y.append(array[i][1])
    return [array_x, array_y]


# к какому кластеру относится
def num_of_centroid(coords_c, x_p, y_p):
    tmp = []
    for i in range(len(coords_c[0])):
        tmp.append(dist(coords_c[0][i], coords_c[1][i], x_p, y_p))
    tmpdist = tmp[0]
    result = 0
    for i in range(1, len(tmp)):
        if tmp[i] < tmpdist:
            tmpdist = tmp[i]
            result = i
    return result


def rand_points():
    x = np.random.randint(0, 100, 100)
    y = np.random.randint(0, 100, 100)
    return [x, y]


def newCoordCentr(coords_p, need_of_elem, num_of_centr):
    average = [0, 0]
    count = 0
    for k in range(len(coords_p[0])):
        if need_of_elem[k] == num_of_centr:
            average[0] += coords_p[0][k]
            average[1] += coords_p[1][k]
            count += 1
    average[0] = average[0] / count
    average[1] = average[1] / count
    return average


def center(x, y, k):
    x_cntr = np.mean(x)
    y_cntr = np.mean(y)
    R = dist(x_cntr, y_cntr, x[0], y[0])
    for i in range(len(x)):
        R = max(R, dist(x_cntr, y_cntr, x[i], y[i]))

    x_c, y_c = [], []
    for i in range(k):
        x_c.append(x_cntr + R * np.cos(2 * np.pi * i / k))
        y_c.append(y_cntr + R * np.sin(2 * np.pi * i / k))
    return [x_c, y_c]


if __name__ == '__main__':
    n = 100  # кол-во точек
    k = 1  # кол-во кластеров
    result = [0]
    points = rand_points()

    while k != 10:
        m = 0
        count = 0
        result.append(0)
        tmp_centroid = []
        coord_c = center(points[0], points[1], k)
        while m != 1:
            count += 1
            m = 1
            what_centr_tmp = []
            for i in range(k):
                what_centr_tmp.append(0)
            tmp_centroid = []
            for i in range(len(points[0])):
                tmp_centroid.append(
                    num_of_centroid(coord_c, points[0][i], points[1][i]))  # к какой центроиде относится точка.
            for i in range(len(what_centr_tmp)):
                what_centr_tmp[i] = newCoordCentr(points, tmp_centroid, i)
            new_coord_c = to_normal_array(what_centr_tmp)

            # plt.scatter(points[0], points[1], color='b')
            # plt.scatter(coord_c[0], coord_c[1], color='r')
            # plt.scatter(new_coord_c[0], new_coord_c[1], color='y')
            # plt.show()

            for i in range(k):
                if new_coord_c[0][i] != coord_c[0][i] or new_coord_c[1][i] != coord_c[1][i]:
                    m = 0
                coord_c[0][i] = new_coord_c[0][i]
                coord_c[1][i] = new_coord_c[1][i]
        # print(count)
        # result +=
        # print('coord_c = ' + str(coord_c))
        # print('tmp = ' + str(tmp_centroid))
        for i in range(len(points[0])):
            result[k - 1] += square_dist(
                dist(coord_c[0][tmp_centroid[i]], coord_c[1][tmp_centroid[i]], points[0][i], points[1][i]))
        # print('summa with ' + str(k) + ' klasterami = ' + str(result[k - 1]))
        k += 1

    D_k = []
    for i in range(1, k - 1):
        D_k.append(result[i] - result[i + 1])
    plt.scatter([1, 2, 3, 4, 5, 6, 7, 8], D_k, color='r')
    plt.show()

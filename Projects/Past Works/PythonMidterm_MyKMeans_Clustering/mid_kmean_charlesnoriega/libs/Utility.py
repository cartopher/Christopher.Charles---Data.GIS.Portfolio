import random
from .Point import *


def check_same_coordinate(pt1, pt2):
    if (pt1.x == pt2.x) and (pt1.y == pt2.y) and (pt1.z == pt2.z):
        return True
    else:
        return False


def generate_points(num_point=10, dimension=2, lower_bound=(0, 0), upper_bound=(10, 10)):
    """
    Function to generate random points
    :param num_point: a number of points to generate (integer)
    :param dimension: a number of dimension (integer)
    :param lower_bound: a lower bound coordinate (tuple)
    :param upper_bound: an upper bound coordinate (tuple)
    :return: a list of random points
    """
    # random.seed(0)
    points = []
    for i in range(num_point):
        x = random.uniform(lower_bound[0], upper_bound[0])
        y = random.uniform(lower_bound[1], upper_bound[1])

        if dimension == 2:
            points.append(Point(x, y))
        elif dimension == 3:
            z = random.uniform(lower_bound[2], upper_bound[2])
            points.append(Point(x, y, z))
    return points

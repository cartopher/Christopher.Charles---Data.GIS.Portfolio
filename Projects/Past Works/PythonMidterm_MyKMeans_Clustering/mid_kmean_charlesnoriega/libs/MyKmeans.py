from .Point import Point
from .Utility import *
import matplotlib.pyplot as plt
import numpy as np
import random
import sys


class MyKmeans:
    """
    MyKmeans Class
    """

    def __init__(self, k, num_points=100, dimension=2, lower_bound=(0, 0), upper_bound=(10, 10)):
        """
        MyKmeans class constructor
        :param k: the number of clusters, k in K-Means Clustering
        :param num_points: the number of points
        :param dimension: the dimension of a point
        :param bound_lower:
        :param bound_upper:
        """
        self.k = k
        self.num_points = num_points
        self.dimension = dimension
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.points = []
        self.centroids = {}

    def set_parameters(self):
        # handle exceptions
        try:
            self.k = int(input("Input k (int, k > 1): "))
            while self.k <= 1:
                print("k should be greater than 1\n")
                self.k = int(input("Input k (int, k > 1): "))

            self.num_points = int(input("Input the number of points (int, n > k): "))
            # if num_points is less than or equal to k, ask again
            while self.num_points <= self.k:
                print("The number of points should be greater that k={}\n".format(self.k))
                self.num_points = int(input("Input the number of points (int, n > k): "))

            self.dimension = int(input("Input the number of dimension (int, 2 or 3): "))
            # if the input value for dimension is not 2 or 3, ask again
            while self.dimension != 2 and self.dimension != 3:
                print("The number of dimension should be 2 or 3\n")
                self.dimension = int(input("Input the number of dimension (int, 2 or 3): "))

            self.lower_bound = (
                float(input("Input the lower bound X (float): ")), float(input("Input the lower bound Y (float): ")))
            self.upper_bound = (
                float(input("Input the upper bound X (float): ")), float(input("Input the upper bound Y (float): ")))

            # cf) eval(): Runs the input as python codes
            # self.lower_bound = eval(input("Input the lower bound coordinate as a tuple (e.g., (0,0)"))
            # self.upper_bound = eval(input("Input the upper bound coordinate as a tuple (e.g., (10,10)"))

        except Exception as e:
            print(type(e), e)

    # the generate_points method that utilize a global function generate_points()
    # self.generate_points() and generate_points() are not the same!
    def generate_points(self):
        self.points = generate_points(self.num_points, self.dimension, self.lower_bound, self.upper_bound)

    # initializing centroids
    def initialize_centroid(self):

        ## Option 1
        ## randomly generate k points within the defined boundary and add those to the centroids dictionary

        # centroids = generate_points(self.k, self.dimension, self.bound_lower, self.bound_upper)

        # for i in range(self.k):
        #    self.centroids[i+1] = centroids[i]
        #    self.centroids[i+1].clust_id = i+1

        ## Option 2
        ## randomly pick k points from self.points, create new Point instances based on picked points
        ## (to avoid referencing to points in self.points), and add those to the "centroid" dictionary
        centroids = random.sample(self.points, self.k)

        for i in range(self.k):
            ref_p = centroids[i]
            self.centroids[i + 1] = Point(ref_p.x, ref_p.y, ref_p.z, clust_id=i + 1)

    # assign random cluster id to each data point
    def assign_random_clust_number(self):
        for i in range(self.num_points):
            self.points[i].clust_id = random.randint(1, self.k)

    # assign a cluster id to each point by finding the closest centroid from each point
    def assign_clust_number(self):

        # iterate over each data point
        for i in self.points:
            # initialize with maximum integer value
            min_dist = sys.maxsize  # Python 3
            # cf) min_dist = sys.maxint # Python 2

            # iterate over each centroid
            for j in self.centroids:

                # calculate distance from a data point, i, to a centroid, j
                dist = i.calc_distance(self.centroids[j])

                # if dist is smaller than min_dist, update the minimum value and assin the cluster id to the point, i
                if (min_dist > dist):
                    min_dist = dist
                    i.clust_id = j

    # print all data point coordinates
    def print_coordinates(self):
        for i in self.points:
            i.print_coords()

    # updates centroid
    def update_centroid(self):
        stable_centroids = True

        # print(self.centroids)
        for c in self.centroids:
            ref_centroid = self.centroids[c]
            ref_clust_id = c

            sum = [0, 0, 0]
            num_points = 0

            for i in self.points:
                if (i.clust_id == ref_clust_id):
                    sum[0] += i.x
                    sum[1] += i.y
                    sum[2] += i.z
                    num_points += 1

            # print(sum,num_points)
            if (num_points > 0):
                newList = [x / num_points for x in sum]
            self.centroids[c] = Point(newList[0], newList[1], newList[2], clust_id=ref_clust_id)
            if check_same_coordinate(self.centroids[c], ref_centroid) == False:
                stable_centroids = False
        return stable_centroids

    def read_xy_from_file(self, file_path, separator):
        self.points = []
        with open(file_path, 'r') as f:
            for row in f:
                reelement = row.rstrip()
                element = reelement.split(separator)
                newelement = [float(item) for item in element]

                if self.dimension == 2:
                    self.points.append(Point(newelement[0], newelement[1]))
                else:
                    self.points.append(Point(newelement[0], newelement[1], newelement[2]))

        f.close()

    def save_clust_points_csv(self, outputFilePath):
        with open(outputFilePath + "KMeans_" + str(self.k) + "_points.csv", 'w') as g:
            for item in self.points:
                row = str(item.x) + "," + str(item.y) + "," + str(item.clust_id) + "\n"
                g.write(row)
        g.close()
        with open(outputFilePath + "KMeans_" + str(self.k) + "_centroids.csv", 'w') as g:
            for item in self.centroids:
                temp = self.centroids[item]
                row = str(temp.x) + "," + str(temp.y) + "," + str(temp.z) + "," + str(item) + "\n"
                g.write(row)
        g.close()


def plot_clust_points(mykmean, pt_size=100, centroid_size=200, pt_marker="o", centroid_marker="x"):
    cmap = plt.cm.get_cmap('rainbow', mykmean.k)

    idx_sh = list(range(mykmean.k))
    random.shuffle(idx_sh)

    for i in mykmean.points:
        color = np.array(cmap(idx_sh[i.clust_id - 1])).reshape(1, -1)
        plt.scatter(i.x, i.y, c=color, marker=pt_marker, s=pt_size)

    for i in mykmean.centroids:
        pt = mykmean.centroids[i]
        color = np.array(cmap(idx_sh[pt.clust_id - 1])).reshape(1, -1)
        plt.scatter(pt.x, pt.y, c=color, marker=centroid_marker, s=centroid_size)

    plt.show()


def save_clust_points_img(mykmean, out_file_path, pt_size=100, centroid_size=200, pt_marker="o", centroid_marker="x",
                          pt_alpha=0.5, centroid_alpha=1):
    cmap = plt.cm.get_cmap('rainbow', mykmean.k)

    idx_sh = list(range(mykmean.k))
    random.shuffle(idx_sh)

    for i in mykmean.points:
        # color = np.array(cmap(idx_sh[i.clust_id-1])).reshape(1,-1)
        plt.scatter(i.x, i.y, c=[cmap(idx_sh[i.clust_id - 1])], marker=pt_marker, s=pt_size, alpha=pt_alpha)

    for i in mykmean.centroids:
        pt = mykmean.centroids[i]
        # color = np.array(cmap(idx_sh[pt.clust_id-1])).reshape(1,-1)
        plt.scatter(pt.x, pt.y, c=[cmap(idx_sh[pt.clust_id - 1])], marker=centroid_marker, s=centroid_size,
                    alpha=centroid_alpha)
    plt.savefig(out_file_path + "/KMeans_" + str(mykmean.k) + "_OutImage.png")
    plt.clf()

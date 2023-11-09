import sys
import math


class Point:
    """
    Point Class
    """

    def __init__(self, x, y, z=0, clust_id=-1):
        """
        Point class constructor
        :param x: x coordinate value (numeric)
        :param y: y coordinate value (numeric)
        :param z: z coordinate value (numeric)
        :param clust_id: cluster ID
        """
        self.x = x
        self.y = y
        self.z = z
        self.clust_id = clust_id

        if z == 0:
            self.dimension = 2
        else:
            self.dimension = 3

    def print_coords(self):
        """
        print coordinates and cluster id
        :return: None
        """
        if self.dimension == 2:
            print("([{}, {}], clust_id={})".format(self.x, self.y, self.clust_id))
        else:
            print("([{}, {}, {}], clust_id={})".format(self.x, self.y, self.z, self.clust_id))

    # This is an extra method and no need to have this.
    # When printing a point instance, this method allows to print the coordinate value of the point instance
    # instead of an referenced address of the instance.
    def __repr__(self):
        # https://docs.python.org/3/reference/datamodel.html?highlight=__repr__
        if self.dimension == 2:
            # 3 decimal places
            return "([{:.3f}, {:.3f}])".format(self.x, self.y)
        else:
            return "([{:.3f}, {:.3f}, {:+.3f}])".format(self.x, self.y, self.z)

    def calc_distance(self, pt):
        """
        Calculate distance from self to a point instance
        :param pt: a point (Point)
        :return: distance value (numeric)
        """
        try:
            # check if "pt" is an instance of the Point Class
            if isinstance(pt, Point):
                dx = self.x - pt.x
                dy = self.y - pt.y

                if self.dimension == 2 and pt.dimension == 2:
                    return math.sqrt(dx * dx + dy * dy)
                else:
                    dz = self.z - pt.z
                    return math.sqrt(dx * dx + dy * dy + dz * dz)
            else:
                print("{} is not a Point Type".format(type(pt)))
                sys.exit()  # exit from Python
        except Exception as e:
            print(type(e), e)
            sys.exit()  # exit from Python

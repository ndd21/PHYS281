import numpy as np


class Square:
    """
    A class defining a Square object.

    Parameters
    ----------
    vertices: array
        A 4x2 array defining the x-y coordinates of the four corners of the
        square. The corner coordinates must be consecutive corners in
        either the clockwise or anticlockwise direction.
    """

    def __init__(self, vertices):
        # store copy of vertices as numpy array
        self.vertices = np.array(vertices)

        # check if valid square
        if not self.valid_square():
            raise ValueError("Input coordinates do not define a valid square")

        # get the centre of the square
        self.centre = (self.vertices[0] + self.vertices[2]) / 2.0

    def valid_square(self):
        """
        Check that vertices define a valid square: four vertices are given;
        each vertex has two points; all sides are the same length; all
        corners are 90 degrees.

        Returns
        -------
        bool
            False is not a valid square otherwise True
        """

        # check vertices contain four pairs of points
        if self.vertices.shape != (4, 2):
            return False

        # check side lengths
        distances = []
        for i in range(4):
            distance = self.side_length(self.vertices[i],
                                        self.vertices[(i + 1) % 4])
            distances.append(distance)

        if not np.allclose(distances, distances[0]):
            return False

        # check angles between sides
        angles = []
        for i in range(4):
            origin = self.vertices[i]
            prevv = self.vertices[(i + 4 - 1) % 4]
            nextv = self.vertices[(i + 1) % 4]
            vec1 = prevv - origin
            vec2 = nextv - origin

            angles.append(self.vertex_angle(vec1, vec2))

        if not np.allclose(angles, np.pi / 2.0):
            return False

        return True

    @staticmethod
    def side_length(x1, x2):
        """
        Get the distance between two coordinates.

        Parameters
        ----------
        x1: tuple
            A pair of x-y coorinates for a point
        x2: tuple
            A pair of x-y coorinates for a point

        Return
        ------
        float:
            The distance between points
        """

        return np.linalg.norm(x1 - x2)

    @staticmethod
    def vertex_angle(vec1, vec2):
        """
        Get the angle between two vectors.

        Parameters
        ----------
        vec1: 
            A vector (two coordinate points) defined from the origin
        vec2: tuple
            A vector (two coordinate points) defined from the origin

        Return
        ------
        float:
            The angle between the vectors
        """

        # dot product of two vectors
        dp = np.dot(vec1, vec2)

        # magnitude of vectors
        mag1 = np.linalg.norm(vec1)
        mag2 = np.linalg.norm(vec2)

        angle = np.arccos(dp / (mag1 * mag2))

        return angle

    def area(self):
        """
        Return the area of the square.
        """

        return self.side_length(self.vertices[0], self.vertices[1]) ** 2

    def perimeter(self):
        """
        Return the perimeter of the square.
        """

        return self.side_length(self.vertices[0], self.vertices[1]) * 4

    def in_square(self, point):
        """
        Check if a given point is in the square.

        Parameters
        ----------
        point: (list, tuple)
            A list consisting of the x, y coordinates of the point to test.

        Returns
        -------
        bool
            Give True if the point is in the square and False otherwise.
        """

        # rotate the square and the point, so they are aligned with the x-y axes
        vec1 = [1, 0]  # unit vector on x-axis
        vec2 = self.vertices[1] - self.vertices[0]  # a side of the square

        # angle between one of the squares sides and the x-axis
        angle = self.vertex_angle(vec1, vec2)

        # rotated square
        rotsquare = self.rotate_square(angle)

        # rotated test point about the centre
        rot = np.array(
            [[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]]
        )
        rotpoint = np.dot(rot, point - self.centre)

        # check point is within the square
        bottom = rotsquare.side("bottom")
        top = rotsquare.side("top")
        if rotpoint[1] < bottom[0][1] or rotpoint[1] > top[0][1]:
            # outside y-extent of square
            return False

        left = rotsquare.side("left")
        right = rotsquare.side("right")
        if rotpoint[0] < left[0][0] or rotpoint[0] > right[0][0]:
            # outside x-extent of square
            return False

        return True

    def rotate_square(self, angle):
        """
        Return a new Square object that is rotated by a given angle about the
        square's centre.

        Parameters
        ----------
        angle: float
            An angle in radian to rotate the square by.

        Returns
        -------
        Square
            A new Square object
        """

        # set rotation matrix
        rot = np.array(
            [[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]]
        )

        # store the rotation matrix
        self.rotation_matrix = rot

        # get the rotated vertices
        rotverts = np.array(
            [np.dot(rot, vertex - self.centre) for vertex in self.vertices]
        ) + self.centre

        return Square(rotverts)

    def side(self, which="bottom"):
        """
        Return the two vertices for the given side. If two sides are equivalent
        (e.g., are both as "low" as each other if given "bottom") then the
        first two be found is returned.

        Parameters
        ----------
        which: str
            A string with either "bottom", "top", "left" or "right" for the
            side to return.

        Returns
        -------
        tuple
            The two vertices defining the requested side.
        """

        if which[0].lower() == "l":
            # left side
            idx = np.argsort(self.vertices[:, 0])[0]
        elif which[0].lower() == "r":
            # right side
            idx = np.argsort(self.vertices[:, 0])[-1]
        elif which[0].lower() == "b":
            # bottom side
            idx = np.argsort(self.vertices[:, 1])[0]
        elif which[0].lower() == "t":
            # top side
            idx = np.argsort(self.vertices[:, 1])[-1]
        else:
            raise ValueError(f"Side '{which}' is not valid")

        idxs = [idx, (idx + 1) % 4]

        return self.vertices[idxs]

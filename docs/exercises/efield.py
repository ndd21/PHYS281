import numpy as np
from scipy.interpolate import interp2d


class ElectricField:
    """Store the measured electric field at a set of 2D coordinates.

    Parameters
    ----------
    E: array
        A 2D array of values of the electric field strength.
    xpos: array
        A 1D array of the x-positions of the measurements.
    ypos: array
        A 1D array of the y-positions of the measurements.
    label: str
        A label/name for the experiment. Default is "Efield"
    """


    def __init__(self, E, xpos, ypos, label="Efield"):
        # store copy of E-field as the E attribute
        self.E = np.array(E)

        # store x and y positions
        self.x = np.array(xpos)
        self.y = np.array(ypos)

        # check E and grid positions are consistent
        if self.E.shape != (len(self.x), len(self.y)):
            raise ValueError("Shape of E is not consistent with grid points")

        self.label = label

    def save(self, fname=None):
        """
        Save the class to a NumPy pickle file.

        Parameters
        ----------
        fname: str
            The output file name for storing the class. If not given the
            `label` attribute of the class will be used and ".npy" will be
            extension.
        """

        if fname is None:
            fname = self.label

        np.save(fname, self, allow_pickle=True)

    @classmethod
    def load(cls, fname):
        """
        Load a saved file containing an instance of this class. The file will
        be a NumPy pickle object with a ".npy" extension.

        Parameters
        ----------
        fname: str
            The name of the file to load
        
        Returns
        -------
        ElectricField
            An ElectricField object.
        """

        E = np.load(fname, allow_pickle=True)

        # NumPy load will load the data as a 0-D NumPy array, so extract the
        # ElectricField object
        E = E.item()

        # check it's the correct type
        if not isinstance(E, cls):
            raise TypeError("Loaded file does not contain an ElectricField")

        return E

    def field_strength(self, x, y):
        """
        Return the electric field strength at any point (interpolated if not
        on the original grid).

        Parameters
        ----------
        x: float
            The x-coordinate position
        y: float
            The y-coordinate position
        
        Returns
        -------
        float
            The electric field strength at the given point.
        """

        # create interpolator
        fieldinterp = interp2d(self.x, self.y, self.E, bounds_error=True)

        try:
            E = fieldinterp(x, y)[0]
        except ValueError:
            raise ValueError(f"x-y coordinates ({x}, {y}) are outside grid "
                             "bounds.")

        return E

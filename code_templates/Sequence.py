class Sequence:
    """ 
    A class to create and manipulate a Fibonacci-style sequence 
    """

    def __init__(self, initialSequence=[0, 1]):
        if not len(initialSequence) > 1:
            raise ValueError("list needs to be at least two elements long to form a sequence")
        
        self.seq = list(initialSequence)  # copy and store initialSequence as the class variable seq

    def __str__(self):
        return "Current Sequence: {}".format(self.seq)

    def value(self, N):
        """
        return the nth value of the sequence where the first element is numbered by 1.

        If a number below 1 is requested None is returned 
        """

        if N < 1:
            return None

        if len(self.seq) < N:
            self.setLength(N)

        # Note computer counting element [0] is the first item in the list!
        return self.seq[N-1]

    def setLength(self, N):
        # use flow control and loops to fill the sequence so it is now length N with the correct values
        if N < 1:
            raise ValueError("You require at least one entry in the sequence")
        # dummy code adding additional zero elements to the list. You need to replace this using 
        # flow control and list operations. 
        dummy =  [0]*(N-len(self.seq))
        self.seq +=  dummy 

    def returnList(self):
        return self.seq

"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """sets the start var and next var to start"""
        self.start = start
        self.next = start

    def __repr__(self):
        return f"<SerialGenerator start={self.start} next={self.next}>"

    def generate(self):
        """returns the previous value + 1"""
        self.next = self.next + 1
        return self.next

    def reset(self):
        """resets the passed value to start """
        self.next = self.start


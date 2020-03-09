__author__ = 'A88253'

class Edge:
    v = None # vertex 1
    w = None # vertex 2
    weight = None # weight

    def __init__(self, v, w, wt):
        self.v = v
        self.w = w
        self.weight = wt

    # return either endpoint
    def either(self):
        return self.v

    # return the other endpoint
    def other(self, v):
        if v==self.v:
            return self.w
        else:
            return self.v

    def __lt__(self, other):
        return self.weight < other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __ge__(self, other):
        return self.weight >= other.weight

    def __le__(self, other):
        return self.weight <= other.weight

    def __eq__(self, other):
        return self.weight == other.weight

    def toString(self):
        return str(self.v) + "-" + \
               str(self.w) + " " + \
               str(self.weight)

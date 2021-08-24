class ClassTypes:
    """
    Stores the valid class types
    """
    YOGA, GYM, DANCE = 0, 1 , 2

class FitnessClass:
    """
    Class contains all the information related to fitness class
    """
    def __init__(self, id, capacity, classType, startTime):
        self.id = id
        self.capacity = capacity
        self.classType = classType
        self.startTime = startTime
        self.occupied = 0

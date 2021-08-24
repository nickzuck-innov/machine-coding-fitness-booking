from models.user_class import UserClassAssociation

class FitnessSlotBooking:
    def __init__(self):
        self.classes = [] # List of models.FitnessClasss
        self.users = []  # List of models.User
        self.bookedUsers = [] # List of models.UserClassAssociation
        self.waitListUsers = [] # List of models.UserClassAssociation

    def add_class(self, classObj):
        self.classes.append(classObj)

    def add_user(self, userObj):
        self.users.append(userObj)

    def find_class(self, class_id):
        for clas in self.classes:
            if clas.id == class_id:
                return clas
        return None

    def inc_occupied(self, class_id):
        for i in range(len(self.classes)):
            if self.classes[i].id == class_id:
                self.classes[i].occupied += 1
        return None

    def dec_occupied(self, class_id):
        for i in range(len(self.classes)):
            if self.classes[i].id == class_id:
                self.classes[i].occupied -= 1
        return None

    # def bookClassUtil(self):


    def book_class(self, class_id, user_id):
        clas = self.find_class(class_id)
        if clas is None:
            return "Cannot book class: class with given id not found"
        if clas.occupied >= clas.capacity:
            self.waitListUsers.append(UserClassAssociation(class_id, user_id))
            return "Class full : You are in waitlist"
        self.bookedUsers.append(UserClassAssociation(class_id, user_id))
        self.inc_occupied(class_id)
        return "Class successfully booked for user : " + user_id


    def cancel_class(self, class_id):
        pass

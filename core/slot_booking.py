from models.user_class import UserClassAssociation
from utils.time_helpers import time_minutes_before, get_curr_time

class FitnessSlotBooking:
    def __init__(self):
        self.classes = [] # List of models.FitnessClasss
        self.users = []  # List of models.User
        self.bookedUsers = [] # List of models.UserClassAssociation
        self.waitListUsers = [] # List of models.UserClassAssociation

    def add_class(self, classObj):
        """
        Adds class to the SlotBooking system
        :param classObj:  models.FitnessClasss object
        :return: None
        """
        self.classes.append(classObj)

    def add_user(self, userObj):
        """
        Adds user to the SlotBooking system
        :param userObj: models.User object
        :return: None
        """
        self.users.append(userObj)

    def find_class(self, class_id):
        """
        Function to find the object of FitnessClass by class_id
        :param class_id: str
        :return: models.FitnessClasss object
        """
        for clas in self.classes:
            if clas.id == class_id:
                return clas
        return None

    def inc_occupied(self, class_id):
        """
        Function to increment the counter of seats occupied
        :param class_id: str
        :return: None
        """
        for i in range(len(self.classes)):
            if self.classes[i].id == class_id:
                self.classes[i].occupied += 1
        return None

    def dec_occupied(self, class_id):
        """
        Function to decrement the counter of seats occupied
        :param class_id: str
        :return: None
        """
        for i in range(len(self.classes)):
            if self.classes[i].id == class_id:
                self.classes[i].occupied -= 1
        return None

    def book_class(self, class_id, user_id):
        """
        Main function to book class by a class id and user id
        :param class_id: str
        :param user_id: str
        :return: str
        """
        clas = self.find_class(class_id)
        if clas is None:
            return "Cannot book class: class with given id not found"
        if clas.occupied >= clas.capacity:
            self.waitListUsers.append(UserClassAssociation(class_id, user_id))
            return "Class full : You are in waitlist"

        # Book class for user
        self.bookedUsers.append(UserClassAssociation(class_id, user_id))
        self.inc_occupied(class_id)
        return "Class successfully booked for user : " + user_id

    def find_user_class_booking_idx(self, class_id, user_id):
        """
        Function to return the index of user's booking for a particular class
        :param class_id: str
        :param user_id:  str
        :return: int / None
        """
        index = 0
        for class_user_assoc in self.bookedUsers:
            if class_user_assoc.user_id == user_id and class_user_assoc.class_id == class_id:
                return index
            index += 1
        return None

    def find_waiting_user_idx(self, class_id):
        """
        Function to find the user waiting for a particular class
        :param class_id: str
        :return: int / None
        """
        index = 0
        for class_user_assoc in self.waitListUsers:
            if class_user_assoc.class_id == class_id:
                return index
            index += 1
        return None

    def assign_waiting_user(self, class_id):
        """
        Main function to assing class to the waiting user after cancellation
        :param class_id: str
        :return: response after class booking
        """
        waitingUserIdx = self.find_waiting_user_idx(class_id)
        if waitingUserIdx is None:
            return None
        classUserAssoc = self.waitListUsers.pop(waitingUserIdx)
        return self.book_class(classUserAssoc.class_id, classUserAssoc.user_id)


    def cancel_class(self, class_id, user_id):
        """
        Main function to cancel the class for a user
        :param class_id: str
        :param user_id: str
        :return: whether a waitlist user has been allocated seat or not
        """
        # Check if we can cancel the class at current time
        clas = self.find_class(class_id)
        if clas is None:
            return "Class not found"

        time30MinutesBefore = time_minutes_before(30)
        if clas.startTime > time30MinutesBefore :
            return "Window to cancel the class is over now"

        # If we can still cancel the class, find the booking and cancel it
        classBookingIdx = self.find_user_class_booking_idx(class_id, user_id)
        if classBookingIdx is None:
            return "Cannot find booking for given class and user"

        # Cancel booking
        self.bookedUsers.pop(classBookingIdx)
        self.dec_occupied(class_id)
        print (f"Class {class_id} cancelled for user {user_id}")

        # Assign the slot to the waiting user
        assignedTo = self.assign_waiting_user(class_id)
        if assignedTo is None:
            return ""
        return assignedTo

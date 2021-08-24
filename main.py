from core.slot_booking import FitnessSlotBooking
from models.users import User
from models.fitness_class import FitnessClass, ClassTypes
from utils.time_helpers import time_minutes_before

if __name__ == '__main__':
    slotBookingObj  = FitnessSlotBooking()
    slotBookingObj.add_user(User("Nikhil"))
    slotBookingObj.add_user(User("Ravi"))
    slotBookingObj.add_user(User("Suman"))

    time30MinsBefore = time_minutes_before(31)
    time60MinsBefore = time_minutes_before(60)
    slotBookingObj.add_class(FitnessClass("class_1", 2, ClassTypes.YOGA, time30MinsBefore))
    slotBookingObj.add_class(FitnessClass("class_2", 1, ClassTypes.GYM, time60MinsBefore))
    slotBookingObj.add_class(FitnessClass("class_3", 10, ClassTypes.DANCE, time60MinsBefore))

    print (slotBookingObj.book_class('class_1', "Nikhil"))
    print (slotBookingObj.book_class('class_1', "Ravi"))
    print (slotBookingObj.book_class('class_1', "Suman"))
    print (slotBookingObj.cancel_class('class_1', "Nikhil"))


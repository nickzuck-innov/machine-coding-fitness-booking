from core.slot_booking import FitnessSlotBooking
from models.users import User
from models.fitness_class import FitnessClass, ClassTypes
import datetime

if __name__ == '__main__':
    slotBookingObj  = FitnessSlotBooking()
    slotBookingObj.add_user(User("Nikhil"))
    slotBookingObj.add_user(User("Ravi"))
    slotBookingObj.add_user(User("Suman"))

    time30MinsBefore = datetime.datetime.now() - datetime.timedelta(minutes= 30)
    time60MinsBefore = datetime.datetime.now() - datetime.timedelta(minutes= 60)
    slotBookingObj.add_class(FitnessClass("class_1", 2, ClassTypes.YOGA, time30MinsBefore))
    slotBookingObj.add_class(FitnessClass("class_2", 1, ClassTypes.GYM, time60MinsBefore))
    slotBookingObj.add_class(FitnessClass("class_3", 10, ClassTypes.DANCE, time60MinsBefore))

    print (slotBookingObj.book_class('class_1', "Nikhil"))
    print (slotBookingObj.book_class('class_1', "Ravi"))
    print (slotBookingObj.book_class('class_1', "Suman"))


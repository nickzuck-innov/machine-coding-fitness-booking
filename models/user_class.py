class UserClassAssociation:
    """
    Association of user with class, basically for storing all the info
    realated to booking of user with class, in case other values are required
    for example: a note maybe
    """
    def __init__(self, class_id, user_id, bookedAt = None):
        self.user_id = user_id
        self.class_id = class_id
        self.bookedAt = bookedAt

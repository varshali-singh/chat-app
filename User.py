import time as t


# ChatApp's user
class User:
    def __init__(self, id, status):
        self.id = id  # userId
        self.status = status  # status whether user is online or offline
        self.statusChangeTime = t.time()  # updated time with updated status

import sys
sys.path.insert(0, '/Database/')
from Database import DataBaseController as dbController

class Collision:
    gps = (0,0)
    timeStamp = 0

    def __init__(self, longitude, latitude, timeStamp):
        self.gps = (longitude,latitude)
        self.timeStamp = timeStamp

    def makeCollision(longitude,latitude,timeStamp):
        collision = Collision((longitude,latitude),timeStamp)
        dbController.uploadCollision(collision)
        return collision
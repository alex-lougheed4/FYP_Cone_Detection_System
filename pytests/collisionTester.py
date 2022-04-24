import pytest
import sys
sys.path.insert(1, '../gui/')

from gui import main


#test collision (with angle) and upload to database
def collisionTest(): 
    angle = 35
    main.setLongitude = 5
    main.setLatitude = 10
    main.collisionOccurred(angle)
    return

#test enter hot area 
def hotAreaTest(): #Where to call in main?
    main.inHotArea = TRUE
    return
#test collision in hot area 
def hotAreaCollisionTest():
    main.inHotArea = TRUE
    angle = 25
    main.setLongitude = 5
    main.setLatitude = 10
    main.collisionOccurred(angle)
    return


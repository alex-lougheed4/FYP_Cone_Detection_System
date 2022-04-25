import pytest
import sys
sys.path.append('..')



#test collision (with angle) and upload to database
def collisionTest(): 
    import main
    angle = 35
    longitude = 5
    latitude = 10
    main.setLongitude = 5
    main.setLatitude = 10
    print(f"Collision Test - Inputs: angle={angle}, longitude={longitude}, latitude={latitude}")
    main.collisionOccurred(angle)
    print(f"Test 1 finished")
    return

#test enter hot area 
def hotAreaTest(): #Where to call in main?
    import main
    print(f"Hot Area Test: Hot Area Bool set to TRUE")
    main.setHotAreaBool(True)
    print(f"Test 2 finished")
    return
#test collision in hot area 
def hotAreaCollisionTest():
    import main
    main.setHotAreaBool(True)
    angle = 25
    longitude = 5
    latitude = 10
    main.setLongitude = 5
    main.setLatitude = 10
    print(f"Hot Area Pre-Collision Test - Inputs: angle={angle}, longitude={longitude}, latitude={latitude}, hotArea Bool set to TRUE")
    main.collisionOccurred(angle)
    print(f"Test 3 finished")
    return

def run(): 
    collisionTest()
    hotAreaTest()
    hotAreaCollisionTest()

print(f"Tests finished")




import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Monkeyboy4",
  database="sys"
)



def uploadCollision(col):
  mycursor = mydb.cursor()

  sql = "INSERT INTO Collisions (GPSLocation, TimeStamp) VALUES (%s, %s)" #gps = tuple of longitude and latitude 
  val = [col.gps, col.timeStamp]

  mycursor.execute(sql, val)
  mydb.commit()
  print("1 record inserted, ID:", mycursor.lastrowid)

def searchForGPS(gpsData):

  #gpsdata + radius calculation
  collisionDetectionRange = gpsData 

  mycursor = mydb.cursor()

  sql = "SELECT * FROM Collisions WHERE GPSLocation = collisionDetectionRange"

  mycursor.execute(sql)

  myresult = mycursor.fetchall()
  return myresult
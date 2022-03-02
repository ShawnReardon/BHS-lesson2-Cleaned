import time
from datetime import datetime 
import pytz 
  
UTC = pytz.utc   

timeZ_Ny = pytz.timezone('America/New_York') 

dt_Ny = datetime.now(timeZ_Ny) 

utc_Ny = dt_Ny.astimezone(UTC) 

timeEST = dt_Ny.strftime('%H:%M:%S %Z')
#print("Date & Time in UTC : ", 
   #   dt_Ny.strftime('%Y:%m:%d %H:%M:%S %Z %z')) 
  


# For 01:30pm, this function returns 30
def getMinute():
  return int(timeEST[3:5])

# For 01:30pm this function returns 01 
def getHour():
  return int(timeEST[0:2])


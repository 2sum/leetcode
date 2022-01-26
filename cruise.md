Our vehicle operations center needs to identify which cars are available for use.  We have access to two APIs which we can use to help them.  

 A get request to http://getcruise.com/cars returns a JSON map of all cars friendly names and their VIN.  A VIN is a 17 character unique identifier consisting of numbers and letters.

 Example:

 """
 {
     "Beetle": "ce1K9WtMd5wXmAdb1",
     "BoltyMcBoltface": "Az6xYDIYdUA3I2EXq",
     "Penguin": "Kefkjfe39KJKf3234djkl"
 }
 """

 A get request to http://getcruise.com/cars/${VIN} returns a digit between 0 and 4 representing the battery level of the cars.

 Example:

 """
 curl http://getcruise.com/cars/ce1K9WtMd5wXmAdb1
 {"battery_level": 1}
 """

Write a small program that will print out the battery level followed by all the friendly names of the cars at that battery level.

# Example Output:

"""
Level 4
BoltyMcBoltface
Penguin
Level 3
Beetle
"""

import random

s = {"Beetle": "ce1K9WtMd5wXmAdb1","BoltyMcBoltface": "Az6xYDIYdUA3I2EXq","Penguin": "Kefkjfe39KJKf3234djkl"} 
res={}

# INPUT: VIN -> OUTPUT: {"battery_level": 1}

def findBatteryLevel(url,vin,make,flag):
    
    url+=vin
    
    r = {"battery_level": random.choice([0, 1, 2, 3, 4])}
    print("GET BATTERY LEVEL: "+str(r))
    battery_level="Level "+str(r["battery_level"])
    if battery_level not in res.keys():
        #print("THIS IS OVERIDING")
        res[battery_level]=[make]
    else:
        res[battery_level].append(make)
    print("RES DICT:",res)
    #print("DEBUG before loop:",flag,res)
    return res
     for k,v in res.items():
             #i+=1
             #print("DEBUG:",len(v),flag,k,v)
         if len(v) >0 and not flag:
             print(k+"\n"+v[0]+"\n")
                 #flag=True
                
         else:
                 #print("IN ELSE")
             print(v[i]+"\n")
        # else:
        #     if len(v)>1:
        #         for j in range(1,len(v)-1):
        #             print(v[j]+"\n")

    
   
    

url = 'http://getcruise.com/cars/'
flag=False
for make,vin in s.items():
    findBatteryLevel(url,vin,make,flag)
    flag=True
print("--------------------------")      
for k,v in res.items():
    print(k)
    for i in v:
        print(i)

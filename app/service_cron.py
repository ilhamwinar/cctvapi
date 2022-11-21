import os
import ast
import time
from collections import Counter
from datetime import datetime

list_minutes=[]
z = {}

for i in range(5):
    time.sleep(61)
    time.sleep(500/1000)
    f = open('temp.txt', 'r')
    api=f.read()
    print(type(api))
    dictapi = ast.literal_eval(api)
    id=dictapi['id']
    dictapi.pop('id')
    dictapi.pop('time')
    list_minutes.append(dictapi)
    
    print(list_minutes)
    print(len(list_minutes))

total_kr_down=list_minutes[0]['total_kr_down']+list_minutes[1]['total_kr_down']+list_minutes[2]['total_kr_down']+list_minutes[3]['total_kr_down']+list_minutes[4]['total_kr_down']
Bus_down=list_minutes[0]['Bus_down']+list_minutes[1]['Bus_down']+list_minutes[2]['Bus_down']+list_minutes[3]['Bus_down']+list_minutes[4]['Bus_down']
car_down=list_minutes[0]['car_down']+list_minutes[1]['car_down']+list_minutes[2]['car_down']+list_minutes[3]['car_down']+list_minutes[4]['car_down']
truck_down=list_minutes[0]['truck_down']+list_minutes[1]['truck_down']+list_minutes[2]['truck_down']+list_minutes[3]['truck_down']+list_minutes[4]['truck_down']
total_kr_up=list_minutes[0]['total_kr_up']+list_minutes[1]['total_kr_up']+list_minutes[2]['total_kr_up']+list_minutes[3]['total_kr_up']+list_minutes[4]['total_kr_up']
Bus_up=list_minutes[0]['Bus_up']+list_minutes[1]['Bus_up']+list_minutes[2]['Bus_up']+list_minutes[3]['Bus_up']+list_minutes[4]['Bus_up']
car_up=list_minutes[0]['car_up']+list_minutes[1]['car_up']+list_minutes[2]['car_up']+list_minutes[3]['car_up']+list_minutes[4]['car_up']
truck_up=list_minutes[0]['truck_up']+list_minutes[1]['truck_up']+list_minutes[2]['truck_up']+list_minutes[3]['truck_up']+list_minutes[4]['truck_up']
z.update({"total_kr_down": total_kr_down})
z.update({"Bus_down": Bus_down})
z.update({"car_down": car_down})
z.update({"truck_down": truck_down})
z.update({"total_kr_up": total_kr_up})
z.update({"Bus_up": Bus_up})
z.update({"car_up": car_up})
z.update({"truck_up": truck_up})
print(z)

dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%d-%m-%Y %H:%M:%S.%f")
#print('Current Timestamp : ', timestampStr)
if sum(z.values())==0:
    print("antiran list kosong")
    os.system("docker restart aicctv")
    
    z.update({"id": id})
    z.update({"time": timestampStr})
else:
    print("tidak kosong")
    z.update({"id": id})
    z.update({"time": timestampStr})

result = open("temp_result.txt", "w")
print(z)
result.write(str(z))
result.close()




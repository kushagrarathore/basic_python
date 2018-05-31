import time
current_time = time.time()
# print(current_time)
total_second = int((current_time) + (5.30*60*60))
current_second = total_second % 60
# print(current_second)
total_minutes = total_second//60
current_minutes = total_minutes % 60
# print(current_minutes)
total_hours = total_minutes//60
current_hours = total_hours % 24
# print(current_hours)
print("Current Time IS  ",current_hours ,":",current_minutes, ":", current_second )
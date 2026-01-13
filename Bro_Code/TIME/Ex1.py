import time

# print(time.ctime(10000000))

# print(time.time())

time_object = time.localtime()
print(time_object)
# print(time.gmtime())

local_time = time.strftime("%B %d %Y %H:%M:%S",time_object)

print(local_time)

time_str = "24 June 2023" 
time_form = time.strptime(time_str,"%d %B %Y")

print(time_form)
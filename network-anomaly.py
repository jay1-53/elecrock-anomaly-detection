import psutil

from datetime import datetime

#8am to 5pm 
dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("(%H:%M:%S.%f)")
startTimeStr = "08:00:00"
endTimeStr = "17:00:00"
initial_process_count = 0
network_usage = []
cpu_usage = []
storage_usage = []
# if(timestampStr == startTimeStr): #comment out for test run
process_count = 0
for proc in psutil.process_iter(): initial_process_count += 1
NETWORK_INTERFACE = 'Ethernet'
netio = psutil.net_io_counters(pernic=True)
net_usage = netio[NETWORK_INTERFACE].bytes_recv
temporary_network_value = net_usage
bytes_received = 0
NETWORK_LIMIT = net_usage + 5368709120
while len(network_usage) != 20:
    ### *** CPU FUNCTIONS ***
    cpu_usage_percentage = psutil.cpu_percent()
    cpu_usage.append(cpu_usage_percentage)
    # Disk usage statistics
    disk_usage = psutil.disk_usage('/')
    storage_usage.append(disk_usage)
    netio = psutil.net_io_counters(pernic=True)
    net_usage = netio[NETWORK_INTERFACE].bytes_recv
    if net_usage > NETWORK_LIMIT:
        print("Meets network limit!")
    bytes_received = net_usage - temporary_network_value
    temporary_network_value = net_usage
    network_usage.append(bytes_received)
    for proc in psutil.process_iter(): process_count += 1
    # print(initial_process_count) #for debugging
    # print(process_count) #for debugging
    if(process_count != initial_process_count):
        initial_process_count = 0
        for proc in psutil.process_iter():
            try:
                pinfo = proc.as_dict(attrs=['pid', 'name'])
            except psutil.NoSuchProcess:
                pass
            else:
                initial_process_count += 1
                #print(pinfo) #show list of files when new file was opened
                #scan files here
    process_count = 0
else:
    print(timestampStr)
# print(network_usage) # for debugging
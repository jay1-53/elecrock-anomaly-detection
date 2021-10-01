import psutil

from datetime import datetime

#8am to 5pm 
dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("(%H:%M:%S.%f)")
startTimeStr = "08:00:00"
endTimeStr = "17:00:00"
initial_process_count = 0
if(timestampStr == startTimeStr): #comment out for test run
    process_count = 0
    for proc in psutil.process_iter(): initial_process_count += 1
    NETWORK_INTERFACE = 'Ethernet'
    netio = psutil.net_io_counters(pernic=True)
    net_usage = netio[NETWORK_INTERFACE].bytes_sent + netio[NETWORK_INTERFACE].bytes_recv
    starting_value = net_usage
    NETWORK_LIMIT = net_usage + 5368709120
    while timestampStr != endTimeStr:
        netio = psutil.net_io_counters(pernic=True)
        net_usage = netio[NETWORK_INTERFACE].bytes_sent + netio[NETWORK_INTERFACE].bytes_recv
        if net_usage > NETWORK_LIMIT:
            print("Meets network limit!")
        print(net_usage, "bytes has been used")
        for proc in psutil.process_iter(): process_count += 1
        print(initial_process_count) #for debugging
        print(process_count) #for debugging
        if(process_count != initial_process_count):
            initial_process_count = 0
            for proc in psutil.process_iter():
                try:
                    pinfo = proc.as_dict(attrs=['pid', 'name'])
                except psutil.NoSuchProcess:
                    pass
                else:
                    initial_process_count += 1
                    print(pinfo) #show list of files when new file was opened
                    #scan files here
        process_count = 0
    else:
        print(timestampStr)
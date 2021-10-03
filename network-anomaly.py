import psutil
from numpy import asarray
from numpy import savez_compressed
from datetime import datetime
import time

def dateTime():
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%H-%M-%S-%f")
    return timestampStr

def log_network_sent(timestampStr, network_sent_byte_usage):
    savez_compressed('logs/network_usage-'+timestampStr+'.npz', network_sent_byte_usage)
    return

def log_network_receive(timestampStr, network_sent_byte_usage):
    savez_compressed('logs/network_usage-'+timestampStr+'.npz', network_sent_byte_usage)
    return

def log_storage(timestampStr, storage_usage):
    savez_compressed('logs/storage_usage-'+timestampStr+'.npz', storage_usage)
    return

def log_cpu(timestampStr, cpu_usage):
    savez_compressed('logs/cpu_usage-'+timestampStr+'.npz', cpu_usage)
    return

def data_gather(timestampStr):
    # initial_process_count = 0
    network_usage = []
    cpu_usage = []
    storage_usage = []
    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        ### VALUES FOR SOFTWARE PROCESSES GATHERING ###
        # process_count = 0
        # for proc in psutil.process_iter(): initial_process_count += 1
        ### ----------------------------------------
        NETWORK_INTERFACE = 'Ethernet'
        netio = psutil.net_io_counters(pernic=True)
        net_usage = netio[NETWORK_INTERFACE].bytes_recv
        temporary_network_value = net_usage
        bytes_received = 0

        # NETWORK_LIMIT = net_usage + 5368709120
        
        ### CPU Statistics
        cpu_usage_percentage = psutil.cpu_percent()
        cpu_usage.append(cpu_usage_percentage)
        ### Disk usage statistics
        storage_usage_stats = psutil.disk_usage('/')
        storage_usage.append(storage_usage_stats)
        ### Network Receive
        netio = psutil.net_io_counters(pernic=True)
        net_usage = netio[NETWORK_INTERFACE].bytes_recv

        ###---FOR NETWORK LIMITING---
        # if net_usage > NETWORK_LIMIT:
        #     print("Meets network limit!")
        #     more process here
        ###--------------------------

        ###
        bytes_received = net_usage - temporary_network_value
        temporary_network_value = net_usage
        network_usage.append(bytes_received)

        ###---PROCESS LIST GATHERING---
        # for proc in psutil.process_iter(): process_count += 1
        # # print(initial_process_count) #for debugging
        # # print(process_count) #for debugging
        # if(process_count != initial_process_count):
        #     initial_process_count = 0
        #     for proc in psutil.process_iter():
        #         try:
        #             pinfo = proc.as_dict(attrs=['pid', 'name'])
        #         except psutil.NoSuchProcess:
        #             pass
        #         else:
        #             initial_process_count += 1
        #             #print(pinfo) #show list of files when new file was opened
        #             #scan files here
        # process_count = 0
        ###------------------------------

        if elapsed_time > seconds:
            print(timestampStr)
            log_network_receive(timestampStr, network_usage)
            log_network_sent(timestampStr, network_usage)
            log_storage(timestampStr, storage_usage)
            log_cpu(timestampStr, cpu_usage)
            break
        

x = 0 #as number of times it should be repeated using minutes

#replace (x != n) with True to continuously run the program
while x != 2:
    start_time = time.time()
    seconds = 60
    y = dateTime()
    data_gather(y)
    #delete this if the while loop is turned into True
    x += 1


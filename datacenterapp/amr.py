import socket
import json
from .rbkNetProtoEnums import *
import os
import time
import socket

def amr_command(point):
   
    # Constants for the first connection
    PACK_FMT_STR_1 = '!BBHLH6s'
    IP_1 = '192.168.100.141'
    Port_1 = 19206

    # Constants for the second connection
    PACK_FMT_STR_2 = '!BBHLH6s'
    IP_2 = '192.168.100.141'
    Port_2 = 19204

    # Create socket connection 1
    so1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    so1.connect((IP_1, Port_1))
    so1.settimeout(5)

    # Sending and receiving from the first robot
    reqId1 = 1
    reqId1 = int(reqId1)

    msg_name1 = robot_task_gotarget_req
    if point == "LM15" or point == "LM10" or point == "LM7":
        data1 = {
        "id": point,
        "task_id": "87654321",
        # "method": "backward",
        "max_speed": 0.3,
        "max_wspeed": 0.3,
        "max_acc": 0.15,
        "max_wacc": 0.15,
        }
    elif point == "HR2":
        data1 = {
        "id": point,
        "task_id": "87654321",
        # "method": "backward",
        "max_speed": 0.9,
        "max_wspeed": 0.9,
        "max_acc": 0.80,
        "max_wacc": 0.80,
        }
    else:
        data1 = {
        "id": point,
        "task_id": "87654321",
        # "method": "backward",
        }

    so1.send(packMsg(reqId1, msg_name1, data1))

    try:
        data = so1.recv(16)
    except socket.timeout:
        print('timeout')
        quit()

    jsonDataLen = 0
    backReqNum = 0
    if(len(data) < 16):
        print('pack head error')
        print(data)
        os.system('pause')
        so1.close()
        quit()
    else:
        jsonDataLen, backReqNum = unpackHead(data)
        print('json datalen: %d, backReqNum: %d' % (jsonDataLen, backReqNum))

    if(jsonDataLen > 0):
        data = so1.recv(1024)
        ret = json.loads(data)
        print(ret)

    # Create socket connection 2
    so2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    so2.connect((IP_2, Port_2))
    so2.settimeout(5)

    # Run the listening part in a loop
    current_station = ''
    while current_station != point:
        # Handle commands first
        # main()

        reqId2 = 1
        reqId2 = int(reqId2)

        msg_name2 = robot_status_loc_req

        data2 = {}  # No data needed for this request

        so2.send(packMsg(reqId2, msg_name2, data2))

        try:
            data = so2.recv(16)
        except socket.timeout:
            print('timeout')
            quit()

        jsonDataLen, backReqNum = unpackHead(data)

        if jsonDataLen > 0:
            data = so2.recv(jsonDataLen)
            ret = json.loads(data)
            current_station = ret.get('current_station')
            print(f'Current Station: {current_station}')

        time.sleep(1)
    # Close the socket after the loop
    so1.close()
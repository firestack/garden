import requests
import json
from multiprocessing import Queue, Pool
import multiprocessing
import timeit
import time

################################################################
# Python twitch chat searcher
# Copyright Firestack 2015
################################################################
PROCESS_COUNT = 8
MAX_ITER = 10
GEN_FUNC = lambda x : x**2
endpoint = {
    "chatters" : "tmi.twitch.tv/group/user/{user}/chatters",
    "follows" : "api.twitch.tv/kraken/users/{user}/follows/channels"
}







def kernel_A(a):
    return a * a * a

def kernel_B(a):
    return a ** (1.0/3.0)

def process_pool(arr):
    with Pool(PROCESS_COUNT) as P:
        result = P.map(kernel_A, arr)
        result = P.map(kernel_B, result)




def serial(arr):

    result = []
    for i in arr:
        result.append(kernel_A(i))
    resulto = result
    result = []
    for i in resulto:
        result.append(kernel_B(i))



def timeme(func, args, name="", ID="", write=False, **kwargs):
    start = time.clock()
    func(*args)
    end = time.clock()
    total = end-start

    if write:
        print("Test",name,ID,"Has Finished With:",total )
        for i in kwargs.items():
            print(i[0],":",i[1])

    return_val = kwargs
    return_val["time"] = total
    return_val["start"] = start
    return_val["end"] = end
    return_val["name"] = name
    return_val["ID"] = ID
    return return_val



def main():
    log = {
        "pp":[],
        "sl":[]
    }
    for i in range(MAX_ITER):
        print("Generating New Set of Data...")
        DATA = [x for x in range(GEN_FUNC(i))]
        log["pp"].append(timeme(process_pool, (DATA,), "process pool", i, False, IValue=i))
        log["sl"].append(timeme(serial, (DATA,), "serial", i, False, IValue=i))

    #calc average
    temp = []
    for i in log["pp"]:
        temp.append(i["time"])
    print(sum(temp)/len(temp))

    temp = []
    for i in log["sl"]:
        temp.append(i["time"])
    print(sum(temp)/len(temp))





    """
    workers = [worker(i, workQueue) for i in range(PROCESS_COUNT)]
    workerProcesses = []
    for i in range(PROCESS_COUNT):
        workerProcesses.append(multiprocessing.Process(target=(workers[i]).invoke))
        workerProcesses[i].start()
    """




if __name__ == '__main__':
    main()

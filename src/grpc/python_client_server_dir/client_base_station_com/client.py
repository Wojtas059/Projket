from __future__ import print_function


import logging
from queue import Queue
from unicodedata import name
from urllib import response

import grpc
import src.grpc.protos_dir.protos_base_station_com.client_base_station_pb2 as ServicerMethods
import src.grpc.protos_dir.protos_base_station_com.client_base_station_pb2_grpc as Servicer



def main():
    channel = grpc.insecure_channel("192.168.1.107:50051")
    stub = Servicer.ClientBaseStationStub(channel)
    response = stub.checkConnection(ServicerMethods.CheckConnection(stats="client"))
    print("Greeter client received: "+ response.stats)
    response = stub.checkConnection(ServicerMethods.OrderSTM(order="Sampling"))
    if response=="Sampling":
        print(response)
    
def empty():
    pass

if __name__ == "__main__":
    logging.basicConfig()
    main()
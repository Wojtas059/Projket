from __future__ import print_function

import logging
import threading
from queue import Queue
from unicodedata import name
from urllib import response

import grpc
import src.grpc.protos_dir.protos_base_station_com.client_base_station_pb2 as ServicerMethods
import src.grpc.protos_dir.protos_base_station_com.client_base_station_pb2_grpc as Servicer


def get_data(_stub):
    results = _stub.sendSTMData(ServicerMethods.Void())

    # for x in results:
    # print(x.data)


def wait_for_end(_stub):
    command = input()
    if command == "stop":
        response = _stub.stopSTMSampling(ServicerMethods.OrderSTM(order="Sampling"))
        print(response)
        return False
    return True


def main():
    channel = grpc.insecure_channel("192.168.1.107:50051")
    stub = Servicer.ClientBaseStationStub(channel)
    response = stub.checkConnection(ServicerMethods.CheckConnection(stats="client"))
    print("Greeter client received: " + response.stats)
    response = stub.startSTMSampling(ServicerMethods.OrderSTM(order="Sampling"))
    print(response.stats)
    if response.stats == "Sampling":
        threading.Thread(target=get_data, args=[stub]).start()
        while wait_for_end(stub):
            print("test")


def empty():
    pass


if __name__ == "__main__":
    logging.basicConfig()
    main()

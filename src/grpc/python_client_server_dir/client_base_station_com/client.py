from __future__ import print_function

import queue

import grpc
import src.grpc.protos_dir.protos_base_station_com.client_base_station_pb2 as ServicerMethods
import src.grpc.protos_dir.protos_base_station_com.client_base_station_pb2_grpc as Servicer


class Client:
    def __init__(self):
        self.channel = None
        self.stub = None
        self.transfer_status = False
        self.channel = grpc.insecure_channel("raspberrypi:50051")
        self.stub = Servicer.ClientBaseStationStub(self.channel)

    def connect(self):
        try:
            response = self.stub.checkConnection(
                ServicerMethods.CheckConnection(stats="client")
            )
            if response.stats == "Active":
                return True
            else:
                return False
        except grpc._channel._InactiveRpcError:
            return False

    def stop_connection(self):
        try:
            self.channel.close()
        except grpc._channel._MultiThreadedRendezvous:
            pass

    def startSTM(self):
        response = self.stub.startSTMSampling(
            ServicerMethods.OrderSTM(order="Sampling")
        )

        if response.stats == "Sampling":
            self.transfer_status = True
            return True
        else:
            return False

    def stopSTM(self):
        response = self.stub.stopSTMSampling(ServicerMethods.OrderSTM(order="Idle"))
        if response.stats == "Idle":
            self.transfer_status = False
            return True
        else:
            return False

    def getDataSTM(self):
        file = open("data_stm_sampling.csv", "w")
        file.write("Value A, Value B, Value C, Constant value\n")
        file.close()
        queue_data = queue.Queue()
        while self.transfer_status:
            results = self.stub.sendSTMData(ServicerMethods.Void())
            for result in results:
                queue_data.put(float(result.data))
                # file.write(result.data)
        # file = open("data_stm_sampling.csv","a")
        # while queue_data.qsize() > 0:
        #    file.write(queue_data.get())
        # file.close()

    # for x in results:
    # print(x.data)

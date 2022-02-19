from __future__ import print_function

import grpc
import src.grpc.protos_dir.protos_base_station_com.client_base_station_pb2 as ServicerMethods
import src.grpc.protos_dir.protos_base_station_com.client_base_station_pb2_grpc as Servicer



class Client:
    channel = None
    stub = None
    transfer_status = False

    def __init__(self):
        self.channel = grpc.insecure_channel("192.168.1.107:50051")
        self.stub = Servicer.ClientBaseStationStub(self.channel)

    def connect(self):
        response = self.stub.checkConnection(ServicerMethods.CheckConnection(stats="client"))
        if response.stats == "Active":
            return True
        else:
            return False
        

    def startSTM(self):
        response = self.stub.startSTMSampling(ServicerMethods.OrderSTM(order="Sampling"))
        
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
        while(self.transfer_status):
            results = self.stub.sendSTMData(ServicerMethods.Void())
            for result in results:
                file.write(result.data)
    
        file.close()
    # for x in results:
    # print(x.data)


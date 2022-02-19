import logging
from concurrent import futures
from queue import Queue

import grpc
import src.grpc.protos_dir.protos_base_station_com.client_base_station_pb2 as ServicerMethods
import src.grpc.protos_dir.protos_base_station_com.client_base_station_pb2_grpc as Servicer
from file.mygrid import Connect as ConnectSTM32


class BaseStation(Servicer.ClientBaseStationServicer):
    def __init__(self) -> None:
        super().__init__()
        self._my_status = "Active"
        self._stm_status = ""
        self._stm_manager = ConnectSTM32()

    def checkConnection(self, request, context):
        return ServicerMethods.ConnectionStats(stats=self._my_status)

    def checkSTMConnection(self, request, context):
        return ServicerMethods.ConnectionStats(stats=self._stm_status)

    def stopSTMSampling(self, request, context):
        self._stm_manager.stop()
        self._stm_status = request.order
        return ServicerMethods.ConnectionStats(stats=self._stm_status)

    def startSTMSampling(self, request, context):
        self._stm_manager.start()
        self._stm_status = request.order
        print(self._stm_status)
        return ServicerMethods.ConnectionStats(stats=self._stm_status)

    def sendSTMData(self, request, context):
        while True:
            if self._stm_status == "Sampling":
                if self._stm_manager.queue.qsize() > 0:
                    dupa = self._stm_manager.queue.get()
                    print("Wysłane:"+dupa)
                    yield ServicerMethods.STMData(data=dupa)
    #TODO: Function returning the rest of the queue, update proto...

def start_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Servicer.add_ClientBaseStationServicer_to_server(BaseStation(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    start_server()

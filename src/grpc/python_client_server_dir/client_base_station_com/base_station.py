import logging
from concurrent import futures
from queue import Queue

import grpc
import src.grpc.protos_dir.protos_base_station_com.client_base_station_pb2 as ServicerMethods
import src.grpc.protos_dir.protos_base_station_com.client_base_station_pb2_grpc as Servicer
from file.mygrid import Connect as ConnectSTM32


class BaseStation(Servicer.ClientBaseStationServicer):
    _my_status = "Active"
    _stm_status = ""
    _stm_manager = ConnectSTM32()


    def checkConnection(self, request, context):
        return ServicerMethods.ConnectionStats(stats=self._my_status)

    def checkSTMConnection(self, request, context):
        return ServicerMethods.ConnectionStats(stats=self._stm_status)

    def stopSTMSampling(self, request, context):
        self._stm_manager.stop()
        self._stm_status=request.stats
        return ServicerMethods.ConnectionStats(stats=self._stm_status)

    def startSTMSampling(self, request, context):
        self._stm_manager.start()
        self._stm_status=request.stats
        return  self._stm_status
       
    def sendSTMData(self, request, context):
         while self._stm_status == "Sampling":
            if self._stm_manager.queue.qsize > 0:
                yield self._stm_manager.queue.get()
         while self._stm_manager.queue.qsize > 0:
            yield self._stm_manager.queue.get()

def start_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Servicer.add_ClientBaseStationServicer_to_server(BaseStation(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    start_server()

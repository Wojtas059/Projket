
from queue import Queue
from src.grpc.protos_dir.protos_base_station_com.client_base_station_pb2_grpc import ClientBaseStationServicer as Servicer
import src.grpc.protos_dir.protos_base_station_com.client_base_station_pb2 as ServicerMethods

class BaseStation(Servicer):
    _my_status = "Active"
    _stm_status = ""
    _stm_data_queue = Queue()

    def checkConnection(self, request, context):
        return ServicerMethods.ConnectionStats(stats=self._my_status)

    def checkSTMConnection(self, request, context):
        return ServicerMethods.ConnectionStats(stats=self._stm_status)

    def stopSTMSampling(self, request, context):
        return ServicerMethods.ConnectionStats(stats=self._stm_status)
    def startSTMSampling(self, request, context):
        while self._stm_status=="Sampling":
           if self._stm_data_queue.qsize>0:
              yield self._stm_data_queue.get()
        while self._stm_data_queue.qsize>0:
            yield self._stm_data_queue.get()

    